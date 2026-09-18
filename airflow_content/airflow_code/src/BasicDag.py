from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='sample_traditional_dag',
    schedule='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:
    task_start = BashOperator(task_id='print_date', bash_command='date')
    task_process = PythonOperator(task_id='process_data', python_callable=lambda: print("Processing!"))
    task_start >> task_process
