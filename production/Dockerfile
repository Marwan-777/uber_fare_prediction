FROM python:3.12.0-slim

WORKDIR /app

COPY production_model.bin prediction_API_script.py prod_env_requirements.txt /app

RUN pip install -r prod_env_requirements.txt

EXPOSE 9696

CMD ["python", "prediction_API_script.py"]