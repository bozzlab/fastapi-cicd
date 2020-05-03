#!bin/sh

docker pull postgres:11
docker run -d --name postgres_db -e POSTGRES_PASSWORD=password -p 54320:5432 postgres:11
dockerexec -it postgres_db psql -U postgres

