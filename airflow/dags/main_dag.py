import os
import yaml

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta, datetime
from extract import extract
from generate_csv import generate_csv
from hive_query import hive_query
from validate_and_clean_data import validate_and_clean_data
bash_script_path = '/home/nineleaps/airflow/plugins/move_data_to_sql'


"""covid dag configuration arguments."""
default_args = {
    'owner': "Madhur",
    'start_date': datetime(2020, 6, 28),
    'concurrency': 1,
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(seconds=5),

}

with DAG('covid_stats', default_args=default_args,
         schedule_interval='* * * * *')as dag:

    task1 = PythonOperator(task_id='extract',
                           python_callable=extract,                      
                           provide_context=True)

    #task2 = PythonOperator(task_id='validate_and_clean_data',
    #                       python_callable=validate_and_clean_data,
    #                       provide_context=True)

    task3 = PythonOperator(task_id='generate_csv',
                           python_callable=generate_csv,
                           provide_context=True)

    task4 = PythonOperator(task_id='generate_tables',
                           python_callable=hive_query,
                         )

    task5 = BashOperator(task_id='move_data_to_sql',
                         bash_command='/bin/bash '+bash_script_path
                         )


    task1 >> task3 >> task4 >> task5
