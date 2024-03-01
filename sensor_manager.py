# FILENAME: sensor_manager.py
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
from config import settings

class SensorManager:
    def __init__(self):
        # Initialize the ADS1115 ADC using the default I2C address
        self.adc = Adafruit_ADS1x15.ADS1115()
        # Set GPIO mode for any digital sensors
        GPIO.setmode(GPIO.BCM)
        # Load sensor mapping and calibration settings
        self.sensor_mapping = settings['sensor_mapping']
        self.sensor_calibration = settings['sensor_calibration']
        # ADS1115 gain setting (adjust based on the voltage range of your sensors)
        self.gain = 1

        # Setup GPIO pins for digital sensors
        for sensor_id, sensor_info in self.sensor_mapping.items():
            if sensor_info['type'] == 'digital':
                GPIO.setup(sensor_info['pin'], GPIO.IN)

    def read_sensor(self, sensor_id):
        # Ensure the sensor is configured
        if sensor_id not in self.sensor_mapping:
            raise ValueError(f"Sensor {sensor_id} not configured.")

        sensor_info = self.sensor_mapping[sensor_id]

        if sensor_info['type'] == 'analog':
            # Read raw value from the ADC
            raw_value = self.adc.read_adc(sensor_info['channel'], gain=self.gain)
            # Apply calibration if defined
            if sensor_id in self.sensor_calibration:
                calibration_info = self.sensor_calibration[sensor_id]
                calibrated_value = (raw_value - calibration_info['offset']) * calibration_info['slope']
                return calibrated_value
            else:
                return raw_value  # Return raw value if no calibration info
        elif sensor_info['type'] == 'digital':
            # Directly return the digital reading
            return GPIO.input(sensor_info['pin'])
        else:
            raise ValueError(f"Invalid sensor type for {sensor_id}.")

    def get_sensor_ids(self):
        # Return a list of all configured sensor IDs
        return list(self.sensor_mapping.keys())

    def cleanup(self):
        # Clean up GPIO resources
        GPIO.cleanup()
        
