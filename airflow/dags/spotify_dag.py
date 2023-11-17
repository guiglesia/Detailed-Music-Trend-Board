from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from spotify_etl import run_spotify_etl, db_connect, get_token, get_auth_header

default_args = {
    'owner': 'guilherme iglesia',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 11),
    'email': ['g235977@dac.unicamp.br'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='DAG para ETL spotify',
    schedule_interval=timedelta(days=2),
    catchup=False

)
token = PythonOperator(
    task_id = "get_token",
    python_callable = get_token,
    provide_context = True,
    dag=dag
)

header = PythonOperator(
    task_id = "get_header",
    python_callable = get_auth_header,
    provide_context = True,
    dag=dag
)

connection = PythonOperator(
    task_id = "db_connect",
    python_callable = db_connect,
    provide_context = True,
    dag=dag
)

run_etl = PythonOperator(
    task_id = 'whole_spotfy_etl',
    python_callable= run_spotify_etl,
    op_args=[],
    provide_context=True,
    dag=dag,
)
connection >> token >> header >> run_etl 

