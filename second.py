from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

# Define the Python function
def practice():
    a = 6
    b = 9
    a = a + b
    b = a - b
    a = a - b
    print(a)
    print(b)

# Default arguments for the DAG
default_args = {
    'owner': 'Akin',
    'email_on_failure': False,
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='practice',
    default_args=default_args,
    description='Practicing DAGs',
    start_date=datetime(2024, 12, 15),  # Correct datetime format
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Define the PythonOperator task
    type_task = PythonOperator(
        task_id='practicing_airflow',  # Use snake_case for task_id
        python_callable=practice,
    )
