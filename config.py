# FILENAME: config.py
settings = {
    'sensor_mapping': {
        'CO': {'type': 'analog', 'channel': 0},    # CO sensor measuring 0-1000ppm
        'O2': {'type': 'analog', 'channel': 1},    # O2 sensor measuring 0-25%
        'Dust': {'type': 'digital', 'pin': 17},    # Dust sensor measuring 0-100mg/m3
    },
        # Data logging interval in seconds
    'data_logging_interval': 60,
        # GUI update interval in milliseconds
    'gui_update_interval': 1000,
}
