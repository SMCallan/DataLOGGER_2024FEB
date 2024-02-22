# Raspberry Pi Sensor Monitoring Project

This project provides a comprehensive system for monitoring sensor data on a Raspberry Pi, displaying the readings in a graphical user interface (GUI), and logging the data for future analysis. It also includes an alarm management system that triggers alerts based on predefined sensor value thresholds or trends.

## Prerequisites

Before you begin, ensure you have the following:
- A Raspberry Pi set up with Raspbian (or any compatible Raspberry Pi OS).
- Physical sensors connected to your Raspberry Pi. This project is configured for generic sensors, but specifics can be adjusted in the code.
- An internet connection on your Raspberry Pi to download the necessary libraries.

## Installation

1. **Update your Raspberry Pi:**

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Install Python 3 and pip (if not already installed):**

    ```bash
    sudo apt-get install python3 python3-pip
    ```

3. **Install Required Python Libraries:**

    The project requires several Python libraries, including Tkinter for the GUI, Matplotlib for plotting, and Adafruit_ADS1x15 for ADC support.

    - Tkinter (should be included with Python 3):
    
        ```bash
        sudo apt-get install python3-tk
        ```
    
    - Matplotlib:
    
        ```bash
        pip3 install matplotlib
        ```
    
    - Adafruit_ADS1x15 for ADC sensor reading:
    
        ```bash
        pip3 install Adafruit-ADS1x15
        ```
    
    - RPi.GPIO for GPIO pin control (should be pre-installed, but you can reinstall if necessary):
    
        ```bash
        pip3 install RPi.GPIO
        ```

## Project Structure

- `main.py`: The main script that initializes the GUI and starts the sensor monitoring and data logging. It sets up the sensor manager, data logger, alarm manager, and GUI manager. It also starts a separate thread for automatic data logging.

- `config.py`: This file contains the configuration for your sensor system, including the mapping of sensors to their respective channels or pins, and settings for data logging and GUI update intervals.

- `gui_manager.py`: This file defines the `GUIManager` class, which manages the graphical user interface for your application. It reads sensor data, updates the sensor data plot, and redraws the canvas.

- `data_logger.py`: This file defines the `DataLogger` class, which logs sensor data to a CSV file.

- `alarm_manager.py`: This class is responsible for checking alarms based on sensor data. It checks for over-threshold values and increasing trends in the sensor data. If any of these conditions are met, it adds an alarm message to the list of alarms, which it then returns.

- `sensor_manager.py`: This class manages the sensors in your system. It initializes the ADC device for reading analog sensors and sets up the GPIO mode for digital sensor pins. It also loads sensor configurations from the settings in `config.py`. The `read_sensor` method reads and returns data from a specified sensor, and the `get_sensor_ids` method returns a list of all configured sensor IDs.

## Running the Project

1. **Clone the project to your Raspberry Pi:**

    Clone or download the project files to a directory on your Raspberry Pi.

2. **Connect Your Sensors:**

    Ensure your sensors are correctly connected to the Raspberry Pi. The default configuration uses GPIO pins and an ADS1115 ADC. Adjust `sensor_manager.py` as needed to match your sensor setup.

3. **Launch the Application:**

    Navigate to the project directory and run the following command to start the project:

    ```bash
    python3 main.py
    ```

    The GUI will start, displaying real-time sensor data and logging the readings to a CSV file.

## Customization

You can customize the project settings in `config.py`, such as sensor IDs, data logging interval, and GUI update interval. If you're using different sensors or additional hardware, you may need to adjust the `sensor_manager.py` accordingly.

## Troubleshooting

- Ensure all libraries are correctly installed and up to date.
- Check your sensor connections and configurations in `sensor_manager.py`.
- If you encounter errors with the ADC or GPIO, verify that your Raspberry Pi has the correct permissions to access these resources.

---

This README provides a general guide for setting up and running the Raspberry Pi Sensor Monitoring Project. You might need to adjust paths, library versions, or hardware configurations based on your specific setup and the sensors you are using.