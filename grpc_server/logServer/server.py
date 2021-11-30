import os
import os.path as osp
from pathlib import Path
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

#grpc
import grpc
from concurrent import futures
import log_pb2
import log_pb2_grpc

#mqtt
import time
import argparse

import paho.mqtt.client as mqtt
import threading

history = []

BASE_DIR = Path(__file__).resolve().parent.parent

class LogServicer(log_pb2_grpc.LogServiceServicer):

    def __init__(self):
        pass

    def Get(self, request, context):
        response = log_pb2.LogResponse()
        for h in history: response.history.append(h)
        return response

class MqttSubscriber():
    def __init__(self):
        f = open(os.path.join(BASE_DIR.parent, 'config.conf'))
        if f.mode == 'r':
            lines = f.read().splitlines()
            for line in lines:
                type = line.split("=")[0]
                if type == "DOCKER_IP":
                    self.DOCKER_IP=line.split("=")[1]
                elif type == "DOCKER_PORT":
                    self.DOCKER_PORT=line.split("=")[1]

        self.client = mqtt.Client()
        print("Conncet to mqtt broker")
        self.client.on_message = self.on_message
        # Establish connection to mqtt broker
        self.client.connect(host=self.DOCKER_IP, port=int(self.DOCKER_PORT))
        self.client.subscribe('history',0)

    def on_message(self, client, obj, msg):
        history.append(int(msg.payload))

    def main(self):
        try:
            self.client.loop_forever()
        except KeyboardInterrupt as e:
            self.client.loop_stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8081, type=int)

    args = vars(parser.parse_args())
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = LogServicer()
    log_pb2_grpc.add_LogServiceServicer_to_server(servicer, server)

    try:
        server.add_insecure_port(f"127.0.0.1:{args['port']}")

        print(f"Run gRPC Logging Server at 127.0.0.1:{args['port']}")
        mqtt = MqttSubscriber()
        x = threading.Thread(target=mqtt.main)
        x.start()

        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass
