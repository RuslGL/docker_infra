Разворачивание:

docker-compose build --no-cache
docker-compose up -d

see log/par in docker compose (environment) and in scripts/init.sh
http://localhost:8001/home


https://github.com/puckel/docker-airflow/tree/master

Если падает смотрим логи
docker logs airflow-airflow-1 --tail 50
Далее пересобираем
docker-compose down
docker-compose up -d


Теперь попробуем подключиться к PostgreSQL изнутри контейнера:

bash
Copy
Edit
docker exec -it airflow-postgres-1 psql -U airflow -d airflow
Если видим psql (12.0) — значит, подключение успешно.
Если ошибка password authentication failed, попробуем вручную сменить пароль:

sql
Copy
Edit
ALTER USER airflow WITH PASSWORD 'tryit8734';
Затем перезапускаем Airflow:

bash
Copy
Edit
docker restart airflow-airflow-1