import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUIManager:
    def __init__(self, root, sensor_manager, data_logger, alarm_manager):
        self.root = root
        self.sensor_manager = sensor_manager
        self.data_logger = data_logger
        self.alarm_manager = alarm_manager
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.sensor_data = {sensor_id: [] for sensor_id in sensor_manager.get_sensor_ids()}
        self.setup_ui()
        self.auto_update_interval = 1000  # Interval in milliseconds

    def start_auto_update(self):
        self.update_sensor_readings()  # Update the sensor readings
        # Schedule the next call to this method after the specified interval
        self.root.after(self.auto_update_interval, self.start_auto_update)
    
    def setup_ui(self):
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.update_button = tk.Button(self.root, text="Read Sensors", command=self.update_sensor_readings)
        self.update_button.pack(side=tk.BOTTOM)
        self.start_auto_update()  # Start automatic updates

    def update_sensor_readings(self):
        for sensor_id in self.sensor_manager.get_sensor_ids():
            data = self.sensor_manager.read_sensor(sensor_id)
            self.sensor_data[sensor_id].append(data)
        
        self.plot.clear()
        for sensor_id, data in self.sensor_data.items():
            self.plot.plot(data, label=sensor_id)
        
        self.plot.legend()
        self.canvas.draw()
