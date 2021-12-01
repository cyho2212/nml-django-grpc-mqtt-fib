```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install grpc packages
$ pip3 install -r requirements.txt
```

## Compile protobuf schema to python wrapper

```bash
chmod +x ./build.sh
./build
```

## Run the eclipse mosquitto docker container

```bash
sudo docker run -d -it -p 1883:1883 -v $(pwd)/grpc_server/logServer/mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
```
## Update config.conf to match docker port and ip addresses

## Run gRPC server and REST logServer

```bash
chmod +x ./run.sh
./run
```



## Commands to run

**Send to server**

`curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/rest/fibonacci -d "{\"order\":\"{NUMBER}\"}"`



**To Get History**

`curl 127.0.0.1:8000/rest/logs`

## Media reference
I attached snapshots from build to post-get requests instead of video because I faced some issues recording my own screen. Worked procedures are named as filenames, for 4 snapshots in the folder demo-snapshot.
