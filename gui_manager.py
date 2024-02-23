# FILENAME: gui_manager.py

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class GUIManager:
    def __init__(self, root, sensor_manager, data_logger, alarm_manager):
        self.root = root
        self.sensor_manager = sensor_manager
        self.data_logger = data_logger
        self.alarm_manager = alarm_manager
        
        # Define update_interval before setup_ui to avoid AttributeError
        self.update_interval = 1000  # milliseconds for updating sensor readings and plots
        
        # Initialize a dictionary to store recent sensor data for plotting
        self.sensor_data = {'CO': [], 'O2': [], 'Dust': []}
        
        self.setup_ui()

    def setup_ui(self):
        """Sets up the user interface components for the application."""
        self.root.title("Sensor System Dashboard")
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=0, column=0, sticky="nsew")
        
        self.reading_frame = ttk.Frame(self.root, width=200)
        self.reading_frame.grid(row=0, column=1, sticky="ns")
        
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.figure = Figure(figsize=(5, 6), dpi=100)
        self.axs = [self.figure.add_subplot(311), self.figure.add_subplot(312), self.figure.add_subplot(313)]
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.labels = {sensor_id: ttk.Label(self.reading_frame, text=f"{sensor_id} Reading: 0") for sensor_id in ["CO", "O2", "Dust"]}
        for label in self.labels.values():
            label.pack(pady=10)
        
        generate_report_btn = ttk.Button(self.reading_frame, text="Generate Report", command=self.generate_report)
        generate_report_btn.pack(pady=10)
        
        self.start_auto_update()

    def generate_report(self):
        """Generates a report of average sensor readings."""
        self.data_logger.generate_average_report()
        messagebox.showinfo("Report Generated", "The average sensor readings report has been generated.")

    def start_auto_update(self):
        """Begins the process of automatically updating sensor readings and plots."""
        self.update_sensor_readings()
        self.root.after(self.update_interval, self.start_auto_update)

    def update_sensor_readings(self):
        """Fetches the latest readings from sensors and updates the UI accordingly."""
        for sensor_id in ["CO", "O2", "Dust"]:
            reading = self.sensor_manager.read_sensor(sensor_id)
            self.sensor_data[sensor_id].append(reading)
            
            # Update the label with the latest reading
            self.labels[sensor_id]["text"] = f"{sensor_id} Reading: {reading}"
            
            # Optional: Trim the sensor data list to keep the UI responsive
            if len(self.sensor_data[sensor_id]) > 50:  # Keep the last 50 readings
                self.sensor_data[sensor_id] = self.sensor_data[sensor_id][-50:]
        
        self.update_plots()

    def update_plots(self):
        """Updates the plots with recent sensor data."""
        sensor_ranges = {'CO': (0, 1000), 'O2': (0, 25), 'Dust': (0, 100)}  # Define correct ranges for each sensor
        
        for ax, sensor_id in zip(self.axs, ["CO", "O2", "Dust"]):
            ax.clear()
            ax.plot(self.sensor_data[sensor_id], label=sensor_id)
            ax.legend(loc="upper left")
            ax.set_ylabel(f"{sensor_id}")
            ax.set_ylim(sensor_ranges[sensor_id])  # Set y-axis limits based on sensor ranges
        
        self.axs[-1].set_xlabel("Time (s)")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    # Initialize SensorManager, DataLogger, and AlarmManager with actual instances
    sensor_manager = SensorManager()
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    app = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    root.mainloop()
