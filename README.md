# 🚖 Uber Fare Prediction Web Service

## 📝 Problem Statement
A web service is needed to predict Uber fares, which should be up and running for live fare predictions.

## 💡 Solution Overview
To address this, the following steps were undertaken:

- **🔄 Virtual Environments**: Created two virtual environments to manage dependencies separately for development and production.
- **📈 Machine Learning Model**: Developed an ML model and used **MLflow** to track training experiments and log models.
- **🌐 Flask API**: Built a Flask API to serve the model for predictions.
- **🐳 Dockerization**: Dockerized the app, bundling the production model and environment requirements.
- **☁️ Deployment**: Deployed the Docker container to **GCP Cloud Run** for scalable and efficient access to the model.

## 🚀 Deployment
The app is deployed on GCP Cloud Run to ensure it can scale based on demand.

## 📦 Usage
You can make predictions for Uber fares using the following code snippet:
```
import requests
url = 'https://uber-fare-model-4j2w2fn3sq-uc.a.run.app/predict'
response = requests.post(url, json=data)
```
**data** object is a dictionary of lists that should contain the following features:
- **`pickup_datetime`**: Timestamp (Date and time when the ride was requested)
- **`pickup_longitude`**: Float (Longitude of the pickup location)
- **`pickup_latitude`**: Float (Latitude of the pickup location)
- **`dropoff_longitude`**: Float (Longitude of the dropoff location)
- **`dropoff_latitude`**: Float (Latitude of the dropoff location)
- **`passenger_count`**: Integer (Number of passengers)

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **MLflow**
- **Docker**
- **GCP Cloud Run**
