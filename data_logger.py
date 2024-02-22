import csv
from datetime import datetime

class DataLogger:
    def log_data(self, sensor_data):
        # Example: log data to a CSV file
        filename = datetime.now().strftime("%Y-%m-%d") + ".csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%H:%M:%S")] + sensor_data)
