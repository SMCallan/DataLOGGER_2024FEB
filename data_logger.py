import csv
from datetime import datetime

class DataLogger:
    def log_data(self, sensor_data):
        # Example: log data to a CSV file
        filename = datetime.now().strftime("%Y-%m-%d") + ".csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            # Assuming you want to log the timestamp, sensor IDs, and their readings
            row = [datetime.now().strftime("%H:%M:%S")] + [sensor_id for sensor_id in sensor_data] + [sensor_data[sensor_id] for sensor_id in sensor_data]
            writer.writerow(row)
