import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS1115 instance
ads = ADS.ADS1115(i2c)

# Create an analog input channel on pin 0
chan = AnalogIn(ads, ADS.P0)

def convert_reading_to_actual(raw_value, sensor_type):
    # Example conversion for a specific sensor
    if sensor_type == "O2":
        min_sensor_value = 0
        max_sensor_value = 1000
        voltage = (raw_value * 3.3) / 32767
        actual_value = ((voltage - 0.66) * (max_sensor_value - min_sensor_value) / (3.3 - 0.66)) + min_sensor_value
        return actual_value
    return None

# Test function to read and print a single value
def test_sensor_reading():
    raw_value = chan.value
    voltage = (raw_value * 3.3) / 32767
    actual_value = convert_reading_to_actual(raw_value, "O2")
    print(f"Raw ADC value: {raw_value}")
    print(f"Converted voltage: {voltage:.2f} V")
    print(f"O2 Concentration: {actual_value:.2f} mg/m3")

# Run the test once
test_sensor_reading()

# If the test is successful, uncomment the following lines to begin continuous reading
# while True:
#     raw_value = chan.value
#     actual_value = convert_reading_to_actual(raw_value, "O2")
#     print(f"O2 Concentration: {actual_value:.2f} mg/m3")
#     time.sleep(1)
