# FILENAME: gui_manager.py

import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUIManager:
    def __init__(self, root, sensor_manager, data_logger, alarm_manager):
        """
        Initialize the GUI Manager with references to the sensor manager,
        data logger, and alarm manager, setting up the UI components and
        starting the auto-update process for live sensor data visualization.

        Args:
            root (tk.Tk): The root window of the application.
            sensor_manager (SensorManager): The sensor manager instance.
            data_logger (DataLogger): The data logger instance.
            alarm_manager (AlarmManager): The alarm manager instance.
        """
        self.root = root
        self.sensor_manager = sensor_manager
        self.data_logger = data_logger
        self.alarm_manager = alarm_manager

        self.setup_ui()
        self.update_interval = 1000  # Update interval in milliseconds for sensor data.

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
        """Starts the automatic update process for sensor readings and plots."""
        self.update_sensor_readings()
        self.root.after(self.update_interval, self.start_auto_update)

    def update_sensor_readings(self):
        """
        Fetches the latest sensor readings, updates the live reading labels,
        and triggers an update of the sensor data plots.
        """
        # Fetch and display the latest readings for each sensor.
        for sensor_id in ["CO", "O2", "Dust"]:
            reading = self.sensor_manager.read_sensor(sensor_id)
            self.labels[sensor_id]["text"] = f"{sensor_id} Reading: {reading}"

        # Update the plots with the latest sensor data.
        self.update_plots()

    def update_plots(self):
        """
        Updates the plots with recent sensor data. This method should be
        implemented to fetch recent data for each sensor and update the
        corresponding subplot with that data.
        """
        # Clear existing plots.
        for ax in self.axs:
            ax.clear()

        # Example plotting logic (replace with actual data fetching and plotting)
        # self.axs[0].plot(data_CO)
        # self.axs[1].plot(data_O2)
        # self.axs[2].plot(data_Dust)
        # Re-draw the canvas to reflect updated plots.
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    # Ensure these classes (SensorManager, DataLogger, AlarmManager) are properly implemented.
    sensor_manager = SensorManager()
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    app = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    root.mainloop()
