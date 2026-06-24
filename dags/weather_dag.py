from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
sys.path.insert(0, os.path.expanduser("~/airflow"))

from etl.extract import extract_weather
from etl.transform import transform_weather
from etl.load import load_weather

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def run_extract(**context):
    data = extract_weather()
    context["ti"].xcom_push(key="raw_data", value=data)

def run_transform(**context):
    raw = context["ti"].xcom_pull(key="raw_data", task_ids="extract")
    df = transform_weather(raw)
    context["ti"].xcom_push(key="transformed", value=df.astype(str).to_dict())

def run_load(**context):
    import pandas as pd
    data = context["ti"].xcom_pull(key="transformed", task_ids="transform")
    df = pd.DataFrame(data)
    load_weather(df)

with DAG(
    dag_id="weather_etl",
    default_args=default_args,
    description="ETL pipeline for weather data",
    schedule="@hourly",       # runs every hour
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    extract = PythonOperator(task_id="extract", python_callable=run_extract)
    transform = PythonOperator(task_id="transform", python_callable=run_transform)
    load = PythonOperator(task_id="load", python_callable=run_load)

    extract >> transform >> load      # defines order