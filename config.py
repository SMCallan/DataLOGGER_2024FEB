# FILENAME: config.py
# Configuration settings for the sensor system

settings = {
    # Mapping of sensors to ADC channels or GPIO pins
    'sensor_mapping': {
        'CO': {'type': 'analog', 'channel': 0},    # CO sensor connected to ADC channel 0
        'O2': {'type': 'analog', 'channel': 2},    # O2 sensor connected to ADC channel 2
        'NOx': {'type': 'analog', 'channel': 1},   # NOx sensor connected to ADC channel 1
        'Dust': {'type': 'analog', 'channel': 3},  # Dust sensor connected to ADC channel 3
        'Temp1': {'type': 'analog', 'channel': 4}, # Temp1 sensor (example) connected to ADC channel 4
        'Temp2': {'type': 'analog', 'channel': 5}, # Temp2 sensor (example) connected to ADC channel 5
    },

    # Calibration parameters for each sensor (offset and slope)
    'sensor_calibration': {
        'CO': {'offset': 1.16156, 'slope': 0.00067},
        'O2': {'offset': 1.16156, 'slope': 0.00067},
        'NOx': {'offset': 1.16156, 'slope': 0.00067},
        'Dust': {'offset': 1.16156, 'slope': 0.00067},
        'Temp1': {'offset': 0, 'slope': 1},  # Placeholder values, adjust as needed
        'Temp2': {'offset': 0, 'slope': 1},  # Placeholder values, adjust as needed
    },

    # Data logging interval (in seconds)
    'data_logging_interval': 60,

    # GUI update interval (in milliseconds)
    'gui_update_interval': 1000,
}
