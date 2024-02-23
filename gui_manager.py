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

        self.setup_ui()

        self.update_interval = 1000  # milliseconds
        self.start_auto_update()

    def setup_ui(self):
        self.root.title("Sensor System Dashboard")

        # Create frames for plots and live readings
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.grid(row=0, column=0, sticky="nsew")

        self.reading_frame = ttk.Frame(self.root, width=200)
        self.reading_frame.grid(row=0, column=1, sticky="ns")

        # Configure the grid layout
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Initialize matplotlib figures and canvases for subplots
        self.figure = Figure(figsize=(5, 6), dpi=100)
        self.ax_co = self.figure.add_subplot(311)
        self.ax_o2 = self.figure.add_subplot(312)
        self.ax_dust = self.figure.add_subplot(313)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Labels for live readings
        self.labels = {}
        for i, sensor_id in enumerate(["CO", "O2", "Dust"]):
            self.labels[sensor_id] = ttk.Label(self.reading_frame, text=f"{sensor_id} Reading: 0")
            self.labels[sensor_id].pack(pady=10)

    def start_auto_update(self):
        self.update_sensor_readings()
        self.root.after(self.update_interval, self.start_auto_update)

    def update_sensor_readings(self):
        # Mock sensor data update
        sensor_data = self.sensor_manager.get_mock_sensor_data()  # Implement this method to fetch real sensor data

        # Update plot data and live readings
        self.ax_co.clear()
        self.ax_o2.clear()
        self.ax_dust.clear()

        # Assuming sensor_data is a dictionary like {'CO': [values], 'O2': [values], 'Dust': [values]}
        self.ax_co.plot(sensor_data["CO"], label="CO")
        self.ax_o2.plot(sensor_data["O2"], label="O2")
        self.ax_dust.plot(sensor_data["Dust"], label="Dust")

        self.ax_co.set_ylabel("CO (ppm)")
        self.ax_o2.set_ylabel("O2 (%)")
        self.ax_dust.set_ylabel("Dust (mg/m3)")
        self.ax_dust.set_xlabel("Time")

        # Update live readings
        for sensor_id in ["CO", "O2", "Dust"]:
            self.labels[sensor_id].config(text=f"{sensor_id} Reading: {sensor_data[sensor_id][-1]}")

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    sensor_manager = SensorManager()  # Ensure this class has the necessary implementation
    data_logger = DataLogger()
    alarm_manager = AlarmManager()
    app = GUIManager(root, sensor_manager, data_logger, alarm_manager)
    root.mainloop()
