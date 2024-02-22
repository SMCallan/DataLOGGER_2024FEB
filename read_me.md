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

- `main.py`: The main script that initializes the GUI and starts the sensor monitoring and data logging.
- `gui_manager.py`: Manages the graphical user interface where sensor data is displayed.
- `sensor_manager.py`: Handles the reading of sensor data from the GPIO pins or ADC.
- `data_logger.py`: Manages logging of sensor data to a file.
- `alarm_manager.py`: Checks sensor data against predefined thresholds to trigger alarms.
- `config.py`: Contains configuration settings for the project.

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