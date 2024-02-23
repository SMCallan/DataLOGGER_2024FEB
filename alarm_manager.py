# FILENAME: alarm_manager.py
class AlarmManager:
    def check_alarms(self, sensor_data):
        alarms = []
        for sensor_id, data in sensor_data.items():
            if sensor_id == 'CO' and max(data) > 900:  # Example threshold for CO
                alarms.append(f"{sensor_id} exceeded threshold")
            elif sensor_id == 'O2' and (max(data) > 23 or min(data) < 19):  # Example thresholds for O2
                alarms.append(f"{sensor_id} outside safe range")
            elif sensor_id == 'Dust' and max(data) > 80:  # Example threshold for Dust
                alarms.append(f"{sensor_id} exceeded threshold")
            if len(data) > 2 and data[-1] > data[-2] > data[-3]:  # Increasing trend
                alarms.append(f"{sensor_id} showing increasing trend")
        return alarms
