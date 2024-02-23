import tkinter as tk
from tkinter import Frame, TOP, LEFT, X, BOTH, SUNKEN, BOTTOM
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os

# Importing your SensorManager, DataLogger, and AlarmManager
# This assumes these classes are defined in their respective modules.
from sensor_manager import SensorManager
from data_logger import DataLogger
from alarm_manager import AlarmManager

class GUIManager:
    def __init__(self, root, sensor_manager, data_logger, alarm_manager):
        self.root = root
        self.sensor_manager = sensor_manager
        self.data_logger = data_logger
        self.alarm_manager = alarm_manager

        self.setup_ui()

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.sensor_data = {sensor_id: [] for sensor_id in self.sensor_manager.get_sensor_ids()}
        self.update_interval = 1000  # milliseconds

        self.start_auto_update()

    def setup_ui(self):
        self.root.title("Sensor System Dashboard")

        self.top_frame = Frame(self.root, bd=2, relief=SUNKEN)
        self.top_frame.pack(side=TOP, fill=X)

        self.graph_frame = Frame(self.root, bd=2, relief=SUNKEN)
        self.graph_frame.pack(expand=True, side=LEFT, fill=BOTH)

        self.status_frame = Frame(self.root, bd=2, relief=SUNKEN)
        self.status_frame.pack(expand=True, side=LEFT, fill=BOTH)

        self.alarm_frame = Frame(self.root, bd=2, relief=SUNKEN)
        self.alarm_frame.pack(expand=True, side=BOTTOM, fill=BOTH)

        # Add any additional UI setup here

    def start_auto_update(self):
        self.update_sensor_readings()
        self.root.after(self.update_interval, self.start_auto_update)

    def update_sensor_readings(self):
        for sensor_id in self.sensor_manager.get_sensor_ids():
            data = self.sensor_manager.read_sensor(sensor_id)
            self.sensor_data[sensor_id].append(data)

        self.plot.clear()
        self.plot.set_xlabel("Time")
        self.plot.set_ylabel("Sensor Value")
        self.plot.set_title("Real-time Sensor Data Visualization")

        for sensor_id, data in self.sensor_data.items():
            if data:  # Check if data list is not empty
                self.plot.plot(data, label=sensor_id)

        self.plot.legend()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIManager(root)
    root.mainloop()
