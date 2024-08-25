🚖 Uber Fare Prediction Web Service
📝 Problem Statement
A web service is needed to predict Uber fares, which should be up and running for real-time fare predictions.

💡 Solution Overview
To address this, the following steps were undertaken:

🔄 Virtual Environments: Created two virtual environments to manage dependencies separately for development and production.
📈 Machine Learning Model: Developed an ML model and used MLflow to track training experiments and log models.
🌐 Flask API: Built a Flask API to serve the model for predictions.
🐳 Dockerization: Dockerized the app, bundling the production model and environment requirements.
☁️ Deployment: Deployed the Docker container to GCP Cloud Run for scalable and efficient access to the model.
🚀 Deployment
The app is deployed on GCP Cloud Run to ensure it can scale based on demand.

📦 Usage
Once the container is running, the web service will be available to make predictions for Uber fares.

🛠️ Technologies Used
Python
Flask
MLflow
Docker
GCP Cloud Run
