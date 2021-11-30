#!/usr/bin/env bash

base_dir=$(pwd)

echo "Building rest server..."
cd rest-server && make 
cd $base_dir

echo "Building grrc server..."
cd grpc_server/fibServer && make
cd ../logServer && make
