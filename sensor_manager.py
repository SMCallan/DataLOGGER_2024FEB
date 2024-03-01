# FILENAME: sensor_manager.py
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
from config import settings

class SensorManager:
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        GPIO.setmode(GPIO.BCM)
        self.sensor_mapping = settings['sensor_mapping']
        self.sensor_calibration = settings['sensor_calibration']
        self.gain = 1  # Set gain for ADS1115 to match expected voltage range

    def read_sensor(self, sensor_id):
        if sensor_id not in self.sensor_mapping:
            raise ValueError(f"Sensor {sensor_id} not configured.")

        sensor_info = self.sensor_mapping[sensor_id]
        if sensor_info['type'] == 'analog':
            raw_value = self.adc.read_adc(sensor_info['channel'], gain=self.gain)
            # Convert raw ADC value to voltage (assuming GAIN=1 for ±4.096V range)
            voltage = (raw_value * 4.096) / 32767.0
            # Convert voltage to current (mA) using the known resistor value (165 ohms)
            current_mA = voltage / 165.0 * 1000  # Convert to mA

            if sensor_id in self.sensor_calibration:
                cal_info = self.sensor_calibration[sensor_id]
                # Map the current (mA) to the sensor's measurement range
                measurement = ((current_mA - cal_info['min_mA']) / (cal_info['max_mA'] - cal_info['min_mA'])) * (cal_info['max_measurement'] - cal_info['min_measurement']) + cal_info['min_measurement']
                return measurement
            else:
                return None  # No calibration info available
        elif sensor_info['type'] == 'digital':
            return GPIO.input(sensor_info['pin'])  # Direct digital reading
        else:
            raise ValueError(f"Invalid sensor type for {sensor_id}.")

    def get_sensor_ids(self):
        return list(self.sensor_mapping.keys())

    def cleanup(self):
        GPIO.cleanup()

        
