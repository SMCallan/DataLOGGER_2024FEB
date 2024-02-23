# FILENAME: sensor_manager.py

import RPi.GPIO as GPIO
import Adafruit_ADS1x15
from config import settings

class SensorManager:
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        GPIO.setmode(GPIO.BCM)
        self.sensor_mapping = settings['sensor_mapping']
        self.gain = 1

        for sensor_id, sensor_info in self.sensor_mapping.items():
            if sensor_info['type'] == 'digital':
                GPIO.setup(sensor_info['pin'], GPIO.IN)

    def read_sensor(self, sensor_id):
        if sensor_id not in self.sensor_mapping:
            raise ValueError(f"Sensor {sensor_id} not configured.")
        sensor_info = self.sensor_mapping[sensor_id]
        if sensor_info['type'] == 'analog':
            return self.adc.read_adc(sensor_info['channel'], gain=self.gain)
        elif sensor_info['type'] == 'digital':
            return GPIO.input(sensor_info['pin'])
        else:
            raise ValueError(f"Invalid sensor type for {sensor_id}.")

    def get_sensor_ids(self):
        return list(self.sensor_mapping.keys())

    def cleanup(self):
        GPIO.cleanup()
