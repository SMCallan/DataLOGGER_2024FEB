# FILENAME: config.py

settings = {
    'sensor_mapping': {
        'O2': {'type': 'analog', 'channel': 0},    # O2 sensor connected to ADC channel 0
        'CO': {'type': 'analog', 'channel': 1},    # CO sensor connected to ADC channel 1
        'NOx': {'type': 'analog', 'channel': 2},   # NOx sensor connected to ADC channel 2
        'Dust': {'type': 'analog', 'channel': 3},  # Dust sensor connected to ADC channel 3
    },

    # Placeholder for calibration parameters; adjust as needed for actual calibration
    'sensor_calibration': {
        'O2': {'offset': 0, 'slope': 1},
        'CO': {'offset': 0, 'slope': 1},
        'NOx': {'offset': 0, 'slope': 1},
        'Dust': {'offset': 0, 'slope': 1},
    },

    'data_logging_interval': 60,  # Data logging interval in seconds
    'gui_update_interval': 1000,  # GUI update interval in milliseconds
}
