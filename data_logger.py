#data_logger.py
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
        try:
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                for sensor_id, reading in sensor_data.items():
                    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    self.sensor_data_with_timestamps.setdefault(sensor_id, []).append((timestamp, reading))
                    writer.writerow([timestamp, sensor_id, reading])
        except IOError as e:
            print(f"Error logging data: {e}")

    def generate_average_report(self, interval='minute'):
        averages = {}
        # Placeholder dictionary for average calculations
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
        try:
            report_filename = f"average_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            with open(report_filename, 'w') as file:
                for sensor_id, time_averages in averages.items():
                    file.write(f"Sensor ID: {sensor_id}\n")
                    for time_key, avg_reading in time_averages.items():
                        file.write(f"Average for {time_key}: {avg_reading:.2f}\n")
                    file.write("\n")
            print(f"Report generated: {report_filename}")
        except IOError as e:
            print(f"Error generating report: {e}")
