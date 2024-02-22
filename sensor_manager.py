import RPi.GPIO as GPIO
import Adafruit_ADS1x15

class SensorManager:
    def __init__(self):
        # Initialize ADC for analog sensors
        self.adc = Adafruit_ADS1x15.ADS1115()
        # Sensor channels for ADC (analog sensors)
        self.analog_sensor_channels = {'sensor1': 0, 'sensor2': 1}
        # Gain for ADC readings
        self.gain = 1
        # GPIO pins for digital sensors
        self.digital_sensor_pins = {'sensor3': 17, 'sensor4': 27}
        # Setup GPIO mode
        GPIO.setmode(GPIO.BCM)
        # Setup GPIO pins as input
        for pin in self.digital_sensor_pins.values():
            GPIO.setup(pin, GPIO.IN)

    def read_sensor(self, sensor_id):
        # Check if sensor is analog and read from ADC
        if sensor_id in self.analog_sensor_channels:
            channel = self.analog_sensor_channels[sensor_id]
            sensor_value = self.adc.read_adc(channel, gain=self.gain)
            return sensor_value
        # Otherwise, read from GPIO (digital sensor)
        elif sensor_id in self.digital_sensor_pins:
            pin = self.digital_sensor_pins[sensor_id]
            sensor_value = GPIO.input(pin)
            return sensor_value
        else:
            raise ValueError("Sensor ID not recognized.")
