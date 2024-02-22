class AlarmManager:
    def check_alarms(self, sensor_data):
        # Example: Check for over-threshold values and increasing trends
        alarms = []
        for sensor_id, data in sensor_data.items():
            if max(data) > 90:  # Threshold check
                alarms.append(f"{sensor_id} exceeded threshold")
            if len(data) > 2 and data[-1] > data[-2] > data[-3]:  # Increasing trend
                alarms.append(f"{sensor_id} showing increasing trend")
        return alarms
