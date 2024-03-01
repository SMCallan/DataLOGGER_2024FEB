# FILENAME: config.py

settings = {
    'sensor_mapping': {
        'O2': {'type': 'analog', 'channel': 0},    # O2 sensor connected to ADC channel 0
        'CO': {'type': 'analog', 'channel': 1},    # CO sensor connected to ADC channel 1
        'NOx': {'type': 'analog', 'channel': 2},   # NOx sensor connected to ADC channel 2
        'Dust': {'type': 'analog', 'channel': 3},  # Dust sensor connected to ADC channel 3
    },

    'sensor_calibration': {
        # Example calibration parameters for 4-20mA sensors, assuming linear relationship
        'O2': {
            'min_mA': 4, 'max_mA': 20,
            'min_measurement': 0, 'max_measurement': 25  # Assuming O2 is measured from 0% to 25%
        },
        'CO': {
            'min_mA': 4, 'max_mA': 20,
            'min_measurement': 0, 'max_measurement': 1000  # Assuming CO is measured from 0 to 1000 ppm
        },
        'NOx': {
            'min_mA': 4, 'max_mA': 20,
            'min_measurement': 0, 'max_measurement': 500  # Assuming NOx is measured from 0 to 500 ppm
        },
        'Dust': {
            'min_mA': 4, 'max_mA': 20,
            'min_measurement': 0, 'max_measurement': 100  # Assuming Dust is measured from 0 to 100 mg/m3
        },
    },

    'data_logging_interval': 60,  # Data logging interval in seconds
    'gui_update_interval': 1000,  # GUI update interval in milliseconds
}
