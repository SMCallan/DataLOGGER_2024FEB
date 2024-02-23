# FILENAME: gui_manager.py
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUIManager:
    def __init__(self, root, sensor_manager, data_logger, alarm_manager):
        self.root = root
        self.sensor_manager = sensor_manager
        self.data_logger = data_logger
        self.alarm_manager = alarm_manager
        
        # Initialize a dictionary to store sensor data for plotting.
        # This will hold the latest sensor readings.
        self.sensor_data = {'CO': [], 'O2': [], 'Dust': []}
        
        self.setup_ui()
        self.update_interval = 1000  # milliseconds for updating sensor readings and plots

    def setup_ui(self):
        """Sets up the user interface components for the application."""
        self.root.title("Sensor System Dashboard")
        # Create frames for the plots and live readings.
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=0, column=0, sticky="nsew")
        
        self.reading_frame = ttk.Frame(self.root, width=200)
        self.reading_frame.grid(row=0, column=1, sticky="ns")

        # Configure the root window's grid layout.
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Initialize Matplotlib figures and subplots for each sensor.
        self.figure = Figure(figsize=(5, 6), dpi=100)
        self.axs = [self.figure.add_subplot(311), self.figure.add_subplot(312), self.figure.add_subplot(313)]
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Initialize labels for displaying live sensor readings.
        self.labels = {sensor_id: ttk.Label(self.reading_frame, text=f"{sensor_id} Reading: 0") for sensor_id in ["CO", "O2", "Dust"]}
        for label in self.labels.values():
            label.pack(pady=10)

        self.start_auto_update()

    def start_auto_update(self):
        """Begins the process of automatically updating sensor readings and plots."""
        self.update_sensor_readings()
        self.root.after(self.update_interval, self.start_auto_update)

    def update_sensor_readings(self):
                """
        Fetches the latest sensor readings, updates the live reading labels,
        and appends the new readings to self.sensor_data for plotting.
        """
        window_size = 50  # Keep the last 50 readings for plotting
        for sensor_id in ['CO', 'O2', 'Dust']:
            reading = self.sensor_manager.read_sensor(sensor_id)  # Fetch new reading
            self.sensor_data[sensor_id].append(reading)  # Append new reading
            # Remove the oldest reading if exceeding window size
            if len(self.sensor_data[sensor_id]) > window_size:
                self.sensor_data[sensor_id].pop(0)
            # Update live reading label
            self.labels[sensor_id]["text"] = f"{sensor_id} Reading: {reading}"

        # After updating sensor_data, refresh plots with the new data
        self.update_plots()

    def update_plots(self):
                """
        Updates the plots with recent sensor data, assuming self.sensor_data
        contains the latest N readings for each sensor.
        """
        sensor_ids = ['CO', 'O2', 'Dust']
        for ax, sensor_id in zip(self.axs, sensor_ids):
            ax.clear()  # Clear existing plot
            ax.plot(self.sensor_data[sensor_id], label=sensor_id)  # Plot new data
            ax.legend(loc="upper left")
            ax.set_ylabel(f"{sensor_id}")
            # Optionally, set ax.set_ylim([min_value, max_value]) based on sensor's expected range

        self.axs[-1].set_xlabel("Time (s)")
        self.canvas.draw()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    sensor_manager = SensorManager()  # Ensure this class has necessary implementations
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    app = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    root.mainloop()
