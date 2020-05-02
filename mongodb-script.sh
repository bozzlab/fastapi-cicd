#!bin/sh

#start mongodb
docker run -d --name mongodb \
-e MONGO_INITDB_ROOT_USERNAME=fastapi-admin \
-e MONGO_INITDB_ROOT_PASSWORD=fastapi-password \
-v $PWD/mongodb/data/db:/data/db \
-p 27017:27017 \
mongo


#shell into mongodb
docker exec -it mongodb mongo -u fastapi-admin -p fastapi-password --authenticationDatabase admin

#switch db 
use movies

#test insertion 
db.movies.insert({"username" : "fastapi-admin"})
