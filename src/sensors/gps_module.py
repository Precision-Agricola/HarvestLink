import serial

#TODO: Update this file for a differnt GPS module (change for more generic GPS)

def read_gps():
    port = "/dev/ttyS0"  # Puerto serial del GPS
    with serial.Serial(port, baudrate=9600, timeout=1) as ser:
        data = ser.readline().decode("utf-8").strip()
        # Aquí puedes usar una librería como pynmea2 para procesar la data
        return data

