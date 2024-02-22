import tkinter as tk
from gui_manager import GUIManager
from sensor_manager import SensorManager
from data_logger import DataLogger
from alarm_manager import AlarmManager
import threading
import time

def automatic_data_logging(sensor_manager, data_logger):
    while True:
        sensor_data = {sensor_id: sensor_manager.read_sensor(sensor_id) for sensor_id in sensor_manager.sensors}
        data_logger.log_data(sensor_data)
        time.sleep(60)  # Log data every 60 seconds

def main():
    root = tk.Tk()
    sensor_manager = SensorManager()
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    gui_manager = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    
    data_logging_thread = threading.Thread(target=automatic_data_logging, args=(sensor_manager, data_logger))
    data_logging_thread.daemon = True
    data_logging_thread.start()
    
    root.mainloop()

if __name__ == "__main__":
    main()
