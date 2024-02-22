# config.py
# Central configuration for the sensor system. Defines mappings for both analog and digital sensors, 
# including their types, channels for analog sensors, and pins for digital sensors.

settings = {
    'sensor_mapping': {
        # Define analog sensors with their respective ADC channels
        'sensor1': {'type': 'analog', 'channel': 0},
        'sensor2': {'type': 'analog', 'channel': 1},
        # Define digital sensors with their respective GPIO pins
        'sensor3': {'type': 'digital', 'pin': 17},
        'sensor4': {'type': 'digital', 'pin': 27},
    },
    # Data logging interval in seconds
    'data_logging_interval': 60,
    # GUI update interval in milliseconds
    'gui_update_interval': 1000,
    # Additional settings can be added here
}
