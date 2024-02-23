# Raspberry Pi Sensor Monitoring Project

This project is designed to offer a robust solution for real-time sensor monitoring on the Raspberry Pi, featuring a graphical user interface (GUI) for live data visualization, data logging capabilities for historical analysis, and an alarm system for threshold-based alerts. It's ideal for a wide range of applications, from environmental monitoring to home automation systems.

## Prerequisites

To run this project, you'll need:
- A Raspberry Pi set up with the latest Raspberry Pi OS.
- Compatible sensors connected to the Raspberry Pi. The project is pre-configured for CO, O2, and Dust sensors but can be adapted for others.
- An active internet connection on your Raspberry Pi for library installations.

## Installation

Follow these steps to prepare your environment:

1. **Update and Upgrade your Raspberry Pi:**

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Ensure Python 3 and pip are installed:**

    Python 3 comes pre-installed on Raspberry Pi OS. Verify its installation with `python3 --version`. If needed, install pip:

    ```bash
    sudo apt-get install python3-pip
    ```

3. **Install Required Libraries:**

    - **Tkinter for GUI** (usually comes with Python 3):

        ```bash
        sudo apt-get install python3-tk
        ```
    
    - **Matplotlib for plotting sensor data**:
    
        ```bash
        pip3 install matplotlib
        ```
    
    - **Adafruit_ADS1x15 for analog-to-digital conversion**:
    
        ```bash
        pip3 install Adafruit-ADS1x15
        ```
    
    - **RPi.GPIO for GPIO control** (pre-installed but can be updated):
    
        ```bash
        pip3 install RPi.GPIO
        ```

## Project Overview

- **`main.py`**: Initializes all managers (GUI, Sensor, Data Logger, Alarm) and starts the main application. It handles the creation of a separate thread for continuous data logging.

- **`config.py`**: Contains configurations such as sensor mappings to ADC channels or GPIO pins, data logging intervals, and GUI update frequencies.

- **`gui_manager.py`**: Manages the application's GUI, displaying sensor data in real-time, updating plots, and facilitating user interactions like report generation.

- **`data_logger.py`**: Responsible for logging sensor data into CSV files and generating reports that summarize sensor data over specified intervals.

- **`alarm_manager.py`**: Evaluates sensor data against defined thresholds to identify and report alarm conditions.

- **`sensor_manager.py`**: Handles reading data from both analog and digital sensors, abstracting the hardware layer from the rest of the application.

## Running the Application

1. **Prepare Your Sensors:**
   Ensure your sensors are connected to the Raspberry Pi as per the configurations defined in `config.py`.

2. **Start the Application:**
   Navigate to the project's directory and execute:

    ```bash
    python3 main.py
    ```

   This launches the GUI, showcasing live sensor data and starting the data logging process.

## Customization

- **Sensor Configuration**: Modify `config.py` to match your specific sensor setup (types, channels, pins).
- **Functionality Expansion**: Extend `sensor_manager.py` for additional sensors or `alarm_manager.py` for more complex alarm conditions.
- **GUI Enhancements**: Adjust `gui_manager.py` to alter the GUI layout, themes, or add new UI elements.

## Troubleshooting

- **Library Issues**: Confirm all required libraries are installed. Reinstall any library if errors persist.
- **Hardware Connectivity**: Check sensor connections and configurations if data is not appearing as expected.
- **Permission Errors**: Ensure your Raspberry Pi user has the necessary permissions, especially for GPIO access.

---

This README aims to guide you through setting up and customizing the Raspberry Pi Sensor Monitoring Project for your specific needs. Adaptations may be necessary based on your hardware setup, sensor types, and application requirements.
