
FROM python:3.8

ENV AIRFLOW_HOME=/usr/local/airflow

ARG AIRFLOW_VERSION=2.1.4


# Папка с дагами и плагинами
ENV AIRFLOW__CORE__DAGS_FOLDER=/usr/local/airflow/dags
ENV AIRFLOW__CORE__PLUGINS_FOLDER=/usr/local/airflow/plugins

# Замени executor и сменим бд на постгрес
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:tryit8734@postgres:5432/airflow

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

RUN pip install apache-airflow[postgres]==${AIRFLOW_VERSION}

RUN pip install SQLAlchemy==1.3.24

RUN pip install airflow-code-editor
RUN pip install black fs-s3fs fs-gcsfs


RUN mkdir /project
COPY scripts/ /project/scripts/
RUN chmod +x /project/scripts/init.sh

# Запускаем sh скрипт
# Начнет процесс инициализации airflow
ENTRYPOINT ["/project/scripts/init.sh"]