import sys
from datetime import datetime

# Add your project path
sys.path.append('/home/nirali/crypto_data_pipeline_v2')

from airflow import DAG
from airflow.operators.python import PythonOperator

from extract import extract_data
from transform import transform_data
from load import load_data

default_args = {
    'owner': 'nirali',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='crypto_pipeline_v2',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    extract_task >> transform_task >> load_task