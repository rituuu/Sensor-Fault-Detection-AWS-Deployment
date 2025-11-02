from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os, sys
from sensor.logger import logging
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import read_yaml_file, load_object
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from sensor.constant.application import APP_HOST, APP_PORT
from sensor.ml.model.estimator import ModelResolver, TargetValueMapping
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response, StreamingResponse
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
import pandas as pd
from io import BytesIO


env_file_path=os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):
    env_config = read_yaml_file(env_file_path)
    os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


app = FastAPI(title="Sensor Fault Detection API")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("TRAINING COMPLETELY SUCCESSFULL !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict", tags=["Prediction"])
async def predict_route(file: UploadFile = File(...)):
    """
    Upload a CSV file and get predictions as downloadable CSV.
    """
    try:
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))

        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            raise HTTPException(status_code=404, detail="Model is not available")

        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)

        y_pred = model.predict(df)

        df["prediction"] = ["Yes" if val == 1 else "No" for val in y_pred]

        output = BytesIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return StreamingResponse(
            output,
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=predictions.csv"},
        )

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Uploaded file is empty or invalid CSV.")
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=500, detail=f"Error Occurred: {str(e)}")


def main():
    try:
        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__=="__main__":
    #main()
    set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT)
