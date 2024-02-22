import RPi.GPIO as GPIO
import Adafruit_ADS1x15

class SensorManager:
    def __init__(self):
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.analog_sensor_channels = {'sensor1': 0, 'sensor2': 1}
        self.gain = 1
        self.digital_sensor_pins = {'sensor3': 17, 'sensor4': 27}
        GPIO.setmode(GPIO.BCM)
        for pin in self.digital_sensor_pins.values():
            GPIO.setup(pin, GPIO.IN)

    def read_sensor(self, sensor_id):
        if sensor_id in self.analog_sensor_channels:
            channel = self.analog_sensor_channels[sensor_id]
            return self.adc.read_adc(channel, gain=self.gain)
        elif sensor_id in self.digital_sensor_pins:
            return GPIO.input(self.digital_sensor_pins[sensor_id])
        else:
            raise ValueError("Sensor ID not recognized.")
    
    def get_sensor_ids(self):
        return list(self.analog_sensor_channels.keys()) + list(self.digital_sensor_pins.keys())
