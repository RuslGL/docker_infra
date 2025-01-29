#!/bin/bash

# Создание БД
airflow db init
sleep 15

airflow users create \
          --username ruslan_gl \
          --firstname airflow \
          --lastname airflow \
          --role Admin \
          --email admin@example.org \
          -p qwerty12345

# Запуск шедулера и вебсервера
airflow scheduler & airflow webserver