#!bin/sh

docker pull postgres:11
docker run -d --name postgres_db -v $PWD/postgres/data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=password -p 54320:5432 postgres:11
docker exec -it postgres_db psql -U postgres

