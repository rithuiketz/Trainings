from datetime import datetime
from airflow import DAG
import pandas as pd
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator

# 1. Create your DataFrame
df = pd.DataFrame(columns=['id', 'name'], data=[(1, 'rith')])

# 2. Convert the DataFrame to a CSV string format
csv_data = df.to_csv(index=False)

with DAG(
    dag_id='s3-data-creation',
    start_date=datetime(2026, 1, 1), # Best practice: Always provide a start_date
    catchup=False
) as dag:
    
    file_copy_task = S3CreateObjectOperator(
        task_id='create_s3_csv',       # Added required task_id
        data=csv_data,                 # Passed the converted string
        aws_conn_id='aws_s3',
        s3_bucket='rith-bucket-001',
        s3_key='test.csv',             # Fixed to be a relative key path
        replace=True,
    )

    # Note: dag.add_task() is redundant when using the 'with DAG' context manager.
    # Declaring the operator inside the block automatically registers it.
