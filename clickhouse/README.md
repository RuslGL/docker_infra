# GUIDE from YANDEX -works for server only
https://hub.docker.com/r/yandex/clickhouse-server

# FOR MAC
docker run -d --name some-clickhouse-server -p 8123:8123 --ulimit nofile=262144:262144 clickhouse
http://127.0.0.1:8123/

# for my compose 
docker-compose up -d

## подключение к дефолтному юзеру изнутри контейнера
docker exec -it some-clickhouse-server clickhouse-client -u default



