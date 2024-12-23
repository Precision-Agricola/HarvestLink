#TODO: change the iot core aws  credentialas after console aws confiuration
import boto3
import json
import os

class AWSIoTClient:
    def __init__(self):
        self.client = boto3.client(
            'iot-data',
            region_name=os.getenv("AWS_REGION")
        )

    def connect(self):
        print("Connected to AWS IoT Core.")

    def publish(self, topic, payload):
        self.client.publish(
            topic=topic,
            qos=1,
            payload=json.dumps(payload)
        )
        print(f"Published to {topic}: {payload}")

