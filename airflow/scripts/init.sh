#!/bin/bash

# Создание БД
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:tryit8734@postgres:5432/airflow
airflow db init
sleep 15

airflow users create \
          --username airflow \
          --firstname airflow \
          --lastname airflow \
          --role Admin \
          --email admin@example.org \
          -p tryit8734

# Запуск шедулера и вебсервера
airflow scheduler & airflow webserver