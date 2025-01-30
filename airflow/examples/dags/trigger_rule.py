# trigger_rule
# all_failed: Задача выполняется, если все непосредственно зависимые задачи завершились с ошибкой.
# all_done: Запускает задачу, как только все непосредственно зависимые задачи завершены, независимо от их состояния.
# one_failed: Как только одна из зависимых задач завершится с ошибкой, ваша задача запустится.
# one_success: Как и с one_failed Ваша задача запускается, как только одна из зависимых задач завершается успешно
# none_failed: Ваша задача запускается, если все непосредственно зависимые задачи завершились успешно или были пропущены.
# none_skipped: Задача запускается, если ни одна из зависимых задач не находится в состоянии skipped
# none_failed_min_one_success С этим правилом триггера ваша задача запускается, если все непосредственно зависимые задачи не завершились с ошибкой и хотя бы одна из них была успешной.

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


# Функция, которая будет вызываться в PythonOperator
def task_that_fails1():
    return 1 / 0

def task_that_fails2():
    return 1 / 0

def task_that_success():
    return True

# Создаём DAG
dag = DAG(
    'dag1',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # Запускать DAG вручную
)

# Задача, которая вызывает ошибку
task1 = PythonOperator(
    task_id='task_that_fails1',
    python_callable=task_that_fails1,
    dag=dag,
)

# Задача, которая вызывает ошибку
task2 = PythonOperator(
    task_id='task_that_fails2',
    python_callable=task_that_fails2,
    dag=dag,
)

# Задача, которая вызывает ошибку
task3 = PythonOperator(
    task_id='task_that_success',
    python_callable=task_that_success,
    # Данная задача будет ожидать определенное поведение
    # В данном примере она ждет что все дочерние задачи завершатся ошибкой
    trigger_rule='all_failed',  # one_failed DAG снова завершится успешно, наличие хотя бы одной дочерней задачи с ошибко
    dag=dag,
)

[task1, task2] >> task3