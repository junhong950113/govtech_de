"""
Setting up airflow dag
"""

from task1 import main #our main task
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    'task1',
    start_date=datetime(2021,11,6),
    schedule_interval='15 1 * * *' #daily at 0115 as new file comes in at 0100
)

main_task = PythonOperator(
    task_id="main task",
    python_callable=main,
    dag=dag
)