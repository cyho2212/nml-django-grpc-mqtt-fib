#!/usr/bin/env bash

cur=$(pwd)

echo "Starting fibonacci gPRC server on 127.0.0.1:8080 ..."
cd grpc_server/fibServer && python3 server.py --ip 0.0.0.0 --port 8080 &

echo "Starting logging gPRC server on 127.0.0.1:8081 ..."
cd $cur/grpc_server/logServer && python3 server.py  --port 8081 &

cd $cur/rest-server
 
echo "Create migrations..."
python3 manage.py migrate

echo "Starting REST server on 127.0.0.1:8000 ..."
python3 manage.py runserver 0.0.0.0:8000 
