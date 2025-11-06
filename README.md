
#  Sensor Fault Detection — End-to-End AI & MLOps Project

This repository contains the **complete Sensor Fault Detection System**, integrating **Data Engineering, Machine Learning, and MLOps** to build a production-grade pipeline for predictive maintenance in heavy-duty vehicles.

The system identifies **Air Pressure System (APS)** faults by analyzing live sensor data streams, automating the entire lifecycle — from **data ingestion** to **real-time fault prediction APIs**.

---

## Project Summary

The **Sensor Fault Detection** project represents an end-to-end implementation of an AI-powered fault detection system designed for **industrial IoT (IIoT)** use cases.

It automates:

* **Data Streaming & Storage** → Real-time sensor data via Apache Kafka to MongoDB.
* **Data Validation & Transformation** → Ensures schema integrity, drift detection, and preprocessing.
* **Model Training & Evaluation** → Binary classification using optimized ML pipelines.
* **Model Serving** → Exposes `/train` and `/predict` endpoints via FastAPI.
* **Deployment** → Dockerized and CI/CD-ready for scalable deployment on AWS or local environments.

By reducing false positives and improving system reliability, this project supports **predictive maintenance** and **cost-effective operations** in safety-critical automotive systems.

---

## 🌟 Key Achievements

* 🧩 **Engineered** a complete real-time data pipeline using **Kafka** and **MongoDB** handling **35,000+ APS sensor readings**.
* 🤖 **Developed** an ML pipeline for **binary classification** to detect APS-related faults.
* ⚙️ **Integrated** ETL, validation, transformation, training, and prediction workflows under one MLOps framework.
* 🧠 **Deployed** containerized **FastAPI endpoints** for `/train` and `/predict` supporting scalable inference.
* ☁️ **Enabled** CI/CD-ready and **environment-driven configuration** for smooth deployment across cloud platforms.

---
## Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

The **Air Pressure System (APS)** provides compressed air for vehicle braking and gear systems.
Faults in APS components can lead to unsafe operation, so early detection is crucial.

* **Positive Class:** Fault due to APS components
* **Negative Class:** Other unrelated failures
* **Goal:** Minimize false positives and reduce unnecessary maintenance.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

#### The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
---

## 🏗️ System Architecture

```
                ┌────────────────────────┐
                │   Local Data Source    │
                └────────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Apache Kafka       │
                  │  (Producer + Topic)  │
                  └────────────┬─────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Kafka Consumer →     │
                  │     MongoDB Store    │
                  └────────────┬─────────┘
                             │
                             ▼
                ┌─────────────────────────────┐
                │ ETL Pipeline (Ingestion,    │
                │ Validation, Transformation) │
                └────────────┬────────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Model Training &     │
                  │ Evaluation           │
                  └────────────┬─────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ FastAPI Endpoints      │
                │ /train & /predict      │
                └────────────────────────┘
```

## Components

### **1. Data Engineering (ETL)**

* Streams live APS sensor data to Kafka.
* Consumes and stores data in MongoDB.
* Performs automated ingestion, validation, and transformation.
 
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)


### **2. Machine Learning (Model Training)**

* Binary classification model to predict fault occurrence.
* Trained using validated and transformed features.
* Evaluates using accuracy, precision, recall, and F1-score.
  #### Project Architecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)

### **3. MLOps Deployment**

* Fully containerized using **Docker**.
* Integrated with **CI/CD pipelines** for automated build and deployment.
  ####  **Fast API endpoint**

* **/train** — Triggers data ingestion, validation, transformation, and model retraining.
* **/predict** — Accepts sensor input data and returns real-time fault prediction.
* Implemented using **FastAPI** with structured logging.
  
  #### Deployment Architecture
  <img width="919" height="260" alt="image" src="https://github.com/user-attachments/assets/b0ba3d15-6c9f-4d4c-a23a-e7bffb2df3a5" />
  
---

## Tech Stack

| Layer           | Tools & Technologies |
| --------------- | -------------------- |
| Streaming       | Apache Kafka         |
| Database        | MongoDB              |
| Programming     | Python               |
| API Framework   | FastAPI              |
| Version Control | Git, Github          |
| MLOps           | CI/CD Integration, Github Actions |
| Deployment      | AWS EC2, ECR and S3, Docker   |

---

## How It Works

1. **Kafka Producer** streams sensor data from the local environment.
2. **Kafka Consumer** listens to the topic and writes data to MongoDB.
3. **Data Ingestion** fetches the latest records for preprocessing.
4. **Data Validation** ensures schema integrity and checks for drift.
5. **Data Transformation** scales and encodes features for training.
6. **Model Training** executes and stores the trained model artifact.
7. **FastAPI Service** exposes endpoints for real-time retraining and prediction.

---

## Output Artifacts

| Stage          | Output                                    |
| -------------- | ----------------------------------------- |
| Ingestion      | train.csv, test.csv                       |
| Validation     | drift_report.yaml                         |
| Transformation | train.npy, test.npy, preprocessing.pkl    |
| Model Training | model.pkl, metrics.json                   |
| Serving        | FastAPI endpoints `/train` and `/predict` |

---

## 🧾 Summary (Impact)

This project showcases the integration of **Data Engineering + Machine Learning + MLOps**, aligning with real-world **AI infrastructure** standards.
It demonstrates:

* **Automation:** Minimal human intervention across the ML lifecycle.
* **Scalability:** Modular, Dockerized setup ready for enterprise environments.
* **Production-grade Design:** Real-time ingestion, validation, training, and inference flow.
  
---
## Project Setup for running locally
#### Step 1: Clone the repository
```bash
git clone https://github.com/rituuu/Sensor-Fault-Detection-AWS-Deployment.git
```

#### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.11.13 -y
```

```bash
conda activate sensor
```

#### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

#### Step 4 - Set environment variable in .env file
Make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances. Once AWS account is created, add the below environment variables: 
```bash
AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

MONGODB_URL="mongodb+srv://<username>:<password>@-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```

#### Step 5 - Run the application server
```bash
python main.py
```

#### Step 6. Train application
```bash
http://localhost:8080/train

```

#### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

#### Run locally using Docker

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

## 📚 License & Attribution

Developed by **Ritu Gujela**

---
