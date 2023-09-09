from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from spotfy_etl import run_spotify_etl, db_connect, get_token

default_args = {
    'owner': 'guilherme iglesia',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 9),
    'email': ['gui.henrique333@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotfy_dag',
    default_args=default_args,
    description='DAG para ETL spotfy',
    schedule_interval=timedelta(days=1),

)

run_etl = PythonOperator(
    task_id = 'whole_spotfy_etl',
    python_callable= run_spotify_etl(get_token, db_connect),
    dag=dag,
)
run_etl

