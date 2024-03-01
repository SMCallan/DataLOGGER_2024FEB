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
        
        # Set the update interval for sensor readings and plots (in milliseconds)
        self.update_interval = 1000
        
        # Initialize a dictionary to store recent sensor data for plotting
        # Note: Adjust this dictionary if you add more sensors or change the existing ones
        self.sensor_data = {'CO': [], 'O2': [], 'Dust': [], 'NOx': []}
        
        self.setup_ui()

    def setup_ui(self):
        """Sets up the user interface components for the application."""
        self.root.title("Sensor System Dashboard")
        
        # Plot frame setup
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=0, column=0, sticky="nsew")
        
        # Reading frame setup
        self.reading_frame = ttk.Frame(self.root, width=200)
        self.reading_frame.grid(row=0, column=1, sticky="ns")
        
        # Configure grid
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Figure for plotting sensor data
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.axs = self.figure.subplots(4, 1)  # Create 4 subplots for 4 sensors
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Sensor reading labels
        self.labels = {sensor_id: ttk.Label(self.reading_frame, text=f"{sensor_id} Reading: 0") for sensor_id in self.sensor_data}
        for label in self.labels.values():
            label.pack(pady=10)
        
        # Report generation button
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
        for sensor_id in self.sensor_data:
            reading = self.sensor_manager.read_sensor(sensor_id)  # Assume this returns the raw data for now
            self.sensor_data[sensor_id].append(reading)
            
            # Update the label with the latest reading
            self.labels[sensor_id]["text"] = f"{sensor_id} Reading: {reading}"
            
            # Keep the last 50 readings to maintain UI responsiveness
            if len(self.sensor_data[sensor_id]) > 50:
                self.sensor_data[sensor_id] = self.sensor_data[sensor_id][-50:]
        
        self.update_plots()

    def update_plots(self):
        """Updates the plots with recent sensor data."""
        for ax, (sensor_id, data) in zip(self.axs, self.sensor_data.items()):
            ax.clear()
            ax.plot(data, label=sensor_id)
            ax.legend(loc="upper left")
            ax.set_ylabel(sensor_id)
        
        self.axs[-1].set_xlabel("Time (s)")
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    # Dummy classes for SensorManager, DataLogger, and AlarmManager
    # Replace these with actual instances of your classes
    sensor_manager = SensorManager()
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    app = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    root.mainloop()
