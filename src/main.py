"""AWS IoT Core connection and MQTT client."""

# This is a temporary main function to coneect the aws iot core from the board LTE PI
#
from sensors.dht_sensor import read_dht
from sensors.gps_module import read_gps
from aws.iot_client import AWSIoTClient

def main():
    aws_client = AWSIoTClient()
    aws_client.connect()

    # Leer datos de sensores
    temp, humidity = read_dht()
    gps_data = read_gps()

    # Enviar datos a AWS IoT Core
    payload = {
        "temperature": temp,
        "humidity": humidity,
        "gps": gps_data,
    }
    aws_client.publish(topic="iot/sensor_data", payload=payload)

if __name__ == "__main__":
    main()

