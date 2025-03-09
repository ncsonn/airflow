from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

DAG_NAME = "first_dags"

run_date = """{{ execution_date.strftime("%Y-%m-%d") }}"""

def example_python_callable(**kwargs):
    print(kwargs)


default_args={
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "depends_on_past": False,
    "catchup": False,
    "tags": ["example"],
}

with DAG(
    dag_id=DAG_NAME,
    default_args=default_args,
    schedule="0 0 * * *", # Run every day at midnight
    start_date=datetime(2025, 1, 1),
    max_active_runs=1,
    concurrency=1,
    catchup=False
) as dag :
    
    t1 = BashOperator(
        task_id="run_time",
        bash_command="date",
    )

    t2 = PythonOperator(
        task_id="print_context",
        python_callable=example_python_callable,
        op_kwargs={"run_date": run_date},
    )

    t1 >> t2