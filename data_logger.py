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

import csv
from datetime import datetime

class DataLogger:
    def __init__(self):
        # Initialize a dictionary to store sensor data with timestamps
        self.sensor_data_with_timestamps = {}

    def log_data(self, sensor_data):
        # Log data with timestamps for each sensor reading
        current_time = datetime.now()
        filename = current_time.strftime("%Y-%m-%d") + ".csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            for sensor_id, reading in sensor_data.items():
                timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
                # Store the data with timestamp
                if sensor_id not in self.sensor_data_with_timestamps:
                    self.sensor_data_with_timestamps[sensor_id] = []
                self.sensor_data_with_timestamps[sensor_id].append((timestamp, reading))
                # Log the data
                writer.writerow([timestamp, sensor_id, reading])
                
    def generate_average_report(self, interval='minute'):
        # Placeholder dictionary for average calculations
        averages = {}
        for sensor_id, readings in self.sensor_data_with_timestamps.items():
            # Initialize averages dictionary for this sensor
            averages[sensor_id] = {}
            for timestamp, reading in readings:
                # Extract the part of the timestamp that corresponds to the chosen interval
                if interval == 'minute':
                    time_key = timestamp[:16]  # YYYY-MM-DD HH:MM
                elif interval == 'day':
                    time_key = timestamp[:10]  # YYYY-MM-DD
                else:
                    raise ValueError("Unsupported interval. Choose 'minute' or 'day'.")
                
                if time_key not in averages[sensor_id]:
                    averages[sensor_id][time_key] = []
                averages[sensor_id][time_key].append(reading)
            
            # Calculate average for each interval
            for time_key in averages[sensor_id]:
                avg_reading = sum(averages[sensor_id][time_key]) / len(averages[sensor_id][time_key])
                averages[sensor_id][time_key] = avg_reading
        
        # Generate report from averages
        report_filename = f"average_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(report_filename, 'w') as file:
            for sensor_id, time_averages in averages.items():
                file.write(f"Sensor ID: {sensor_id}\n")
                for time_key, avg_reading in time_averages.items():
                    file.write(f"Average for {time_key}: {avg_reading:.2f}\n")
                file.write("\n")
        print(f"Report generated: {report_filename}")

# Example usage:
# data_logger = DataLogger()
# ... log some data ...
# data_logger.generate_average_report(interval='minute')  # Or 'day' for daily averages
