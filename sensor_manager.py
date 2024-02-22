import RPi.GPIO as GPIO
import Adafruit_ADS1x15
from config import settings  # Import settings from config.py

class SensorManager:
    def __init__(self):
        # Initialize the ADC device for reading analog sensors
        self.adc = Adafruit_ADS1x15.ADS1115()
        # Load sensor configurations from settings
        self.sensor_mapping = settings['sensor_mapping']
        self.gain = 1  # Gain for ADC readings
        
        # Setup GPIO mode for digital sensor pins
        GPIO.setmode(GPIO.BCM)
        # Initialize each digital sensor pin as input
        for sensor_id, sensor_info in self.sensor_mapping.items():
            if sensor_info['type'] == 'digital':
                pin = sensor_info['pin']
                GPIO.setup(pin, GPIO.IN)  # Using 'pin' here makes it clear

    def read_sensor(self, sensor_id):
        # Retrieve sensor configuration
        sensor_info = self.sensor_mapping[sensor_id]
        # Read and return data from the specified sensor
        if sensor_info['type'] == 'analog':
            return self.adc.read_adc(sensor_info['channel'], gain=self.gain)
        elif sensor_info['type'] == 'digital':
            return GPIO.input(sensor_info['pin'])
        else:
            raise ValueError("Invalid sensor type")

    def get_sensor_ids(self):
        # Return a list of all configured sensor IDs
        return list(self.sensor_mapping.keys())
