"""Adafruit library for DHT sensors."""


#TODO: Update this file for a non Adafruit dependency (change for more generic sensor and lib)

import Adafruit_DHT


def read_dht():
    sensor = Adafruit_DHT.DHT22
    pin = 4  # Pin GPIO donde está conectado el sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return temperature, humidity

