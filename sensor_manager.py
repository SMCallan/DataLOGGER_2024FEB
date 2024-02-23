# FILENAME: sensor_manager.py

import RPi.GPIO as GPIO
import Adafruit_ADS1x15
from config import settings  # Ensure this imports your specific settings structure

class SensorManager:
    def __init__(self):
        """
        Initializes the SensorManager with an ADS1115 instance for analog readings
        and GPIO setup for digital sensor pins.
        """
        # Initialize the ADC (Analog-to-Digital Converter) for reading analog sensors
        self.adc = Adafruit_ADS1x15.ADS1115()
        
        # Set up GPIO to BCM mode for consistent pin numbering
        GPIO.setmode(GPIO.BCM)
        
        # Retrieve sensor configurations from settings
        self.sensor_mapping = settings['sensor_mapping']
        
        # Default gain for ADS1115 readings
        self.gain = 1

        # Initialize digital sensors as inputs
        for sensor_id, sensor_info in self.sensor_mapping.items():
            if sensor_info['type'] == 'digital':
                GPIO.setup(sensor_info['pin'], GPIO.IN)

    def read_sensor(self, sensor_id):
        """
        Reads and returns the current value from the specified sensor.

        Args:
            sensor_id (str): The ID of the sensor to read.

        Returns:
            int or float: The current reading of the sensor.

        Raises:
            ValueError: If an invalid sensor type is encountered.
        """
        # Validate sensor_id exists in our mapping
        if sensor_id not in self.sensor_mapping:
            raise ValueError(f"Sensor {sensor_id} not configured.")

        sensor_info = self.sensor_mapping[sensor_id]

        # Read and return analog sensor value
        if sensor_info['type'] == 'analog':
            return self.adc.read_adc(sensor_info['channel'], gain=self.gain)
        # Read and return digital sensor value
        elif sensor_info['type'] == 'digital':
            return GPIO.input(sensor_info['pin'])
        else:
            raise ValueError(f"Invalid sensor type for {sensor_id}.")

    # Consider adding a cleanup method for GPIO cleanup on application exit
    def cleanup(self):
        """
        Cleans up by resetting GPIO pins used by the application. This should be called
        before the application exits to ensure the GPIO pins are left in a safe state.
        """
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    sensor_manager = SensorManager()
    try:
        for sensor_id in sensor_manager.sensor_mapping.keys():
            print(f"{sensor_id} reading: {sensor_manager.read_sensor(sensor_id)}")
    finally:
        sensor_manager.cleanup()

