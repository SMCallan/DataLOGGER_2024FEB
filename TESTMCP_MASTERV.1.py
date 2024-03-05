from tkinter import Tk, Frame, Label, Button
from tkinter import SUNKEN, TOP, LEFT, X, Y, BOTTOM, BOTH
from PIL import Image, ImageTk, ImageDraw
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from subprocess import call
import sys
from __future__ import print_function  # Enables compatibility with Python 3 print function
from tkinter import *  # Provides GUI functionality for creating windows, buttons, etc.
from tkinter import messagebox  # Displays message boxes in the GUI
from tkinter import filedialog  # Allows the user to select files or directories
from tkinter import ttk  # Provides additional GUI widgets and styles
from tkcalendar import Calendar  # Displays a calendar widget in the GUI
from tkcalendar import DateEntry  # Displays a date entry widget in the GUI
from datetime import datetime, date  # Provides date and time functionality
import shutil  # Provides high-level file operations (copy, move, etc.)
import PIL  # Python Imaging Library for image processing
from PIL import ImageTk, Image, ImageDraw  # Allows image manipulation and display in the GUI
import RPi.GPIO as GPIO  # Library for controlling Raspberry Pi GPIO pins
import matplotlib  # Library for creating plots and graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embeds matplotlib figures in Tkinter GUI
from matplotlib.figure import Figure  # Represents a figure (plot) in matplotlib
import os  # Provides functions for interacting with the operating system
import time  # Provides time-related functions
import Adafruit_ADS1x15  # Library for interacting with ADS1x15 analog-to-digital converters
os.system("sudo pigpiod")  # Launches the GPIO library for Raspberry Pi
time.sleep(1)  # Delays execution for 1 second
import pigpio  # Library for controlling GPIO pins on Raspberry Pi
from pygame import mixer  # Library for playing audio files
import pickle  # Provides serialization and deserialization of Python objects
import csv  # Provides functionality for reading and writing CSV files
import math  # Provides mathematical functions and constants
import sys  # Provides access to some variables used or maintained by the interpreter
import smbus  # Library for I2C communication with devices
# from pymodbus.server.asynchronous import StartSerialServer  # Asynchronous Modbus server implementation
# from pymodbus.device import ModbusDeviceIdentification  # Modbus device identification
# from pymodbus.datastore import ModbusSequentialDataBlock  # Modbus sequential data block
# from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext  # Modbus slave and server context
# from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer, ModbusBinaryFramer  # Modbus framers
# from pymodbus.constants import Endian  # Constants for Modbus communication
# from pymodbus.payload import BinaryPayloadDecoder  # Decodes binary Modbus payloads
# from pymodbus.payload import BinaryPayloadBuilder  # Builds binary Modbus payloads
# from twisted.internet.task import LoopingCall  # Repeatedly calls a function at a specified interval
from multiprocessing import Process  # Provides support for spawning processes
from threading import Thread  # Provides support for threading
# import pymodbus  # Library for Modbus communication
# from pymodbus.client.sync import ModbusTcpClient  # Synchronous Modbus TCP client
from fpdf import FPDF  # Library for creating PDF documents
import warnings  # Provides control over warning messages
import usb  # Library for USB communication
from subprocess import call  # Executes shell commands
from pathlib import Path  # Provides object-oriented file system paths
import serial  # Library for serial communication

warnings.filterwarnings("ignore", category=DeprecationWarning) 
SavePath = "/home/pi/MCP_Plus/"
DataPath = "/home/pi/MCP_Plus/Data/"
matplotlib.use('TkAgg')
mixer.init()
alert=mixer.Sound(SavePath + 'bell.wav')
PathtoUSB = ""
ESC=21
PlotSecs = 0
TimeList = []
Data1List = []
Data2List = []
Data3List = []
Data4List = []
Data5List = []
Data6List = []
Data7List = []
Data8List = []
Output1List = []
Output2List = []
Output3List = []
Output4List = []
Output5List = []
Output6List = []
Output7List = []
Output8List = []
CycleSoFar = 0
RunOn = 0
Alarm = 0
XMin = 0
YMin = 0
XMax = 60
YMax = 50
FirstRound = 0
AverageTime = 60
AlarmSilent = 0
adc1 = Adafruit_ADS1x15.ADS1115(address=0x48)
adc2 = Adafruit_ADS1x15.ADS1115(address=0x49)
MyNumber = 0
MyText = ""
ButtonColour = "deepskyblue"
CH1Offset = float(1.16156)
CH1Slope = float(0.00067)
CH2Offset = float(1.16156)
CH2Slope = float(0.00067)
CH3Offset = float(1.16156)
CH3Slope = float(0.00067)
CH4Offset = float(1.16156)
CH4Slope = float(0.00067)
CH5Offset = float(1.16156)
CH5Slope = float(0.00067)
CH6Offset = float(1.16156)
CH6Slope = float(0.00067)
CH7Offset = float(1.16156)
CH7Slope = float(0.00067)
CH8Offset = float(1.16156)
CH8Slope = float(0.00067)
#MY_SDSN = 12212             # Dinkey Dongle SDSN number (demo = 10101, mine = 12212, DRM MCPD system = 13256)
# MY_SDSN = 13256
# #MY_PRODCODE = "TECHMON1"
# MY_PRODCODE = "DRMMCPD1"
AlarmCode = "0000000000000000"
MCPAlarmCode = "0000000000000000"

O21Correct = "Y"
O22Correct = "Y"
O23Correct = "Y"
O24Correct = "Y"
O25Correct = "Y"
O26Correct = "Y"
O27Correct = "Y"
O28Correct = "Y"
O2Ref = 3
Ch1Units = "mg/m3"
Ch2Units = "mg/m3"
Ch3Units = "mg/m3"
Ch4Units = "mg/m3"
Ch5Units = "mg/m3"
Ch6Units = "mg/m3"
Ch7Units = "mg/m3"
Ch8Units = "mg/m3"


# code for optional i2c relay output board
#NUM_RELAY_PORTS = 4
# Change the following value if your Relay board uses a different I2C address. 
#DEVICE_ADDRESS = 0x20  # 7 bit address (will be left shifted to add the read write bit)
# Don't change the values, there's no need for that.
#DEVICE_REG_MODE1 = 0x06
#DEVICE_REG_DATA = 0xff
bus = smbus.SMBus(1)  # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
UseRelays = 1
if UseRelays == 1:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(33,GPIO.OUT)
    # DO NOT USE RELAY 1, GPIO pin 35, IT INTERFERES WITH MODBUS HAT
    # pins used by relays are Relay 1 = 35, relay 2 = 33, Relay 3 = 31, Relay 4 = 29
FTBoards_Installed = 1 

# decide if password is needed to make changes to system
UsePassword = "N"
O2CutOff = 19.5
# Define which interface board is in use
# Custard Pi is CUSTARD
#4 channel, 16 bit ADC from SEEED is SEEED
PiHat = "SEEED"


def MakeReport(Source, ReportPeriod):
    # open the csv file and read in contents
    # need to set file name based on requested report date
    MyFile = Path(Source)
    if MyFile.is_file():
        # print("File exists")    
        with open(Source, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            #get fieldnames from DictReader object and store in list
            headers = reader.fieldnames
            
            # set local variables
            Col0 = headers[0]
            Col1 = headers[1]
            Col2 = headers[2]
            Col3 = headers[3]
            Col4 = headers[4]
            Col5 = headers[5]
            Col6 = headers[6]
            Col7 = headers[7]
            Col8 = headers[8]
            Col9 = headers[9]
            TotalTime = 0
            TotalOpTime = 0
            Col1Total = 0
            Col2Total = 0
            Col3Total = 0
            Col4Total = 0
            Col5Total = 0
            Col6Total = 0
            Col7Total = 0
            Col8Total = 0
            Col9Total = 0
            Col1OpTotal = 0
            Col2OpTotal = 0
            Col3OpTotal = 0
            Col4OpTotal = 0
            Col5OpTotal = 0
            Col6OpTotal = 0
            Col7OpTotal = 0
            Col8OpTotal = 0
            Col9OpTotal = 0
            i = 0
            j = 0
            
            # read in csv row by row
            for row in reader:
                # update progressbar
                #if ReportProgress['value'] < 100:
                #    ReportProgress['value'] += 10
                #else:
                #    ReportProgress['value'] = 0
                
                # Calculate minutes of data
                # ignore first row
                if i != 0:
                    date_time_obj = datetime.strptime(row[Col0], '%d/%m/%Y %H:%M:%S')
                    EndTime = date_time_obj
                # if > first row and plant running
                if i > 0 and int(row[Col9]) == 1:
                    difference = EndTime - StartTime
                    TimeGap = difference.days * 86400 + difference.seconds
                    TotalOpTime = TotalOpTime + TimeGap
                # if > first row and plany not running     
                if i > 0:
                    difference = EndTime - StartTime
                    TimeGap = difference.days * 86400 + difference.seconds
                    TotalTime = TotalTime + TimeGap
                    Col1Total = Col1Total + float(row[Col1])
                    Col2Total = Col2Total + float(row[Col2])
                    Col3Total = Col3Total + float(row[Col3])
                    Col4Total = Col4Total + float(row[Col4])
                    Col5Total = Col5Total + float(row[Col5])
                    Col6Total = Col6Total + float(row[Col6])
                    Col7Total = Col7Total + float(row[Col7])
                    Col8Total = Col8Total + float(row[Col8])
                # set start time of dataset  
                date_time_obj = datetime.strptime(row[Col0], '%d/%m/%Y %H:%M:%S')
                StartTime = date_time_obj
                # add to 'i' to record total number of readings in file
                i = i + 1
                
                if int(row[Col9]) == 1:
                    # add to 'j' to record total number of readings in file if plant was operating
                    j = j + 1
                    # Add up all the columns of data if plant was on
                    Col1OpTotal = Col1OpTotal + float(row[Col1])
                    Col2OpTotal = Col2OpTotal + float(row[Col2])
                    Col3OpTotal = Col3OpTotal + float(row[Col3])
                    Col4OpTotal = Col4OpTotal + float(row[Col4])
                    Col5OpTotal = Col5OpTotal + float(row[Col5])
                    Col6OpTotal = Col6OpTotal + float(row[Col6])
                    Col7OpTotal = Col7OpTotal + float(row[Col7])
                    Col8OpTotal = Col8OpTotal + float(row[Col8])
                
        #print("Total Time Sampled (s) = "+str(TotalTime))
        print("Total Time Sampled (Hrs) = "+str(round(TotalTime/60/60,1)))
        print("total readings with plant on - " + str(j))
        print("Column 1 Ave = " + str(round(Col1Total/i,2)))
        if j != 0:
            print("Column 1 Op Ave = " + str(round(Col1OpTotal/j,2)))

        #print("Column 2 Ave = " + str(round(Col2Total/i,2)))
        #print("Column 3 Ave = " + str(round(Col3Total/i,2)))
        #print("Column 4 Ave = " + str(round(Col4Total/i,2)))
        #print("Column 5 Ave = " + str(round(Col5Total/i,2)))
        #print("Column 6 Ave = " + str(round(Col6Total/i,2)))
        #print("Column 7 Ave = " + str(round(Col7Total/i,2)))
        #print("Column 8 Ave = " + str(round(Col8Total/i,2)))
    else:
        messagebox.showinfo("ERROR", "Source Data File Not Found")
    
    def Generate_Report():
        # set data for report based in the read in csv data
        Tot_Hours = round(TotalTime/60/60,1)
        Op_Hours = round(TotalOpTime/60/60,1)
        CO_Ave = round(Col1Total/i,2)
        NO_Ave = round(Col2OpTotal/i,2)
        NO2_Ave = round(Col3OpTotal/i,2)
        SO2_Ave = round(Col4OpTotal/i,2)
        CH4_Ave = round(Col5OpTotal/i,2)
        O2_Ave = round(Col6OpTotal/i,2)
        Dust_Ave = round(Col7OpTotal/i,2)
        Stack_Temp = round(Col8OpTotal/i,2)

        if j != 0:
            CO_Op_Ave = round(Col1OpTotal/j,2)
            NO_Op_Ave = round(Col2OpTotal/j,2)
            NO2_Op_Ave = round(Col3OpTotal/j,2)
            SO2_Op_Ave = round(Col4OpTotal/j,2)
            CH4_Op_Ave = round(Col5OpTotal/j,2)
            O2_Op_Ave = round(Col6OpTotal/j,2)
            Dust_Op_Ave = round(Col7OpTotal/j,2)
            Temp_Op_Ave = round(Col8OpTotal/j,2)
        else:
            CO_Op_Ave = 0
            NO_Op_Ave = 0
            NO2_Op_Ave = 0
            SO2_Op_Ave = 0
            CH4_Op_Ave = 0
            O2_Op_Ave = 0
            Dust_Op_Ave = 0
            Temp_Op_Ave = 0
            
        # get todays date for 'report generated date'
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        d2 = today.strftime("%B")

        # set header and footer 
        class PDF(FPDF):
            def header(self):
                LogoWidth = 32
                LogoHeight = 14
                self.image('DRM_Logo.png', 10, LogoHeight, LogoWidth)
                self.image('OPS_Logo.png', self.w-10-LogoWidth, LogoHeight, LogoWidth)
                self.set_font('times', 'B', 16)
                self.cell(0,10, 'Monthly Emissions Report', ln=1, align='C')
                #self.ln(10)
                self.cell(0,10, str(Plant_ID), ln=1, align='C')
                self.ln(20)
                
            def footer(self):
                self.set_y(-15)
                self.set_font('times', 'I', 12)
                self.cell(0, 10, f'Page {self.page_no()} of {{nb}}',align='C')
                self.set_font('times', 'I', 8)
                self.cell(0, 10, 'DRM Technic MCP monthly reporting', align='R')
                
        # set page size
        PDF_Report = PDF('P', 'mm', 'A4')
        # need to calc total no of pages
        PDF_Report.alias_nb_pages()
        # create the page
        PDF_Report.add_page()
        # possible fonts are 'times', 'courier', 'helvetica', 'symbol'
        # 'B' Bold - 'U' Underline - 'I' Italics -
        PDF_Report.set_auto_page_break(auto=True, margin=15)
        # add some text

        # Site Information Section
        Col1Wide = 35
        Col2Wide = 70
        Col3Wide = 35
        Col4Wide = 30
        RowHeight = 7

        PDF_Report.set_font('times', 'B', 12)
        PDF_Report .cell(45, RowHeight, 'Site Information', ln=1, border = True)

        PDF_Report.set_font('times', '', 12)
        PDF_Report.cell(Col1Wide, RowHeight, 'Site Address:', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Address_1), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'Report Date:', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, str(d1), border = True, ln=1)

        PDF_Report.cell(Col1Wide, RowHeight, '', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Address_2), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, '', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = True, ln=1)

        PDF_Report.cell(Col1Wide, RowHeight, '', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Address_3), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'Site Contact:', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, Site_Contact, border = True, ln=True)

        PDF_Report.cell(Col1Wide, RowHeight, '', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Post_Code), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'Permit No:', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, str(Permit_No), border = True, ln=True)

        PDF_Report.ln(10)

        # Report info
        PDF_Report.cell(50, 8, 'Month:', border=True)
        PDF_Report.cell(40, 8, 'October 2022', ln=True, border=True)

        PDF_Report.cell(50, 8, 'Operating Hours:', border=True)
        PDF_Report.cell(40, 8, str(Op_Hours), ln=True, border=True)
        PDF_Report.ln(10)

        Col1Wide = 20
        Col2Wide = 20
        Col3Wide = 45
        Col4Wide = 10
        Col5Wide = 20
        Col6Wide = 20
        Col7Wide = 45    
        RowHeight = 7
        
        PDF_Report.set_font('times', 'B', 12)
        PDF_Report .cell(Col1Wide+Col2Wide+Col3Wide, RowHeight, 'Monthly Average (All hours)', border = True)
        PDF_Report .cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report .cell(Col5Wide+Col6Wide+Col7Wide, RowHeight, 'Monthly Average (operating hours)', ln=True, border = True)
        
        PDF_Report.set_font('times', '', 12)
        # CO
        PDF_Report.cell(Col1Wide, RowHeight, 'CO', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(CO_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'CO', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(CO_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
            
        # NO
        PDF_Report.cell(Col1Wide, RowHeight, 'NO', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(NO_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'NO', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(NO_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)

        # NO2
        PDF_Report.cell(Col1Wide, RowHeight, 'NO2', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(NO2_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'NO2', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(NO2_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
        
        # SO2
        PDF_Report.cell(Col1Wide, RowHeight, 'SO2', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(SO2_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'SO2', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(SO2_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
        
        # CH4
        PDF_Report.cell(Col1Wide, RowHeight, 'CH4', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(CH4_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'CH4', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(CH4_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
        
        # O2
        PDF_Report.cell(Col1Wide, RowHeight, 'O2', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(O2_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'O2', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(O2_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
        
        # Dust
        PDF_Report.cell(Col1Wide, RowHeight, 'Dust', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Dust_Ave), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'mg/m3 @ 3% O2', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'Dust', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(Dust_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'mg/m3 @ 3% O2', border = True, ln=True)
        
        #Stack_Temp
        PDF_Report.cell(Col1Wide, RowHeight, 'Temp', border = True)
        PDF_Report.cell(Col2Wide, RowHeight, str(Stack_Temp), border = True)
        PDF_Report.cell(Col3Wide, RowHeight, 'Deg C', border = True)
        PDF_Report.cell(Col4Wide, RowHeight, '', border = False)
        PDF_Report.cell(Col5Wide, RowHeight, 'Temp', border = True)
        PDF_Report.cell(Col6Wide, RowHeight, str(Temp_Op_Ave), border = True)
        PDF_Report.cell(Col7Wide, RowHeight, 'Deg C', border = True, ln=True)
        
        # output the PDF file
        PDF_Report.output(ReportPeriod+"_"+Plant_ID+'_Monthly Report.pdf')
        print ("Report Generation Complete")


    Generate_Report()



def relay_on(relay_num):
    if FailSafe == 1:
        GPIO.output(33,GPIO.LOW)
    else:
        GPIO.output(33,GPIO.HIGH)
    # pins used by relays are Relay 1 = 35 (do not use), relay 2 = 33, Relay 3 = 31, Relay 4 = 29 
# code below for optional i2c relay baord
#    global DEVICE_ADDRESS
#    global DEVICE_REG_DATA
#    global DEVICE_REG_MODE1
#
#    if isinstance(relay_num, int):
#        # do we have a valid relay number?
#        if 0 < relay_num <= NUM_RELAY_PORTS:
#            print('Turning relay', relay_num, 'ON')
#            DEVICE_REG_DATA &= ~(0x1 << (relay_num - 1))
#            bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, DEVICE_REG_DATA)
#        else:
#            print('Invalid relay #:', relay_num)
#    else:
#        print('Relay number must be an Integer value')


def relay_off(relay_num):
    if FailSafe == 1:
        GPIO.output(33,GPIO.HIGH)
    else:    
        GPIO.output(33,GPIO.LOW)
    # pins used by relays are Relay 1 = 35 (Do not use), relay 2 = 33, Relay 3 = 31, Relay 4 = 29 

# code below for optional i2c relay baord
#    global DEVICE_ADDRESS
#    global DEVICE_REG_DATA
#    global DEVICE_REG_MODE1
#
#    if isinstance(relay_num, int):
#        # do we have a valid relay number?
#        if 0 < relay_num <= NUM_RELAY_PORTS:
#            print('Turning relay', relay_num, 'OFF')
#            DEVICE_REG_DATA |= (0x1 << (relay_num - 1))
#            bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, DEVICE_REG_DATA)
#        else:
#            print('Invalid relay #:', relay_num)
#    else:
#        print('Relay number must be an Integer value')

# Set alarm to failsafe condition
relay_on(1)
       
    
def handle_click(event):
    #AlarmsWindow
    return
    #EntryName.insert(END,"123")

def TextPad(EntryName):
    
    # create functions for what to do when each number is clicked
    def Text_1():
        TextEntry.insert(END,"1")
    def Text_2():
        TextEntry.insert(END,"2")
    def Text_3():
        TextEntry.insert(END,"3")
    def Text_4():
        TextEntry.insert(END,"4")
    def Text_5():
        TextEntry.insert(END,"5")
    def Text_6():
        TextEntry.insert(END,"6")
    def Text_7():
        TextEntry.insert(END,"7")
    def Text_8():
        TextEntry.insert(END,"8")
    def Text_9():
        TextEntry.insert(END,"9")
    def Text_0():
        TextEntry.insert(END,"0")
    def Text_Q():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"Q")
        else:
            TextEntry.insert(END,"q")
    def Text_W():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"W")
        else:
            TextEntry.insert(END,"w")
    def Text_E():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"E")
        else:
            TextEntry.insert(END,"e")
    def Text_R():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"R")
        else:
            TextEntry.insert(END,"r")
    def Text_T():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"T")
        else:
            TextEntry.insert(END,"t")
    def Text_Y():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"Y")
        else:
            TextEntry.insert(END,"y")
    def Text_U():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"U")
        else:
            TextEntry.insert(END,"u")
    def Text_I():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"I")
        else:
            TextEntry.insert(END,"i")
    def Text_O():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"O")
        else:
            TextEntry.insert(END,"o")
    def Text_P():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"P")
        else:
            TextEntry.insert(END,"p")
    def Text_A():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"A")
        else:
            TextEntry.insert(END,"a")
    def Text_S():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"S")
        else:
            TextEntry.insert(END,"s")
    def Text_D():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"D")
        else:
            TextEntry.insert(END,"d")
    def Text_F():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"F")
        else:
            TextEntry.insert(END,"f")
    def Text_G():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"G")
        else:
            TextEntry.insert(END,"g")
    def Text_H():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"H")
        else:
            TextEntry.insert(END,"h")
    def Text_J():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"J")
        else:
            TextEntry.insert(END,"j")
    def Text_K():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"K")
        else:
            TextEntry.insert(END,"k")
    def Text_L():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"L")
        else:
            TextEntry.insert(END,"l")
    def Text_Z():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"Z")
        else:
            TextEntry.insert(END,"z")
    def Text_X():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"X")
        else:
            TextEntry.insert(END,"x")
    def Text_C():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"C")
        else:
            TextEntry.insert(END,"c")
    def Text_V():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"V")
        else:
            TextEntry.insert(END,"v")
    def Text_B():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"B")
        else:
            TextEntry.insert(END,"b")
    def Text_N():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"N")
        else:
            TextEntry.insert(END,"n")
    def Text_M():
        if TextShift['relief']=="sunken":
            TextEntry.insert(END,"M")
        else:
            TextEntry.insert(END,"m")
    def Text_Space():
        TextEntry.insert(END," ")
    def Text_Shift():
        if TextShift['relief']=="raised":
            TextShift['relief']="sunken"
            TextQ['text'] = TextQ['text'].upper()
            TextW['text'] = TextW['text'].upper()
            TextE['text'] = TextE['text'].upper()
            TextR['text'] = TextR['text'].upper()
            TextT['text'] = TextT['text'].upper()
            TextY['text'] = TextY['text'].upper()
            TextU['text'] = TextU['text'].upper()
            TextI['text'] = TextI['text'].upper()
            TextO['text'] = TextO['text'].upper()
            TextP['text'] = TextP['text'].upper()
            TextA['text'] = TextA['text'].upper()
            TextS['text'] = TextS['text'].upper()
            TextD['text'] = TextD['text'].upper()
            TextF['text'] = TextF['text'].upper()
            TextG['text'] = TextG['text'].upper()
            TextH['text'] = TextH['text'].upper()
            TextJ['text'] = TextJ['text'].upper()
            TextK['text'] = TextK['text'].upper()
            TextL['text'] = TextL['text'].upper()
            TextZ['text'] = TextZ['text'].upper()
            TextX['text'] = TextX['text'].upper()
            TextC['text'] = TextC['text'].upper()
            TextV['text'] = TextV['text'].upper()
            TextB['text'] = TextB['text'].upper()
            TextN['text'] = TextN['text'].upper()
            TextM['text'] = TextM['text'].upper()
        else:
            TextShift['relief']="raised" 
            TextQ['text'] = TextQ['text'].lower()
            TextW['text'] = TextW['text'].lower()
            TextE['text'] = TextE['text'].lower()
            TextR['text'] = TextR['text'].lower()
            TextT['text'] = TextT['text'].lower()
            TextY['text'] = TextY['text'].lower()
            TextU['text'] = TextU['text'].lower()
            TextI['text'] = TextI['text'].lower()
            TextO['text'] = TextO['text'].lower()
            TextP['text'] = TextP['text'].lower()
            TextA['text'] = TextA['text'].lower()
            TextS['text'] = TextS['text'].lower()
            TextD['text'] = TextD['text'].lower()
            TextF['text'] = TextF['text'].lower()
            TextG['text'] = TextG['text'].lower()
            TextH['text'] = TextH['text'].lower()
            TextJ['text'] = TextJ['text'].lower()
            TextK['text'] = TextK['text'].lower()
            TextL['text'] = TextL['text'].lower()
            TextZ['text'] = TextZ['text'].lower()
            TextX['text'] = TextX['text'].lower()
            TextC['text'] = TextC['text'].lower()
            TextV['text'] = TextV['text'].lower()
            TextB['text'] = TextB['text'].lower()
            TextN['text'] = TextN['text'].lower()
            TextM['text'] = TextM['text'].lower()
        #TextEntry.insert(END," ")
    def Text_Back():
        TextEntry.delete(len(TextEntry.get())-1)
    def Text_Enter():
        MyText = TextEntry.get()
        if MyText != "":
            EntryName.delete(0,"end")
            EntryName.insert(0,MyText)
        TextPadWindow.destroy()

    # create the visible popup text pad
    TextPadWindow = Toplevel(root)
    TextPadWindow.title("Text Pad")
    
    # add frames for the number of rows of buttons
    TNumFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TNumFrame.pack(expand=True, side=TOP, fill=BOTH)
    TFirFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TFirFrame.pack(expand=True, side=TOP, fill=BOTH)
    TSecFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TSecFrame.pack(expand=True, side=TOP, fill=BOTH)
    TThiFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TThiFrame.pack(expand=True, side=TOP, fill=BOTH)
    TForFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TForFrame.pack(expand=True, side=TOP, fill=BOTH)
    TFitFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TFitFrame.pack(expand=True, side=TOP, fill=BOTH)
    TSixFrame = Frame(TextPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    TSixFrame.pack(expand=True, side=TOP, fill=BOTH)
    
    # set the colour of the number pad buttons
    ButCol = "violet"
    
    # create each of the buttons within the rows (frames)
    Text1 = Button(TNumFrame, text="1", width = 5, padx=10, pady=20, command=Text_1, bg=ButCol)
    Text1.pack(side=LEFT, padx=3)
    Text2 = Button(TNumFrame, text="2", width = 5, padx=10, pady=20, command=Text_2, bg=ButCol)
    Text2.pack(side=LEFT, padx=3)
    Text3 = Button(TNumFrame, text="3", width = 5, padx=10, pady=20, command=Text_3, bg=ButCol)
    Text3.pack(side=LEFT, padx=3)
    Text4 = Button(TNumFrame, text="4", width = 5, padx=10, pady=20, command=Text_4, bg=ButCol)
    Text4.pack(side=LEFT, padx=3)
    Text5 = Button(TNumFrame, text="5", width = 5, padx=10, pady=20, command=Text_5, bg=ButCol)
    Text5.pack(side=LEFT, padx=3)
    Text6 = Button(TNumFrame, text="6", width = 5, padx=10, pady=20, command=Text_6, bg=ButCol)
    Text6.pack(side=LEFT, padx=3)
    Text7 = Button(TNumFrame, text="7", width = 5, padx=10, pady=20, command=Text_7, bg=ButCol)
    Text7.pack(side=LEFT, padx=3)
    Text8 = Button(TNumFrame, text="8", width = 5, padx=10, pady=20, command=Text_8, bg=ButCol)
    Text8.pack(side=LEFT, padx=3)
    Text9 = Button(TNumFrame, text="9", width = 5, padx=10, pady=20, command=Text_9, bg=ButCol)
    Text9.pack(side=LEFT, padx=3)
    Text0 = Button(TNumFrame, text="0", width = 5, padx=10, pady=20, command=Text_0, bg=ButCol)
    Text0.pack(side=LEFT, padx=3)
    GapLabel = Label(TFirFrame, text=" ", padx=10, pady=1)
    GapLabel.pack(side=LEFT, padx=3)
    TextQ = Button(TFirFrame, text="q", width = 5, padx=10, pady=20, command=Text_Q, bg=ButCol)
    TextQ.pack(side=LEFT, padx=3)
    TextW = Button(TFirFrame, text="w", width = 5, padx=10, pady=20, command=Text_W, bg=ButCol)
    TextW.pack(side=LEFT, padx=3)
    TextE = Button(TFirFrame, text="e", width = 5, padx=10, pady=20, command=Text_E, bg=ButCol)
    TextE.pack(side=LEFT, padx=3)
    TextR = Button(TFirFrame, text="r", width = 5, padx=10, pady=20, command=Text_R, bg=ButCol)
    TextR.pack(side=LEFT, padx=3)
    TextT = Button(TFirFrame, text="t", width = 5, padx=10, pady=20, command=Text_T, bg=ButCol)
    TextT.pack(side=LEFT, padx=3)
    TextY = Button(TFirFrame, text="y", width = 5, padx=10, pady=20, command=Text_Y, bg=ButCol)
    TextY.pack(side=LEFT, padx=3)
    TextU = Button(TFirFrame, text="u", width = 5, padx=10, pady=20, command=Text_U, bg=ButCol)
    TextU.pack(side=LEFT, padx=3)
    TextI = Button(TFirFrame, text="i", width = 5, padx=10, pady=20, command=Text_I, bg=ButCol)
    TextI.pack(side=LEFT, padx=3)
    TextO= Button(TFirFrame, text="o", width = 5, padx=10, pady=20, command=Text_O, bg=ButCol)
    TextO.pack(side=LEFT, padx=3)
    TextP = Button(TFirFrame, text="p", width = 5, padx=10, pady=20, command=Text_P, bg=ButCol)
    TextP.pack(side=LEFT, padx=3)
    GapLabel = Label(TSecFrame, text="      ", padx=10, pady=1)
    GapLabel.pack(side=LEFT, padx=3)
    TextA = Button(TSecFrame, text="a", width = 5, padx=10, pady=20, command=Text_A, bg=ButCol)
    TextA.pack(side=LEFT, padx=3)
    TextS = Button(TSecFrame, text="s", width = 5, padx=10, pady=20, command=Text_S, bg=ButCol)
    TextS.pack(side=LEFT, padx=3)
    TextD = Button(TSecFrame, text="d", width = 5, padx=10, pady=20, command=Text_D, bg=ButCol)
    TextD.pack(side=LEFT, padx=3)
    TextF = Button(TSecFrame, text="f", width = 5, padx=10, pady=20, command=Text_F, bg=ButCol)
    TextF.pack(side=LEFT, padx=3)
    TextG = Button(TSecFrame, text="g", width = 5, padx=10, pady=20, command=Text_G, bg=ButCol)
    TextG.pack(side=LEFT, padx=3)
    TextH = Button(TSecFrame, text="h", width = 5, padx=10, pady=20, command=Text_H, bg=ButCol)
    TextH.pack(side=LEFT, padx=3)
    TextJ = Button(TSecFrame, text="j", width = 5, padx=10, pady=20, command=Text_J, bg=ButCol)
    TextJ.pack(side=LEFT, padx=3)
    TextK = Button(TSecFrame, text="k", width = 5, padx=10, pady=20, command=Text_K, bg=ButCol)
    TextK.pack(side=LEFT, padx=3)
    TextL = Button(TSecFrame, text="l", width = 5, padx=10, pady=20, command=Text_L, bg=ButCol)
    TextL.pack(side=LEFT, padx=3)
    GapLabel = Label(TThiFrame, text="                         ", padx=10, pady=1)
    GapLabel.pack(side=LEFT, padx=3)
    TextZ = Button(TThiFrame, text="z", width = 5, padx=10, pady=20, command=Text_Z, bg=ButCol)
    TextZ.pack(side=LEFT, padx=3)
    TextX = Button(TThiFrame, text="x", width = 5, padx=10, pady=20, command=Text_X, bg=ButCol)
    TextX.pack(side=LEFT, padx=3)
    TextC = Button(TThiFrame, text="c", width = 5, padx=10, pady=20, command=Text_C, bg=ButCol)
    TextC.pack(side=LEFT, padx=3)
    TextV = Button(TThiFrame, text="v", width = 5, padx=10, pady=20, command=Text_V, bg=ButCol)
    TextV.pack(side=LEFT, padx=3)
    TextB = Button(TThiFrame, text="b", width = 5, padx=10, pady=20, command=Text_B, bg=ButCol)
    TextB.pack(side=LEFT, padx=3)
    TextN = Button(TThiFrame, text="n", width = 5, padx=10, pady=20, command=Text_N, bg=ButCol)
    TextN.pack(side=LEFT, padx=3)
    TextM = Button(TThiFrame, text="m", width = 5, padx=10, pady=20, command=Text_M, bg=ButCol)
    TextM.pack(side=LEFT, padx=3)
    GapLabel = Label(TForFrame, text="                               ", padx=10, pady=1)
    GapLabel.pack(side=LEFT, padx=3)
    TextShift = Button(TForFrame, text="Shift", width = 8, padx=10, pady=20, command=Text_Shift, bg=ButCol)
    TextShift.pack(side=LEFT, padx=3)
    TextSpace = Button(TForFrame, text="Space", width = 16, padx=10, pady=20, command=Text_Space, bg=ButCol)
    TextSpace.pack(side=LEFT, padx=60)
    TextBack = Button(TForFrame, text="<-", width = 6, padx=10, pady=20, command=Text_Back, bg=ButCol)
    TextBack.pack(side=LEFT, padx=20)
    TextEnter = Button(TForFrame, text="Ent", width = 10, padx=10, pady=20, command=Text_Enter, bg=ButCol)
    TextEnter.pack(side=LEFT, padx=3)
    TextEntry = Entry(TSixFrame, width=5)
    TextEntry.pack(expand=True, side=TOP, fill=BOTH)
    return MyText


# try creating a popup number pad
def NumPad(EntryName):
    global MyNumber
    
    def Num1C():
        NumEntry.insert(END,"1")
    def Num2C():
        NumEntry.insert(END,"2")
    def Num3C():
        NumEntry.insert(END,"3")
    def Num4C():
        NumEntry.insert(END,"4")
    def Num5C():
        NumEntry.insert(END,"5")
    def Num6C():
        NumEntry.insert(END,"6")
    def Num7C():
        NumEntry.insert(END,"7")
    def Num8C():
        NumEntry.insert(END,"8")
    def Num9C():
        NumEntry.insert(END,"9")
    def Num0C():
        NumEntry.insert(END,"0")
    def NumMinusC():
        NumEntry.insert(END,"-")
    def NumBac():
        NumEntry.delete(len(NumEntry.get())-1)
    def NumEnt():
        global MyNumber
        MyNumber = NumEntry.get()
        if MyNumber != "":
            EntryName.delete(0,"end")
            EntryName.insert(0,MyNumber)
        NumPadWindow.destroy()
        
    NumPadWindow = Toplevel(root)
    NumPadWindow.title("Number Pad")

    FirFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    FirFrame.pack(expand=True, side=TOP, fill=BOTH)
    SecFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    SecFrame.pack(expand=True, side=TOP, fill=BOTH)
    ThiFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    ThiFrame.pack(expand=True, side=TOP, fill=BOTH)
    ForFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    ForFrame.pack(expand=True, side=TOP, fill=BOTH)
    FitFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    FitFrame.pack(expand=True, side=TOP, fill=BOTH)
    SixFrame = Frame(NumPadWindow, bd=2, padx=10, pady=1, relief=FLAT)
    SixFrame.pack(expand=True, side=TOP, fill=BOTH)
    ButCol = "violet"
    Num1 = Button(FirFrame, text="1", width = 6, padx=10, pady=20, command=Num1C, bg=ButCol)
    Num1.pack(side=LEFT)
    Num2 = Button(FirFrame, text="2", width = 6, padx=10, pady=20, command=Num2C, bg=ButCol)
    Num2.pack(side=LEFT)
    Num3 = Button(FirFrame, text="3", width = 6, padx=10, pady=20, command=Num3C, bg=ButCol)
    Num3.pack(side=LEFT)
    Num4 = Button(SecFrame, text="4", width = 6, padx=10, pady=20, command=Num4C, bg=ButCol)
    Num4.pack(side=LEFT)
    Num5 = Button(SecFrame, text="5", width = 6, padx=10, pady=20, command=Num5C, bg=ButCol)
    Num5.pack(side=LEFT)
    Num6 = Button(SecFrame, text="6", width = 6, padx=10, pady=20, command=Num6C, bg=ButCol)
    Num6.pack(side=LEFT)
    Num7 = Button(ThiFrame, text="7", width = 6, padx=10, pady=20, command=Num7C, bg=ButCol)
    Num7.pack(side=LEFT)
    Num8 = Button(ThiFrame, text="8", width = 6, padx=10, pady=20, command=Num8C, bg=ButCol)
    Num8.pack(side=LEFT)
    Num9 = Button(ThiFrame, text="9", width = 6, padx=10, pady=20, command=Num9C, bg=ButCol)
    Num9.pack(side=LEFT)
    NumMinus = Button(ForFrame, text="-", width = 6, padx=10, pady=20, command=NumMinusC, bg=ButCol)
    NumMinus.pack(side=LEFT)
    Num0 = Button(ForFrame, text="0", width = 6, padx=10, pady=20, command=Num0C, bg=ButCol)
    Num0.pack(side=LEFT)
    NumBack = Button(ForFrame, text="<-", width = 6, padx=10, pady=20, command=NumBac, bg=ButCol)
    NumBack.pack(side=LEFT)
    NumEnter = Button(FitFrame, text="Ent", width = 6, padx=10, pady=20, command=NumEnt, bg=ButCol)
    NumEnter.pack(side=TOP)
    NumEntry = Entry(SixFrame, width=5)
    NumEntry.pack(expand=True, side=TOP, fill=BOTH)
    return MyNumber

def CheckPassword(NextWindow):
    global UsePassword
    def SubmitPassword():
        if EntryBox.get() == "41813":
            #DRM D = 4, R = 18, M = 13
            NextWindow()
        else:
            PassWindow.lower()
            messagebox.showinfo("ERROR", "Incorrect Password")
            PassWindow.tkraise()
        PassWindow.destroy()
            
    PassWindow = Toplevel(root)
    PassWindow.title("Enter Advanced password to continue")
    
    OnlyFrame = Frame(PassWindow, bd=2, padx=150, pady=10, relief=FLAT)
    OnlyFrame.pack(expand=True, side=TOP, fill=BOTH)
    Label1 = Label(OnlyFrame, text="Enter Advanced Password", padx=10,)
    Label1.pack(side=TOP)
    EntryBox = Entry(OnlyFrame, width=10)
    EntryBox.pack(expand=True, padx=10, pady=20,side=TOP, fill=BOTH)
    EntryBox.bind("<1>", (lambda event: NumPad(EntryBox)))
    Submit = Button(OnlyFrame, text="Submit", width = 6, padx=10, pady=20, command=SubmitPassword, bg="Green")
    Submit.pack(side=TOP)
    if UsePassword != "Y":
        NextWindow()
        PassWindow.destroy()
    

def CheckUserPassword(NextWindow):
    def SubmitUserPassword():
        if EntryBox.get() == "151619":
            #OPS O = 15, P = 16, S = 19
            NextWindow()
        else:
            UserPassWindow.lower()
            messagebox.showinfo("ERROR", "Incorrect Password")
            UserPassWindow.tkraise()
        UserPassWindow.destroy()
            
    UserPassWindow = Toplevel(root)
    UserPassWindow.title("Enter User password to continue")
    
    OnlyFrame = Frame(UserPassWindow, bd=2, padx=150, pady=10, relief=FLAT)
    OnlyFrame.pack(expand=True, side=TOP, fill=BOTH)
    Label1 = Label(OnlyFrame, text="Enter User Password", padx=10,)
    Label1.pack(side=TOP)
    EntryBox = Entry(OnlyFrame, width=10)
    EntryBox.pack(expand=True, padx=10, pady=20,side=TOP, fill=BOTH)
    EntryBox.bind("<1>", (lambda event: NumPad(EntryBox)))
    Submit = Button(OnlyFrame, text="Submit", width = 6, padx=10, pady=20, command=SubmitUserPassword, bg="Green")
    Submit.pack(side=TOP)
    if UsePassword != "Y":
        NextWindow()
        UserPassWindow.destroy()

# set temporary default inital settings
# Channel Display Names
def CreateDefault():
    global CH1DispName
    global CH2DispName
    global CH3DispName
    global CH4DispName
    global CH5DispName
    global CH6DispName
    global CH7DispName
    global CH8DispName
    global CH1MinAlarm
    global CH2MinAlarm
    global CH3MinAlarm
    global CH4MinAlarm
    global CH5MinAlarm
    global CH6MinAlarm
    global CH7MinAlarm
    global CH8MinAlarm
    global CH1MaxAlarm
    global CH2MaxAlarm
    global CH3MaxAlarm
    global CH4MaxAlarm
    global CH5MaxAlarm
    global CH6MaxAlarm
    global CH7MaxAlarm
    global CH8MaxAlarm
    global Ch1MinAlOn
    global Ch2MinAlOn
    global Ch3MinAlOn
    global Ch4MinAlOn
    global Ch5MinAlOn
    global Ch6MinAlOn
    global Ch7MinAlOn
    global Ch8MinAlOn
    global Ch1MaxAlOn
    global Ch2MaxAlOn
    global Ch3MaxAlOn
    global Ch4MaxAlOn
    global Ch5MaxAlOn
    global Ch6MaxAlOn
    global Ch7MaxAlOn
    global Ch8MaxAlOn
    global Ch1Active
    global Ch2Active
    global Ch3Active
    global Ch4Active
    global Ch5Active
    global Ch6Active
    global Ch7Active
    global Ch8Active
    global Daily_Files
    global Monthly_Files
    global CH14mA
    global CH120mA
    global CH24mA
    global CH220mA
    global CH34mA
    global CH320mA
    global CH44mA
    global CH420mA
    global CH54mA
    global CH520mA
    global CH64mA
    global CH620mA
    global CH74mA
    global CH720mA
    global CH84mA
    global CH820mA
    global Ave_time
    global CH1Offset
    global CH1Slope
    global CH2Offset
    global CH2Slope
    global CH3Offset
    global CH3Slope
    global CH4Offset
    global CH4Slope
    global CH5Offset
    global CH5Slope
    global CH6Offset
    global CH6Slope
    global CH7Offset
    global CH7Slope
    global CH8Offset
    global CH8Slope
    global XMin
    global XMax
    global YMin
    global YMax
    global O21Correct
    global O22Correct
    global O23Correct
    global O24Correct
    global O25Correct
    global O26Correct
    global O27Correct
    global O28Correct
    global O2Ref
    global Ch1Units
    global Ch2Units
    global Ch3Units
    global Ch4Units
    global Ch5Units
    global Ch6Units
    global Ch7Units
    global Ch8Units
    global SavePath
    global Slave_ID
    global Modbus_Baud
    global Modbus_Bits
    global Modbus_Parity
    global Modbus_StopBits
    global Modbus_Timeout
    global Ch1Mod
    global Ch2Mod
    global Ch3Mod
    global Ch4Mod
    global Ch5Mod
    global Ch6Mod
    global Ch7Mod
    global Ch8Mod
    global Chk_Status
    global Run_If_Temp
    global Use_Stdby
    global User_Pass
    global Dwell_Time
    global Meas_Time
    global Purge_Time
    
    
    print("reset defaults")
    CH1DispName = "CO"
    CH2DispName = "NOx"
    CH3DispName = "O2"
    CH4DispName = "Dust"
    CH5DispName = "Temp 1"
    CH6DispName = "Temp 2"
    CH7DispName = "None"
    CH8DispName = "None"
    CH1MinAlarm = 0
    CH2MinAlarm = 0
    CH3MinAlarm = 0
    CH4MinAlarm = 0
    CH5MinAlarm = 0
    CH6MinAlarm = 0
    CH7MinAlarm = 0
    CH8MinAlarm = 0
    CH1MaxAlarm = 100
    CH2MaxAlarm = 100
    CH3MaxAlarm = 100
    CH4MaxAlarm = 100
    CH5MaxAlarm = 100
    CH6MaxAlarm = 100
    CH7MaxAlarm = 100
    CH8MaxAlarm = 100
    Ch1MinAlOn = 0
    Ch2MinAlOn = 0
    Ch3MinAlOn = 0
    Ch4MinAlOn = 0
    Ch5MinAlOn = 0
    Ch6MinAlOn = 0
    Ch7MinAlOn = 0
    Ch8MinAlOn = 0
    Ch1MaxAlOn = 0
    Ch2MaxAlOn = 0
    Ch3MaxAlOn = 0
    Ch4MaxAlOn = 0
    Ch5MaxAlOn = 0
    Ch6MaxAlOn = 0
    Ch7MaxAlOn = 0
    Ch8MaxAlOn = 0
    Ch1Active = 1
    Ch2Active = 1
    Ch3Active = 1
    Ch4Active = 1
    Ch5Active = 1
    Ch6Active = 1
    Ch7Active = 1
    Ch8Active = 1
    Daily_Files = 1
    Monthly_Files = 0
    CH14mA = 0
    CH120mA = 100
    CH24mA = 0
    CH220mA = 100
    CH34mA = 0
    CH320mA = 100
    CH44mA = 0
    CH420mA = 100
    CH54mA = 0
    CH520mA = 100
    CH64mA = 0
    CH620mA = 100
    CH74mA = 0
    CH720mA = 100
    CH84mA = 0
    CH820mA = 100
    Ave_time = 60
    CH1Offset = -5.02
    CH1Slope = 0.002
    CH2Offset = -5.02
    CH2Slope = 0.002
    CH3Offset = -5.02
    CH3Slope = 0.002
    CH4Offset = -5.02
    CH4Slope = 0.002
    CH5Offset = -5.02
    CH5Slope = 0.002
    CH6Offset = -5.02
    CH6Slope = 0.002
    CH7Offset = -5.02
    CH7Slope = 0.002
    CH8Offset = -5.02
    CH8Slope = 0.002
    XMin = 0
    XMax = 60
    YMin = 0 
    YMax = 100
    O21Correct = "Y"
    O22Correct = "Y"
    O23Correct = "Y"
    O24Correct = "Y"
    O25Correct = "Y"
    O26Correct = "Y"
    O27Correct = "Y"
    O28Correct = "Y"
    O2Ref = 3
    Ch1Units = "mg/m3"
    Ch2Units = "mg/m3"
    Ch3Units = "mg/m3"
    Ch4Units = "mg/m3"
    Ch5Units = "mg/m3"
    Ch6Units = "mg/m3"
    Ch7Units = "mg/m3"
    Slave_ID = 1
    Modbus_Baud = 9600
    Modbus_Bits = 8
    Modbus_Parity = 0
    Modbus_StopBits = 1
    Modbus_Timeout = 1
    Ch1Mod = 0
    Ch2Mod = 0
    Ch3Mod = 0
    Ch4Mod = 0
    Ch5Mod = 0
    Ch6Mod = 0
    Ch7Mod = 0
    Ch8Mod = 0
    Chk_Status = 1
    Run_If_Temp = 50
    Dwell_Time = 90
    Meas_Time = 5
    Purge_Time = 4
    DataHold = Purge_Time + 2
    Use_Stdby = 1
    User_Pass = "0000"
    Address_1 = "1 High Street"
    Address_2 = "Eccleshall"
    Address_3 = "Staffordshire"
    Post_Code = "ST1 1ST"
    Permit_No = "AB1234YZ"
    Site_Contact = "Bob Smith"
    Plant_ID = "Gen Set 1"
    
    FileName = SavePath + 'MCP_config.data'
    dataset = [Chk_Status, Run_If_Temp, Use_Stdby, User_Pass, Address_1, Address_2, Address_3, Post_Code, Permit_No, Site_Contact, Plant_ID, Dwell_Time, Meas_Time, Purge_Time]
    fw = open(FileName, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
    
    FileName = SavePath + 'config.data'
    dataset = [CH1DispName, CH2DispName, CH3DispName, CH4DispName, CH5DispName, CH6DispName, CH7DispName, CH8DispName, CH1MinAlarm, CH2MinAlarm, CH3MinAlarm, CH4MinAlarm, CH5MinAlarm, CH6MinAlarm, CH7MinAlarm, CH8MinAlarm, CH1MaxAlarm, CH2MaxAlarm, CH3MaxAlarm, CH4MaxAlarm, CH5MaxAlarm, CH6MaxAlarm, CH7MaxAlarm, CH8MaxAlarm, Ch1MinAlOn, Ch2MinAlOn, Ch3MinAlOn, Ch4MinAlOn, Ch5MinAlOn, Ch6MinAlOn, Ch7MinAlOn, Ch8MinAlOn, Ch1MaxAlOn, Ch2MaxAlOn, Ch3MaxAlOn, Ch4MaxAlOn, Ch5MaxAlOn, Ch6MaxAlOn, Ch7MaxAlOn, Ch8MaxAlOn, Slave_ID, Modbus_Baud, Modbus_Bits, Modbus_Parity, Modbus_StopBits, Modbus_Timeout]
    fw = open(FileName, 'wb')
    pickle.dump(dataset, fw)
    fw.close()
    
    FileName = SavePath + 'settings.data'
    dataset2 = [Ch1Active, Ch2Active, Ch3Active, Ch4Active, Ch5Active, Ch6Active, Ch7Active, Ch8Active, Daily_Files, Monthly_Files, CH14mA, CH120mA, CH24mA, CH220mA, CH34mA, CH320mA, CH44mA, CH420mA, CH54mA, CH520mA, CH64mA, CH620mA, CH74mA, CH720mA, CH84mA, CH820mA, Ave_time, XMin, XMax, YMin, YMax, O21Correct, O22Correct, O23Correct, O24Correct, O25Correct, O26Correct, O27Correct, O28Correct, O2Ref, Ch1Units, Ch2Units, Ch3Units, Ch4Units, Ch5Units, Ch6Units, Ch7Units, Ch8Units, Ch1Mod, Ch2Mod, Ch3Mod, Ch4Mod, Ch5Mod, Ch6Mod, Ch7Mod, Ch8Mod]
    fw = open(FileName, 'wb')
    pickle.dump(dataset2, fw)
    fw.close()
    
    FileName = SavePath + 'cal.data'
    dataset3 = [CH1Offset, CH1Slope, CH2Offset, CH2Slope, CH3Offset, CH3Slope, CH4Offset, CH4Slope, CH5Offset, CH5Slope, CH6Offset, CH6Slope,CH7Offset, CH7Slope, CH8Offset, CH8Slope]
    fw = open(FileName, 'wb')
    pickle.dump(dataset3, fw)
    fw.close()
    
# only uncomment the row below to create new default config and settings files
#CreateDefault()

FileName = SavePath + 'MCP_config.data'
if os.path.getsize(FileName) == 0:
    # config file is empty, create a new one from defuaults
    print("creating default settings")
    CreateDefault()
else:
    fd = open(FileName, 'rb')
    dataset = pickle.load(fd)
    fd.close()
    
    Chk_Status = dataset[0]
    Run_If_Temp = dataset[1]
    Use_Stdby = dataset[2]
    User_Pass = dataset[3]
    Address_1 = dataset[4]
    Address_2 = dataset[5]
    Address_3 = dataset[6]
    Post_Code = dataset[7] 
    Permit_No = dataset[8]
    Site_Contact = dataset[9]
    Plant_ID = dataset[10]
    Dwell_Time = dataset[11]
    Meas_Time = dataset[12]
    Purge_Time = dataset[13]
    DataHold = int(Purge_Time) + 2
    

FileName = SavePath + 'cal.data'
if os.path.getsize(FileName) == 0:
    # config file is empty, create a new one from defuaults
    print("creating default settings")
    CreateDefault()
else:
    fd = open(FileName, 'rb')
    dataset = pickle.load(fd)
    fd.close()
    
    CH1Offset = (dataset[0])
    CH1Slope = (dataset[1])
    CH2Offset = (dataset[2])
    CH2Slope = (dataset[3])
    CH3Offset = (dataset[4])
    CH3Slope = (dataset[5])
    CH4Offset = (dataset[6])
    CH4Slope = (dataset[7])
    CH5Offset = (dataset[8])
    CH5Slope = (dataset[9])
    CH6Offset = (dataset[10])
    CH6Slope = (dataset[11])
    CH7Offset = (dataset[12])
    CH7Slope = (dataset[13])
    CH8Offset = (dataset[14])
    CH8Slope = (dataset[15])

    #print(CH1Offset)
    #print(CH1Slope)
    #print(CH3Offset)
    #print(CH3Slope)
    

FileName = SavePath + 'config.data'
if os.path.getsize(FileName) == 0:
    # config file is empty, create a new one from defuaults
    print("creating default config file")
    CreateDefault()
else:
    fd = open(FileName, 'rb')
    dataset = pickle.load(fd)
    fd.close()
    CH1DispName = (dataset[0])
    CH2DispName = (dataset[1])
    CH3DispName = (dataset[2])
    CH4DispName = (dataset[3])
    CH5DispName = (dataset[4])
    CH6DispName = (dataset[5])
    CH7DispName = (dataset[6])
    CH8DispName = (dataset[7])
    CH1MinAlarm = (dataset[8])
    CH2MinAlarm = (dataset[9])
    CH3MinAlarm = (dataset[10])
    CH4MinAlarm = (dataset[11])
    CH5MinAlarm = (dataset[12])
    CH6MinAlarm = (dataset[13])
    CH7MinAlarm = (dataset[14])
    CH8MinAlarm = (dataset[15])
    CH1MaxAlarm = (dataset[16])
    CH2MaxAlarm = (dataset[17])
    CH3MaxAlarm = (dataset[18])
    CH4MaxAlarm = (dataset[19])
    CH5MaxAlarm = (dataset[20])
    CH6MaxAlarm = (dataset[21])
    CH7MaxAlarm = (dataset[22])
    CH8MaxAlarm = (dataset[23])
    Ch1MinAlOn = (dataset[24])
    Ch2MinAlOn = (dataset[25])
    Ch3MinAlOn = (dataset[26])
    Ch4MinAlOn = (dataset[27])
    Ch5MinAlOn = (dataset[28])
    Ch6MinAlOn = (dataset[29])
    Ch7MinAlOn = (dataset[30])
    Ch8MinAlOn = (dataset[31])
    Ch1MaxAlOn = (dataset[32])
    Ch2MaxAlOn = (dataset[33])
    Ch3MaxAlOn = (dataset[34])
    Ch4MaxAlOn = (dataset[35])
    Ch5MaxAlOn = (dataset[36])
    Ch6MaxAlOn = (dataset[37])
    Ch7MaxAlOn = (dataset[38])
    Ch8MaxAlOn = (dataset[39])
    Slave_ID = (dataset[40])
    Modbus_Baud = int((dataset[41]))
    Modbus_Bits = int((dataset[42]))
    Modbus_Parity = int((dataset[43]))
    Modbus_StopBits = int((dataset[44]))
    Modbus_Timeout = int((dataset[45]))

    
FileName = SavePath + 'settings.data'
if os.path.getsize(FileName) == 0:
    # config file is empty, create a new one from defuaults
    print("creating default settings")
    CreateDefault()
else:
    fd = open(FileName, 'rb')
    dataset = pickle.load(fd)
    fd.close()
    
    Ch1Active = (dataset[0])
    Ch2Active = (dataset[1])
    Ch3Active = (dataset[2])
    Ch4Active = (dataset[3])
    Ch5Active = (dataset[4])
    Ch6Active = (dataset[5])
    Ch7Active = (dataset[6])
    Ch8Active = (dataset[7])
    Daily_Files = (dataset[8])
    Monthly_Files = (dataset[9])
    CH14mA = (dataset[10])
    CH120mA = (dataset[11])
    CH24mA = (dataset[12])
    CH220mA = (dataset[13])
    CH34mA = (dataset[14])
    CH320mA = (dataset[15])
    CH44mA = (dataset[16])
    CH420mA = (dataset[17])
    CH54mA = (dataset[18])
    CH520mA = (dataset[19])
    CH64mA = (dataset[20])
    CH620mA = (dataset[21])
    CH74mA = (dataset[22])
    CH720mA = (dataset[23])
    CH84mA = (dataset[24])
    CH820mA = (dataset[25])
    Ave_time = (dataset[26])
    XMin = (dataset[27])
    XMax = (dataset[28])
    YMin = (dataset[29])
    YMax = (dataset[30])
    O21Correct = (dataset[31])
    O22Correct = (dataset[32])
    O23Correct = (dataset[33])
    O24Correct = (dataset[34])
    O25Correct = (dataset[35])
    O26Correct = (dataset[36])
    O27Correct = (dataset[37])
    O28Correct = (dataset[38])
    O2Ref = (dataset[39])
    O2Ref = (dataset[39])
    Ch1Units = (dataset[40])
    Ch2Units = (dataset[41])
    Ch3Units = (dataset[42])
    Ch4Units = (dataset[43])
    Ch5Units = (dataset[44])
    Ch6Units = (dataset[45])
    Ch7Units = (dataset[46])
    Ch8Units = (dataset[47])
    Ch1Mod = (dataset[48])
    Ch2Mod = (dataset[49])
    Ch3Mod = (dataset[50])
    Ch4Mod = (dataset[51])
    Ch5Mod = (dataset[52])
    Ch6Mod = (dataset[53])
    Ch7Mod = (dataset[54])
    Ch8Mod = (dataset[55])

def ClearGraph():
    global PlotSecs
    global FirstRound
    global TimeList
    global Data1List
    global Data2List
    global Data3List
    global Data4List
    global Data5List
    global Data6List
    global Data7List
    global Data8List
    global CycleSoFar

    PlotSecs = 0
    FirstRound = 0
    TimeList.clear()
    Data1List.clear()
    Data2List.clear()
    Data3List.clear()
    Data4List.clear()
    Data5List.clear()
    Data6List.clear()
    Data7List.clear()
    Data8List.clear()
    CycleSoFar = 0

def updating_writer(a):
    global context
    # a worker process that runs every so often to update live values on RTU modbus server
    #context = a[0]
    FunctionCode = 3
    This_ID = int(Slave_ID)
    slave_id = This_ID
    #0x01
    address = 0x10
    Register3 = 0x06

    context[slave_id].setValues(FunctionCode,Register3 , [0x66])
    #print("updated with initial data")

def run_update_Modbus_Server():
    global context
    global ModServer
    global Slave_ID
    global Modbus_Baud
    global Modbus_Bits
    global Modbus_Parity
    global Modbus_StopBits
    global Modbus_Timeout
    
    #Slave_ID = 1
    #Modbus_Baud = 9600
    #Modbus_Bits = 8
    #Modbus_Parity = 0
    #Modbus_StopBits = 1
    #Modbus_Timeout = 1
    
    ##This_ID = int(Slave_ID)
    ##addresses = [This_ID]
    ##slaves = {}
    #for adress in addresses:
    ##store = ModbusSlaveContext(zero_mode=True)
    ##slaves.update({This_ID: store})

    # initialize the server information
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'DRM_Technic'
    identity.ProductCode = 'MCP'
    identity.VendorUrl = 'https://www.drmtechnic.com/'
    identity.ProductName = 'DRM Modbus Server'
    identity.ModelName = 'Modbus Server'
    identity.MajorMinorRevision = '1.1.3'

    #updating_writer(context)
    ##This_ID = int(Slave_ID)
    ##addresses = [This_ID]
    ##slaves = {}
    #for adress in addresses:
    ##store = ModbusSlaveContext(zero_mode=True)
    ##slaves.update({This_ID: store})

    print("RTU Server Initialising in separate Thread - named ModServer")
    
    Modbus_Timout = int(Modbus_Timeout) / 10000
    #Modbus_Timout = 0.0001
    print("Modbus Timeout"+str(Modbus_Timout))
    if Modbus_Parity == 0:
        Mod_Parity = 'N'
    elif Modbus_Parity == 1:
        Mod_Parity = 'O'
    else:
        Mod_Parity = 'E'
    args=(context, identity)
    kwargs={"framer": ModbusRtuFramer,"port":"/dev/ttySC0","timeout":Modbus_Timout,"baudrate":Modbus_Baud,"parity":Mod_Parity,"bytesize":Modbus_Bits,"stopbits":Modbus_StopBits,"ignore_missing_slaves":True}
    #time.sleep(1)
    #print("Start Server")
    #StartSerialServer(
    #    context=context,
    #    framer=ModbusRtuFramer,
    #    identity=identity,
    #    port="/dev/ttySC0",
    #    timeout=0.0001,
    #    baudrate=9600,
    #    parity='N',
    #    bytesize=8,
    #    stopbits=1,
    #    ignore_missing_slaves=True)
    #time.sleep(1)
    #print("Stop Server")
    #server.ServerStop()
    #time.sleep(1)
    #print("Start Server again")
    time.sleep(2)
    ModServer = Thread(target=StartSerialServer, args=args, kwargs=kwargs )
    time.sleep(2)
    ModServer.start()

if Slave_ID != 0:
    global context
    global This_ID
    global addresses
    global slaves
    global store
    # Create a single Modbus context ready for use
    #print("SLave ID")
    #print(Slave_ID)
    This_ID = int(Slave_ID)
    addresses = [This_ID]
    slaves = {}
    #for adress in addresses:
    store = ModbusSlaveContext(zero_mode=True)
    slaves.update({This_ID: store})
    context = ModbusServerContext(slaves=slaves, single=False)
    time.sleep(2)
    ser = serial.Serial('/dev/ttySC0', 115200, timeout=0.050)
    # count = 0
    ser.write(0b00)
    time.sleep(2)
    run_update_Modbus_Server()
    
def AFunction():
    return

def SilenceAlarms():
    global AlarmSilent
    if ButtonF['relief']=="raised":            
        AlarmSilent = 1
        if UseRelays == 1:
            relay_off(1)
        ButtonF['relief']="sunken"
        ButtonF['image'] = AlarmOnImage
    else:
        AlarmSilent = 0
        if UseRelays == 1:
            #print(" ")
            if RunOn == 0:
                relay_on(1)
        ButtonF['relief']="raised"
        ButtonF['image'] = AlarmOffImage
        


def SettingsClicked():
    SettingsWindow = Toplevel(root)
    SettingsWindow.title("SETTINGS")
    SettingsWindow.geometry('600x400')
    global Ch1Active
    global Ch2Active
    global Ch3Active
    global Ch4Active
    global Ch5Active
    global Ch6Active
    global Ch7Active
    global Ch8Active
    global Daily_Files
    global Monthly_Files
    global CH14mA
    global CH120mA
    global CH24mA
    global CH220mA
    global CH34mA
    global CH320mA
    global CH44mA
    global CH420mA
    global CH54mA
    global CH520mA
    global CH64mA
    global CH620mA
    global CH74mA
    global CH720mA
    global CH84mA
    global CH820mA
    global Ave_time
    global CH1DispName
    global CH2DispName
    global CH3DispName
    global CH4DispName
    global CH5DispName
    global CH6DispName
    global CH7DispName
    global CH8DispName
    global CH1_Name
    global CH2_Name
    global CH3_Name
    global CH4_Name
    global CH5_Name
    global CH6_Name
    global CH7_Name
    global CH8_Name
    global ButtonColour
    global CH1Offset
    global CH1Slope
    global CH2Offset
    global CH2Slope
    global CH3Offset
    global CH3Slope
    global CH4Offset
    global CH4Slope
    global CH5Offset
    global CH5Slope
    global CH6Offset
    global CH6Slope
    global CH7Offset
    global CH7Slope
    global CH8Offset
    global CH8Slope
    global XMin
    global XMax
    global YMin
    global YMax
    global O21Correct
    global O22Correct
    global O23Correct
    global O24Correct
    global O25Correct
    global O26Correct
    global O27Correct
    global O28Correct
    global O2Ref
    global Ch1Units
    global Ch2Units
    global Ch3Units
    global Ch4Units
    global Ch5Units
    global Ch6Units
    global Ch7Units
    global Ch8Units
    global SavePath
    global Ch1Mod
    global Ch2Mod
    global Ch3Mod
    global Ch4Mod
    global Ch5Mod
    global Ch6Mod
    global Ch7Mod
    global Ch8Mod
    global client
    global Chk_Status
    global Run_If_Temp
    global Use_Stdby
    global User_Pass
    global Dwell_Time
    global Meas_Time
    global Purge_Time
    global Modbus_Baud
    global Modbus_Bits
    global Modbus_Parity
    global Modbus_StopBits
    global Modbus_Timeout
    
    def CalInputs():
        global Cal_Running
        global SavePath
        SettingsWindow.destroy()
        Cal_Running = 1
        Temp1 = 0
        Temp2 = 0
        Temp3 = 0
        Temp4 = 0
        Temp5 = 0
        Temp6 = 0
        Temp7 = 0
        Temp8 = 0
        
        def task2():
            global Cal_Running
            if Cal_Running == 1:
                root.after(2000, task2)
            # Read all the ADC channel values in a list.
            values = [0]*4
            GAIN = 1
            for i in range(4):
                values[i] = adc1.read_adc(i, gain=GAIN)
            #print('brd1| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
            Ch1Current['text'] = int('{0:>6}'.format(*values))
            Ch2Current['text'] = int('{1:>6}'.format(*values))
            Ch3Current['text'] = int('{2:>6}'.format(*values))
            Ch4Current['text'] = int('{3:>6}'.format(*values))
            # Pause for half a second.
            time.sleep(0.5)
            values2 = [0]*4
            if FTBoards_Installed == 2:
                for j in range(4):
                    values2[j] = adc2.read_adc(j, gain=GAIN)
                #print('brd2| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values2))
                Ch5Current['text'] = int('{0:>6}'.format(*values2))
                Ch6Current['text'] = int('{1:>6}'.format(*values2))
                Ch7Current['text'] = int('{2:>6}'.format(*values2))
                Ch8Current['text'] = int('{3:>6}'.format(*values2))
                # Pause for half a second.
            else:
                Ch5Current['text'] = 0
                Ch6Current['text'] = 0
                Ch7Current['text'] = 0
                Ch8Current['text'] = 0
            time.sleep(0.5)
            if Cal_Running == 0:
                CalWindow.destroy()
            
        def Close_Cal():
            global Cal_Running
            global CH1Offset
            global CH1Slope
            global CH2Offset
            global CH2Slope
            global CH3Offset
            global CH3Slope
            global CH4Offset
            global CH4Slope
            global CH5Offset
            global CH5Slope
            global CH6Offset
            global CH6Slope
            global CH7Offset
            global CH7Slope
            global CH8Offset
            global CH8Slope
            global SavePath
            Close_Button["state"] = "disabled"
            # save all calibrations to file
            FileName = SavePath + 'cal.data'
            dataset3 = [CH1Offset, CH1Slope, CH2Offset, CH2Slope, CH3Offset, CH3Slope, CH4Offset, CH4Slope, CH5Offset, CH5Slope, CH6Offset, CH6Slope,CH7Offset, CH7Slope, CH8Offset, CH8Slope]
            fw = open(FileName, 'wb')
            pickle.dump(dataset3, fw)
            fw.close()
            Cal_Running = 0
        
        def Cal1Min():
            global Temp1
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp1 = Ch1Current['text']
                Cal1_Max_Button["state"] = "normal"
        
        def Cal1Max():
            global CH1Offset
            global CH1Slope
            global Temp1
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch1Current['text'])-float(Temp1))
                c = (m*(0-float(Temp1)))+float(4)
                CH1Offset = c
                CH1Slope = m

        def Cal2Min():
            global Temp2
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp2 = Ch2Current['text']
                Cal2_Max_Button["state"] = "normal"
        
        def Cal2Max():
            global CH2Offset
            global CH2Slope
            global Temp2
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch2Current['text'])-float(Temp2))
                c = (m*(0-float(Temp2)))+float(4)
                CH2Offset = c
                CH2Slope = m


        def Cal3Min():
            global Temp3
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp3 = Ch3Current['text']
                Cal3_Max_Button["state"] = "normal"
        
        def Cal3Max():
            global CH3Offset
            global CH3Slope
            global Temp3
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch3Current['text'])-float(Temp3))
                c = (m*(0-float(Temp3)))+float(4)
                CH3Offset = c
                CH3Slope = m
                
        def Cal4Min():
            global Temp4
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp4 = Ch4Current['text']
                Cal4_Max_Button["state"] = "normal"
        
        def Cal4Max():
            global CH4Offset
            global CH4Slope
            global Temp4
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch4Current['text'])-float(Temp4))
                c = (m*(0-float(Temp4)))+float(4)
                CH4Offset = c
                CH4Slope = m
                
        def Cal5Min():
            global Temp5
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp5 = Ch5Current['text']
                Cal5_Max_Button["state"] = "normal"
        
        def Cal5Max():
            global CH5Offset
            global CH5Slope
            global Temp5
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch5Current['text'])-float(Temp5))
                c = (m*(0-float(Temp5)))+float(4)
                CH5Offset = c
                CH5Slope = m
                
        def Cal6Min():
            global Temp6
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp6 = Ch6Current['text']
                Cal6_Max_Button["state"] = "normal"
        
        def Cal6Max():
            global CH6Offset
            global CH6Slope#
            global Temp6
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch6Current['text'])-float(Temp6))
                c = (m*(0-float(Temp6)))+float(4)
                CH6Offset = c
                CH6Slope = m
                
        def Cal7Min():
            global Temp7
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp7 = Ch7Current['text']
                Cal7_Max_Button["state"] = "normal"
        
        def Cal7Max():
            global CH7Offset
            global CH7Slope
            global Temp7
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch7Current['text'])-float(Temp7))
                c = (m*(0-float(Temp7)))+float(4)
                CH7Offset = c
                CH7Slope = m
                
        def Cal8Min():
            global Temp8
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 4mA?")
            CalWindow.tkraise()
            if response == TRUE:
                Temp8 = Ch8Current['text']
                Cal8_Max_Button["state"] = "normal"
        
        def Cal8Max():
            global CH8Offset
            global CH8Slope
            global Temp8
            CalWindow.lower()
            response = messagebox.askokcancel("Please Confirm", "Store Current Raw value as 20mA?")
            CalWindow.tkraise()
            if response == TRUE:
                m = (float(20)-float(4))/(float(Ch8Current['text'])-float(Temp8))
                c = (m*(0-float(Temp8)))+float(4)
                CH8Offset = c
                CH8Slope = m
                
        CalWindow = Toplevel(root)
        CalWindow.title("CALIBRATE 4-20mA INPUTS")
        global CH1Offset
        global CH1Slope
        global CH2Offset
        global CH2Slope
        global CH3Offset
        global CH3Slope
        global CH4Offset
        global CH4Slope
        global CH5Offset
        global CH5Slope
        global CH6Offset
        global CH6Slope
        global CH7Offset
        global CH7Slope
        global CH8Offset
        global CH8Slope

        Frame1 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame1.pack(expand=True, side=TOP, fill=BOTH)
        Frame2 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame2.pack(expand=True, side=TOP, fill=BOTH)
        Frame3 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame3.pack(expand=True, side=TOP, fill=BOTH)
        Frame4 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame4.pack(expand=True, side=TOP, fill=BOTH)
        Frame5 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame5.pack(expand=True, side=TOP, fill=BOTH)
        Frame6 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame6.pack(expand=True, side=TOP, fill=BOTH)
        Frame7 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame7.pack(expand=True, side=TOP, fill=BOTH)
        Frame8 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame8.pack(expand=True, side=TOP, fill=BOTH)
        Frame9 = Frame(CalWindow, bd=2, padx=10, pady=1, relief=FLAT)
        Frame9.pack(expand=True, side=TOP, fill=BOTH)
        
        #Frame1    
        Label1 = Label(Frame1, text="Channel 1", padx=10,)
        Label1.pack(side=LEFT)
        Label2 = Label(Frame1, text="Raw reading -", padx=10,)
        Label2.pack(side=LEFT)
        Ch1Current = Label(Frame1, text="##", width = 8, padx=10,)
        Ch1Current.pack(side=LEFT)
        Cal1_Min_Button = Button(Frame1, text="Calilbrate 4mA", padx=10, pady=10, command=Cal1Min, bg=ButtonColour)
        Cal1_Min_Button.pack(side=LEFT)
        Cal1_Max_Button = Button(Frame1, text="Calilbrate 20mA", padx=10, pady=10, command=Cal1Max, bg=ButtonColour)
        Cal1_Max_Button.pack(side=LEFT)
        
            #Frame2    
        Label3 = Label(Frame2, text="Channel 2", padx=10,)
        Label3.pack(side=LEFT)
        Label4 = Label(Frame2, text="Raw reading -", padx=10,)
        Label4.pack(side=LEFT)
        Ch2Current = Label(Frame2, text="##", width = 8, padx=10,)
        Ch2Current.pack(side=LEFT)
        Cal2_Min_Button = Button(Frame2, text="Calilbrate 4mA", padx=10, pady=10, command=Cal2Min, bg=ButtonColour)
        Cal2_Min_Button.pack(side=LEFT)
        Cal2_Max_Button = Button(Frame2, text="Calilbrate 20mA", padx=10, pady=10, command=Cal2Max, bg=ButtonColour)
        Cal2_Max_Button.pack(side=LEFT)
        
            #Frame3
        Label5 = Label(Frame3, text="Channel 3", padx=10,)
        Label5.pack(side=LEFT)
        Label6 = Label(Frame3, text="Raw reading -", padx=10,)
        Label6.pack(side=LEFT)
        Ch3Current = Label(Frame3, text="##", width = 8, padx=10,)
        Ch3Current.pack(side=LEFT)
        Cal3_Min_Button = Button(Frame3, text="Calilbrate 4mA", padx=10, pady=10, command=Cal3Min, bg=ButtonColour)
        Cal3_Min_Button.pack(side=LEFT)
        Cal3_Max_Button = Button(Frame3, text="Calilbrate 20mA", padx=10, pady=10, command=Cal3Max, bg=ButtonColour)
        Cal3_Max_Button.pack(side=LEFT)
        
            #Frame4
        Label7 = Label(Frame4, text="Channel 4", padx=10,)
        Label7.pack(side=LEFT)
        Label8 = Label(Frame4, text="Raw reading -", padx=10,)
        Label8.pack(side=LEFT)
        Ch4Current = Label(Frame4, text="##", width = 8, padx=10,)
        Ch4Current.pack(side=LEFT)
        Cal4_Min_Button = Button(Frame4, text="Calilbrate 4mA", padx=10, pady=10, command=Cal4Min, bg=ButtonColour)
        Cal4_Min_Button.pack(side=LEFT)
        Cal4_Max_Button = Button(Frame4, text="Calilbrate 20mA", padx=10, pady=10, command=Cal4Max, bg=ButtonColour)
        Cal4_Max_Button.pack(side=LEFT)
        
            #Frame5    
        Label9 = Label(Frame5, text="Channel 5", padx=10,)
        Label9.pack(side=LEFT)
        Label10 = Label(Frame5, text="Raw reading -", padx=10,)
        Label10.pack(side=LEFT)
        Ch5Current = Label(Frame5, text="##", width = 8, padx=10,)
        Ch5Current.pack(side=LEFT)
        Cal5_Min_Button = Button(Frame5, text="Calilbrate 4mA", padx=10, pady=10, command=Cal5Min, bg=ButtonColour)
        Cal5_Min_Button.pack(side=LEFT)
        Cal5_Max_Button = Button(Frame5, text="Calilbrate 20mA", padx=10, pady=10, command=Cal5Max, bg=ButtonColour)
        Cal5_Max_Button.pack(side=LEFT)
        
            #Frame6
        Label11 = Label(Frame6, text="Channel 6", padx=10,)
        Label11.pack(side=LEFT)
        Label12 = Label(Frame6, text="Raw reading -", padx=10,)
        Label12.pack(side=LEFT)
        Ch6Current = Label(Frame6, text="##", width = 8, padx=10,)
        Ch6Current.pack(side=LEFT)
        Cal6_Min_Button = Button(Frame6, text="Calilbrate 4mA", padx=10, pady=10, command=Cal6Min, bg=ButtonColour)
        Cal6_Min_Button.pack(side=LEFT)
        Cal6_Max_Button = Button(Frame6, text="Calilbrate 20mA", padx=10, pady=10, command=Cal6Max, bg=ButtonColour)
        Cal6_Max_Button.pack(side=LEFT)
        
            #Frame7
        Label13 = Label(Frame7, text="Channel 7", padx=10,)
        Label13.pack(side=LEFT)
        Label14 = Label(Frame7, text="Raw reading -", padx=10,)
        Label14.pack(side=LEFT)
        Ch7Current = Label(Frame7, text="##", width = 8, padx=10,)
        Ch7Current.pack(side=LEFT)
        Cal7_Min_Button = Button(Frame7, text="Calilbrate 4mA", padx=10, pady=10, command=Cal7Min, bg=ButtonColour)
        Cal7_Min_Button.pack(side=LEFT)
        Cal7_Max_Button = Button(Frame7, text="Calilbrate 20mA", padx=10, pady=10, command=Cal7Max, bg=ButtonColour)
        Cal7_Max_Button.pack(side=LEFT)
        
            #Frame8    
        Label15 = Label(Frame8, text="Channel 8", padx=10,)
        Label15.pack(side=LEFT)
        Label16 = Label(Frame8, text="Raw reading -", padx=10,)
        Label16.pack(side=LEFT)
        Ch8Current = Label(Frame8, text="##", width = 8, padx=10,)
        Ch8Current.pack(side=LEFT)
        Cal8_Min_Button = Button(Frame8, text="Calilbrate 4mA", padx=10, pady=10, command=Cal8Min, bg=ButtonColour)
        Cal8_Min_Button.pack(side=LEFT)
        Cal8_Max_Button = Button(Frame8, text="Calilbrate 20mA", padx=10, pady=10, command=Cal8Max, bg=ButtonColour)
        Cal8_Max_Button.pack(side=LEFT)
            
            #Frame9
        Close_Button = Button(Frame9, text="Done", padx=10, pady=10, command=Close_Cal, bg=ButtonColour)
        Close_Button.pack(side=LEFT)
        Close_Button["state"] = "normal"
        
        #disable 20mA cal button until zero has been calibrated
        Cal1_Max_Button["state"] = "disabled"
        Cal2_Max_Button["state"] = "disabled"
        Cal3_Max_Button["state"] = "disabled"
        Cal4_Max_Button["state"] = "disabled"
        Cal5_Max_Button["state"] = "disabled"
        Cal6_Max_Button["state"] = "disabled"
        Cal7_Max_Button["state"] = "disabled"
        Cal8_Max_Button["state"] = "disabled"
        
        task2()
    
    
    
    def SetClock():
        SettingsWindow.destroy()
        MyFont=("Arial", 16)

        def SaveClock():
            # what to do when 'Save' clicked
            TheYear = DTYear.get()
            AsText = TheYear+"-"+DTMonth.get()+"-"+DTDay.get()+" "+DTHour.get()+":"+DTMin.get()+":"+DTSec.get()
            print(AsText)
            call("sudo date -s '"+AsText+"'", shell=True)
            call("sudo hwclock -w", shell=True)
            ClockWindow.destroy()

        ClockWindow = Toplevel(root)
        ClockWindow.title("Set Date and Time")

        # Create an initial startup window
        ClockFrame = Frame(ClockWindow, bd=2, padx=1, pady=1, relief=SUNKEN)
        ClockFrame.pack(side=TOP, fill=X)
        # create a frame within the window
        Frame1 = Frame(ClockFrame, bd=2, padx=10, pady=1, relief=SUNKEN)
        Frame1.pack(expand=True, side=TOP, fill=BOTH)

        Frame2 = Frame(ClockFrame, bd=2, padx=10, pady=1, relief=SUNKEN)
        Frame2.pack(expand=True, side=TOP, fill=BOTH)

        Frame3 = Frame(ClockFrame, bd=2, padx=10, pady=1, relief=SUNKEN)
        Frame3.pack(expand=True, side=TOP, fill=BOTH)

        #Contents of Frame1
        DTTitleLabel = Label(Frame1, text="Year / Month / Day  -  Hours : Minutes : Seconds", padx=10, pady=1, font=(MyFont))
        DTTitleLabel.pack(side=LEFT)

        DTYear = Entry(Frame2, width=5, font=(MyFont))
        DTYear.pack(side=LEFT, fill=BOTH)
        DTYear.bind("<1>", (lambda event: NumPad(DTYear)))
        DTYear.insert(0,str("2022"))

        DTLine = Label(Frame2, text="/", padx=10, pady=1, font=(MyFont))
        DTLine.pack(side=LEFT)

        DTMonth = Entry(Frame2, width=3, font=(MyFont))
        DTMonth.pack(side=LEFT, fill=BOTH)
        DTMonth.bind("<1>", (lambda event: NumPad(DTMonth)))
        DTMonth.insert(0,str("10"))

        DTLine = Label(Frame2, text="/", padx=10, pady=1, font=(MyFont))
        DTLine.pack(side=LEFT)

        DTDay = Entry(Frame2, width=3, font=(MyFont))
        DTDay.pack(side=LEFT, fill=BOTH)
        DTDay.bind("<1>", (lambda event: NumPad(DTDay)))
        DTDay.insert(0,str("16"))

        DTGap = Label(Frame2, text=" - ", padx=10, pady=1, font=(MyFont))
        DTGap.pack(side=LEFT)

        DTHour = Entry(Frame2, width=3, font=(MyFont))
        DTHour.pack(side=LEFT, fill=BOTH)
        DTHour.bind("<1>", (lambda event: NumPad(DTHour)))
        DTHour.insert(0,str("14"))

        DTColon = Label(Frame2, text=":", padx=10, pady=1, font=(MyFont))
        DTColon.pack(side=LEFT)

        DTMin = Entry(Frame2, width=3, font=(MyFont))
        DTMin.pack(side=LEFT, fill=BOTH)
        DTMin.bind("<1>", (lambda event: NumPad(DTMin)))
        DTMin.insert(0,str("00"))

        DTColon = Label(Frame2, text=":", padx=10, pady=1, font=(MyFont))
        DTColon.pack(side=LEFT)

        DTSec = Entry(Frame2, width=3, font=(MyFont))
        DTSec.pack(side=LEFT, fill=BOTH)
        DTSec.bind("<1>", (lambda event: NumPad(DTSec)))
        DTSec.insert(0,str("00"))

        SetTime = Button(Frame3, text="Save", wraplength=70, padx=5, pady=8, command=SaveClock, bg=ButtonColour)
        SetTime.pack( side = TOP, padx=4 )
    
    def SaveSettings():
        global Ch1Active
        global Ch2Active
        global Ch3Active
        global Ch4Active
        global Ch5Active
        global Ch6Active
        global Ch7Active
        global Ch8Active
        global Daily_Files
        global Monthly_Files
        global CH14mA
        global CH120mA
        global CH24mA
        global CH220mA
        global CH34mA
        global CH320mA
        global CH44mA
        global CH420mA
        global CH54mA
        global CH520mA
        global CH64mA
        global CH620mA
        global CH74mA
        global CH720mA
        global CH84mA
        global CH820mA
        global Ave_time
        global CH1DispName
        global CH1_Name
        global CH2DispName
        global CH2_Name
        global CH3DispName
        global CH3_Name
        global CH4DispName
        global CH4_Name
        global CH5DispName
        global CH5_Name
        global CH6DispName
        global CH6_Name
        global CH7DispName
        global CH7_Name
        global CH8DispName
        global CH8_Name
        global CH1Offset
        global CH1Slope
        global CH2Offset
        global CH2Slope
        global CH3Offset
        global CH3Slope
        global CH4Offset
        global CH4Slope
        global CH5Offset
        global CH5Slope
        global CH6Offset
        global CH6Slope
        global CH7Offset
        global CH7Slope
        global CH8Offset
        global CH8Slope
        global XMin
        global XMax
        global YMin
        global YMax
        global O21Correct
        global O22Correct
        global O23Correct
        global O24Correct
        global O25Correct
        global O26Correct
        global O27Correct
        global O28Correct
        global O2Ref
        global Ch1Units
        global Ch2Units
        global Ch3Units
        global Ch4Units
        global Ch5Units
        global Ch6Units
        global Ch7Units
        global Ch8Units
        global SavePath
        global Ch1Mod
        global Ch2Mod
        global Ch3Mod
        global Ch4Mod
        global Ch5Mod
        global Ch6Mod
        global Ch7Mod
        global Ch8Mod
        
        Ch1Active = var11.get()
        Ch2Active = var12.get()
        Ch3Active = var13.get()
        Ch4Active = var14.get()
        Ch5Active = var15.get()
        Ch6Active = var16.get()
        Ch7Active = var17.get()
        Ch8Active = var18.get()
        Daily_Files = var19.get()
        Monthly_Files = var20.get()
        if var21.get() == 1:
            O21Correct = "Y"    
        if var22.get() == 1:
            O22Correct = "Y"    
        if var23.get() == 1:
            O23Correct = "Y"    
        if var24.get() == 1:
            O24Correct = "Y"    
        if var25.get() == 1:
            O25Correct = "Y"    
        if var26.get() == 1:
            O26Correct = "Y"    
        if var27.get() == 1:
            O27Correct = "Y"    
        if var28.get() == 1:
            O28Correct = "Y"    
        
        # input error checking
        checked = 0
        try:
            value = int(CH14mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch1 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH14mA) < 999999 and int(CH14mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch1 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        try:
            value = int(CH24mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch2 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH24mA) < 999999 and int(CH24mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch2 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH34mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch3 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH34mA) < 999999 and int(CH34mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch3 4mA value >999999 or <0")
                SettingsWindow.tkraise()
                
        try:
            value = int(CH44mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch4 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH44mA) < 999999 and int(CH44mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch4 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH54mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch5 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH54mA) < 999999 and int(CH54mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch5 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH64mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch6 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH64mA) < 999999 and int(CH64mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch6 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH74mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch7 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH74mA) < 999999 and int(CH74mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch7 4mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH84mA)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch8 4mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH84mA) < 999999 and int(CH84mA) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch8 4mA value >999999 or <0")
                SettingsWindow.tkraise()
                
        try:
            value = int(CH1_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch1 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH1_20mA.get()) < 999999 and int(CH1_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch1 20mA value >999999 or <0")
                SettingsWindow.tkraise()
                
        try:
            value = int(CH2_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch2 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH2_20mA.get()) < 999999 and int(CH2_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch2 20mA value >999999 or <0")
                SettingsWindow.tkraise()
                
        try:
            value = int(CH3_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch3 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH3_20mA.get()) < 999999 and int(CH3_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch3 20mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH4_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch4 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH4_20mA.get()) < 999999 and int(CH4_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch4 20mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH5_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch5 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH5_20mA.get()) < 999999 and int(CH5_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch5 20mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH6_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch6 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH6_20mA.get()) < 999999 and int(CH6_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch6 20mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH7_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch7 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH7_20mA.get()) < 999999 and int(CH7_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch7 20mA value >999999 or <0")
                SettingsWindow.tkraise()
        
        try:
            value = int(CH8_20mA.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Ch8 20mA value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH8_20mA.get()) < 999999 and int(CH8_20mA.get()) > -0.1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Ch8 20mA value >999999 or <0")
                SettingsWindow.tkraise()
                
        try:
            value = int(CH1_Ave.get())
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Averaging time value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH1_Ave.get()) < 121 and int(CH1_Ave.get()) > 1:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Averaging time must be between 2 and 120")
                SettingsWindow.tkraise()

        if checked == 34:
            Zero= int("0")
            CH14mA = Zero
            CH120mA = int(CH1_20mA.get())
            CH24mA = Zero
            CH220mA = int(CH2_20mA.get())
            CH34mA = Zero
            CH320mA = int(CH3_20mA.get())
            CH44mA = Zero
            CH420mA = int(CH4_20mA.get())
            CH54mA = Zero
            CH520mA = int(CH5_20mA.get())
            CH64mA = Zero
            CH620mA = int(CH6_20mA.get())
            CH74mA = Zero
            CH720mA = int(CH7_20mA.get())
            CH84mA = Zero
            CH820mA = int(CH8_20mA.get())
            Ave_time = CH1_Ave.get()
            CH1DispName = CH1_Name.get()
            CH2DispName = CH2_Name.get()
            CH3DispName = CH3_Name.get()
            CH4DispName = CH4_Name.get()
            CH5DispName = CH5_Name.get()
            CH6DispName = CH6_Name.get()
            CH7DispName = CH7_Name.get()
            CH8DispName = CH8_Name.get()
            Ch1Active = var11.get()
            Ch2Active = var12.get()
            Ch3Active = var13.get()
            Ch4Active = var14.get()
            Ch5Active = var15.get()
            Ch6Active = var16.get()
            Ch7Active = var17.get()
            Ch8Active = var18.get()
            Ch1Mod = Mod1.get()
            Ch2Mod = Mod2.get()
            Ch3Mod = Mod3.get()
            Ch4Mod = Mod4.get()
            Ch5Mod = Mod5.get()
            Ch6Mod = Mod6.get()
            Ch7Mod = Mod7.get()
            Ch8Mod = Mod8.get()
            Daily_Files = var19.get()
            Monthly_Files = var20.get()
            if var21.get() == 1:
                O21Correct = "Y"
            else:
                O21Correct = "N"
            if var22.get() == 1:
                O22Correct = "Y"
            else:
                O22Correct = "N"
            if var23.get() == 1:
                O23Correct = "Y"
            else:
                O23Correct = "N"
            if var24.get() == 1:
                O24Correct = "Y"
            else:
                O24Correct = "N"
            if var25.get() == 1:
                O25Correct = "Y"
            else:
                O25Correct = "N"
            if var26.get() == 1:
                O26Correct = "Y"
            else:
                O26Correct = "N"
            if var27.get() == 1:
                O27Correct = "Y"
            else:
                O27Correct = "N"
            if var28.get() == 1:
                O28Correct = "Y"
            else:
                O28Correct = "N"
            
            O2Ref = O2_Ref.get()
            Ch1Units = Ch1_Units.get()
            Ch2Units = Ch2_Units.get()
            Ch3Units = Ch3_Units.get()
            Ch4Units = Ch4_Units.get()
            Ch5Units = Ch5_Units.get()
            Ch6Units = Ch6_Units.get()
            Ch7Units = Ch7_Units.get()
            Ch8Units = Ch8_Units.get()
            
            FileName = SavePath + 'settings.data'
            dataset2 = [Ch1Active, Ch2Active, Ch3Active, Ch4Active, Ch5Active, Ch6Active, Ch7Active, Ch8Active, Daily_Files, Monthly_Files, CH14mA, CH120mA, CH24mA, CH220mA, CH34mA, CH320mA, CH44mA, CH420mA, CH54mA, CH520mA, CH64mA, CH620mA, CH74mA, CH720mA, CH84mA, CH820mA, Ave_time, XMin, XMax, YMin, YMax, O21Correct, O22Correct, O23Correct, O24Correct, O25Correct, O26Correct, O27Correct, O28Correct, O2Ref, Ch1Units, Ch2Units, Ch3Units, Ch4Units, Ch5Units, Ch6Units, Ch7Units, Ch8Units, Ch1Mod, Ch2Mod, Ch3Mod, Ch4Mod, Ch5Mod, Ch6Mod, Ch7Mod, Ch8Mod]
            fw = open(FileName, 'wb')
            pickle.dump(dataset2, fw)
            fw.close()
                
            FileName = SavePath + 'config.data'
            fd = open(FileName, 'rb')
            newdataset = pickle.load(fd)
            fd.close()
            
            newdataset[0] = CH1DispName
            newdataset[1] = CH2DispName
            newdataset[2] = CH3DispName
            newdataset[3] = CH4DispName
            newdataset[4] = CH5DispName
            newdataset[5] = CH6DispName
            newdataset[6] = CH7DispName
            newdataset[7] = CH8DispName
            Outputdataset = newdataset
            fw = open(FileName, 'wb')
            pickle.dump(Outputdataset, fw)
            fw.close()
            SettingsWindow.lower()
            messagebox.showinfo("Please note", "System must be re-started for changes to take effect")
            SettingsWindow.tkraise()
            
            SettingsWindow.destroy()
    
    def CancelSettings():
        SettingsWindow.destroy()
    
    def NextPage():
        if SettingsWindow.title() == "Settings - Page 1":
            Page1.forget()
            Page2.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 2")
            # remove the 4 lines below to enable page 3
            Button3["state"]="normal"
            Button7["state"]="normal"
            Button4["state"]="normal"
            Button8["state"]="normal"
        elif SettingsWindow.title() == "Settings - Page 2":
            # code below only required for page 3
            Page2.forget()
            Page3.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 3")
            Button3["state"]="normal"
            Button7["state"]="normal"
            Button4["state"]="normal"
            Button8["state"]="normal"
        elif SettingsWindow.title() == "Settings - Page 3":
            # code below only required for page 4
            Page3.forget()
            Page4.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 4")
            Button3["state"]="normal"
            Button7["state"]="normal"
            Button4["state"]="normal"
            Button8["state"]="normal"
            if Chk_Status == 1:
                ChkStatus.select()
            if Use_Stdby == 1:
                UseStdby.select()
        elif SettingsWindow.title() == "Settings - Page 4":
            # code below only required for page 5
            Page4.forget()
            Page5.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 5")
            Button3["state"]="disabled"
            Button7["state"]="disabled"
            Button4["state"]="normal"
            Button8["state"]="normal"

                
    def LastPage():
        if SettingsWindow.title() == "Settings - Page 2":
            Page2.forget()
            Page1.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 1")
            Button4["state"]="disabled"
            Button8["state"]="disabled"
            Button3["state"]="normal"
            Button7["state"]="normal"
        elif SettingsWindow.title() == "Settings - Page 3":
            Page3.forget()
            Page2.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 2")
            Button4["state"]="normal"
            Button8["state"]="normal"
            Button12["state"]="normal"
            Button16["state"]="normal"
            Button3["state"]="normal"
            Button7["state"]="normal"
        elif SettingsWindow.title() == "Settings - Page 4":
            Page4.forget()
            Page3.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 3")
            Button4["state"]="normal"
            Button8["state"]="normal"
            Button12["state"]="normal"
            Button16["state"]="normal"
            Button3["state"]="normal"
            Button7["state"]="normal"
        elif SettingsWindow.title() == "Settings - Page 5":
            Page5.forget()
            Page4.pack(expand=True, side=TOP, fill=BOTH)
            SettingsWindow.title("Settings - Page 4")
    
    # Cal screen GUI setup
    SettingsWindow.title("Settings - Page 1")
    Page1 = Frame(SettingsWindow, bd=2, padx=1, pady=1, relief=FLAT)
    Page1.pack(expand=True, side=TOP, fill=BOTH)
    
    Page2 = Frame(SettingsWindow, bd=2, padx=1, pady=1, relief=FLAT)

    Page3 = Frame(SettingsWindow, bd=2, padx=1, pady=1, relief=FLAT)
    Page4 = Frame(SettingsWindow, bd=2, padx=1, pady=1, relief=FLAT)
    Page5 = Frame(SettingsWindow, bd=2, padx=1, pady=1, relief=FLAT)
    
    Frame1 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame1.pack(expand=True, side=TOP, fill=X)
    Frame2 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    #Frame2.pack(expand=True, side=TOP, fill=BOTH)
    Frame2_5 = Frame(Page1, bd=2, pady=1, relief=FLAT)
    Frame2_5.pack(expand=True, side=TOP, fill=BOTH)
    Frame3 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame3.pack(expand=True, side=TOP, fill=BOTH)
    Frame4 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame4.pack(expand=True, side=TOP, fill=BOTH)
    Frame5 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame5.pack(expand=True, side=TOP, fill=BOTH)
    Frame6 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame6.pack(expand=True, side=TOP, fill=BOTH)
    Frame6_2 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame6_2.pack(expand=True, side=TOP, fill=BOTH)
    Frame6_5 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame6_5.pack(expand=True, side=TOP, fill=BOTH)
    Frame7 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame7.pack(expand=True, side=TOP, fill=BOTH)
    Frame8 = Frame(Page1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame8.pack(expand=True, side=BOTTOM, fill=BOTH)
    
    #Frame1    
    Label1 = Label(Frame1, text="Channel      ", padx=10, pady=1)
    Label1.pack(side=LEFT)
    Label2 = Label(Frame1, text="  1  ", padx=10, pady=1)
    Label2.pack(side=LEFT)
    Label3 = Label(Frame1, text="  2  ", padx=10, pady=1)
    Label3.pack(side=LEFT)
    Label4 = Label(Frame1, text="  3  ", padx=10, pady=1)
    Label4.pack(side=LEFT)
    Label5 = Label(Frame1, text="   4  ", padx=10, pady=1)
    Label5.pack(side=LEFT)
    Label6 = Label(Frame1, text="   5  ", padx=10, pady=1)
    Label6.pack(side=LEFT)
    Label7 = Label(Frame1, text="   6  ", padx=10, pady=1)
    Label7.pack(side=LEFT)
    Label8 = Label(Frame1, text="   7  ", padx=10, pady=1)
    Label8.pack(side=LEFT)
    Label9 = Label(Frame1, text="   8  ", padx=10, pady=1)
    Label9.pack(side=LEFT)


    #Frame2 
    Label10 = Label(Frame2, text="4mA =        ", padx=10, pady=1)
    Label10.pack(side=LEFT)
    CH1_4mA = Entry(Frame2, width=6)
    CH1_4mA.pack(side=LEFT, fill=BOTH)
    CH2_4mA = Entry(Frame2, width=6)
    CH2_4mA.pack(side=LEFT, fill=BOTH)
    CH3_4mA = Entry(Frame2, width=6)
    CH3_4mA.pack(side=LEFT, fill=BOTH)
    CH4_4mA = Entry(Frame2, width=6)
    CH4_4mA.pack(side=LEFT, fill=BOTH)
    CH5_4mA = Entry(Frame2, width=6)
    CH5_4mA.pack(side=LEFT, fill=BOTH)
    CH6_4mA = Entry(Frame2, width=6)
    CH6_4mA.pack(side=LEFT, fill=BOTH)
    CH7_4mA = Entry(Frame2, width=6)
    CH7_4mA.pack(side=LEFT, fill=BOTH)
    CH8_4mA = Entry(Frame2, width=6)
    CH8_4mA.pack(side=LEFT, fill=BOTH)
    
    #disable entry boxes for "4mA =", surely 4mA is alwasy zero!
    CH1_4mA["state"]="disabled"
    CH2_4mA["state"]="disabled"
    CH3_4mA["state"]="disabled"
    CH4_4mA["state"]="disabled"
    CH5_4mA["state"]="disabled"
    CH6_4mA["state"]="disabled"
    CH7_4mA["state"]="disabled"
    CH8_4mA["state"]="disabled"
    
    #Frame2_5
    #add 2 frames inside, 1 for tickboxes to activate a modbus input and if activated a second to enter which modbus register
    Frame2_5_1 = Frame(Frame2_5, bd=2, pady=1, relief=FLAT)
    Frame2_5_1.pack(expand=True, side=TOP, fill=BOTH)
    Frame2_5_2 = Frame(Frame2_5, bd=2, pady=1, relief=FLAT)
    Frame2_5_2.pack(expand=True, side=TOP, fill=BOTH)
    Label12 = Label(Frame2_5_1, text="Use Modbus? ", padx=10, pady=1)
    Label12.pack(side=LEFT)
    # add the tick boxes
    Mod1 = IntVar()
    Mod2 = IntVar()
    Mod3 = IntVar()
    Mod4 = IntVar()
    Mod5 = IntVar()
    Mod6 = IntVar()
    Mod7 = IntVar()
    Mod8 = IntVar()
    
    Use_Mod1 = Checkbutton(Frame2_5_1, text="", variable=Mod1, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod1.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch1Mod == 1:
        Use_Mod1.select()
    Use_Mod2 = Checkbutton(Frame2_5_1, text="", variable=Mod2, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod2.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch2Mod == 1:
        Use_Mod2.select()
    Use_Mod3 = Checkbutton(Frame2_5_1, text="", variable=Mod3, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod3.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch3Mod == 1:
        Use_Mod3.select()
    Use_Mod4 = Checkbutton(Frame2_5_1, text="", variable=Mod4, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod4.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch4Mod == 1:
        Use_Mod4.select()
    Use_Mod5 = Checkbutton(Frame2_5_1, text="", variable=Mod5, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod5.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch5Mod == 1:
        Use_Mod5.select()
    Use_Mod6 = Checkbutton(Frame2_5_1, text="", variable=Mod6, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod6.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch6Mod == 1:
        Use_Mod6.select()
    Use_Mod7 = Checkbutton(Frame2_5_1, text="", variable=Mod7, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod7.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch7Mod == 1:
        Use_Mod7.select()
    Use_Mod8 = Checkbutton(Frame2_5_1, text="", variable=Mod8, onvalue=1, offvalue=0, padx=4, pady=1)
    Use_Mod8.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch8Mod == 1:
        Use_Mod8.select()
    
    
    #Frame 2_5_2
    Label11 = Label(Frame2_5_2, text="Register =     ", padx=10, pady=1)
    Label11.pack(side=LEFT)
    Mod1_Reg = Entry(Frame2_5_2, width=6)
    Mod1_Reg.pack(side=LEFT, fill=BOTH)
    Mod1_Reg.bind("<1>", (lambda event: NumPad(Mod1_Reg)))
    Mod1_Reg.insert(0,str(Mod1Reg))
    
    Mod2_Reg = Entry(Frame2_5_2, width=6)
    Mod2_Reg.pack(side=LEFT, fill=BOTH)
    Mod2_Reg.bind("<1>", (lambda event: NumPad(Mod2_Reg)))
    Mod2_Reg.insert(0,str(Mod2Reg))
    
    Mod3_Reg = Entry(Frame2_5_2, width=6)
    Mod3_Reg.pack(side=LEFT, fill=BOTH)
    Mod3_Reg.bind("<1>", (lambda event: NumPad(Mod3_Reg)))
    Mod3_Reg.insert(0,str(Mod3Reg))
    
    Mod4_Reg = Entry(Frame2_5_2, width=6)
    Mod4_Reg.pack(side=LEFT, fill=BOTH)
    Mod4_Reg.bind("<1>", (lambda event: NumPad(Mod4_Reg)))
    Mod4_Reg.insert(0,str(Mod4Reg))
    
    Mod5_Reg = Entry(Frame2_5_2, width=6)
    Mod5_Reg.pack(side=LEFT, fill=BOTH)
    Mod5_Reg.bind("<1>", (lambda event: NumPad(Mod5_Reg)))
    Mod5_Reg.insert(0,str(Mod5Reg))
    
    Mod6_Reg = Entry(Frame2_5_2, width=6)
    Mod6_Reg.pack(side=LEFT, fill=BOTH)
    Mod6_Reg.bind("<1>", (lambda event: NumPad(Mod6_Reg)))
    Mod6_Reg.insert(0,str(Mod6Reg))
    
    Mod7_Reg = Entry(Frame2_5_2, width=6)
    Mod7_Reg.pack(side=LEFT, fill=BOTH)
    Mod7_Reg.bind("<1>", (lambda event: NumPad(Mod7_Reg)))
    Mod7_Reg.insert(0,str(Mod7Reg))
    
    Mod8_Reg = Entry(Frame2_5_2, width=6)
    Mod8_Reg.pack(side=LEFT, fill=BOTH)
    Mod8_Reg.bind("<1>", (lambda event: NumPad(Mod8_Reg)))
    Mod8_Reg.insert(0,str(Mod8Reg))
    
    Mod1_Reg["state"]="disabled"
    Mod2_Reg["state"]="disabled"
    Mod3_Reg["state"]="disabled"
    Mod4_Reg["state"]="disabled"
    Mod5_Reg["state"]="disabled"
    Mod6_Reg["state"]="disabled"
    Mod7_Reg["state"]="disabled"
    Mod8_Reg["state"]="disabled"
    
    #Frame3 
    Label11 = Label(Frame3, text="20mA =       ", padx=10, pady=1)
    Label11.pack(side=LEFT)
    CH1_20mA = Entry(Frame3, width=6)
    CH1_20mA.pack(side=LEFT, fill=BOTH)
    CH1_20mA.bind("<1>", (lambda event: NumPad(CH1_20mA)))
    CH2_20mA = Entry(Frame3, width=6)
    CH2_20mA.pack(side=LEFT, fill=BOTH)
    CH2_20mA.bind("<1>", (lambda event: NumPad(CH2_20mA)))
    CH3_20mA = Entry(Frame3, width=6)
    CH3_20mA.pack(side=LEFT, fill=BOTH)
    CH3_20mA.bind("<1>", (lambda event: NumPad(CH3_20mA)))
    CH4_20mA = Entry(Frame3, width=6)
    CH4_20mA.pack(side=LEFT, fill=BOTH)
    CH4_20mA.bind("<1>", (lambda event: NumPad(CH4_20mA)))
    CH5_20mA = Entry(Frame3, width=6)
    CH5_20mA.pack(side=LEFT, fill=BOTH)
    CH5_20mA.bind("<1>", (lambda event: NumPad(CH5_20mA)))
    CH6_20mA = Entry(Frame3, width=6)
    CH6_20mA.pack(side=LEFT, fill=BOTH)
    CH6_20mA.bind("<1>", (lambda event: NumPad(CH6_20mA)))
    CH7_20mA = Entry(Frame3, width=6)
    CH7_20mA.pack(side=LEFT, fill=BOTH)
    CH7_20mA.bind("<1>", (lambda event: NumPad(CH7_20mA)))
    CH8_20mA = Entry(Frame3, width=6)
    CH8_20mA.pack(side=LEFT, fill=BOTH)
    CH8_20mA.bind("<1>", (lambda event: NumPad(CH8_20mA)))
    
    #Frame4
    Label12 = Label(Frame4, text="Enabled?     ", padx=10, pady=1)
    Label12.pack(side=LEFT)
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    
    CH1_Active = Checkbutton(Frame4, text="", variable=var11, onvalue=1, offvalue=0, padx=4, pady=1)
    CH1_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch1Active == 1:
        CH1_Active.select()
    CH2_Active = Checkbutton(Frame4, text="", variable=var12, onvalue=1, offvalue=0, padx=4, pady=1)
    CH2_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch2Active == 1:
        CH2_Active.select()
    CH3_Active = Checkbutton(Frame4, text="", variable=var13, onvalue=1, offvalue=0, padx=4, pady=1)
    CH3_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch3Active == 1:
        CH3_Active.select()
    CH4_Active = Checkbutton(Frame4, text="", variable=var14, onvalue=1, offvalue=0, padx=4, pady=1)
    CH4_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch4Active == 1:
        CH4_Active.select()
    CH5_Active = Checkbutton(Frame4, text="", variable=var15, onvalue=1, offvalue=0, padx=4, pady=1)
    CH5_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch5Active == 1:
        CH5_Active.select()
    CH6_Active = Checkbutton(Frame4, text="", variable=var16, onvalue=1, offvalue=0, padx=4, pady=1)
    CH6_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch6Active == 1:
        CH6_Active.select()
    CH7_Active = Checkbutton(Frame4, text="", variable=var17, onvalue=1, offvalue=0, padx=4, pady=1)
    CH7_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch7Active == 1:
        CH7_Active.select()
    CH8_Active = Checkbutton(Frame4, text="", variable=var18, onvalue=1, offvalue=0, padx=4, pady=1)
    CH8_Active.pack(expand=True, side=LEFT, fill=BOTH)
    if Ch8Active == 1:
        CH8_Active.select()

    #Frame5    
    Label13 = Label(Frame5, text="Name          ", padx=10, pady=1)
    Label13.pack(side=LEFT)
    CH1_Name = Entry(Frame5, width=6)
    CH1_Name.pack(fill=BOTH, side=LEFT)
    CH1_Name.bind("<1>", (lambda event: TextPad(CH1_Name)))
    CH2_Name = Entry(Frame5, width=6)
    CH2_Name.pack(fill=BOTH, side=LEFT)
    CH2_Name.bind("<1>", (lambda event: TextPad(CH2_Name)))
    CH3_Name = Entry(Frame5, width=6)
    CH3_Name.pack(fill=BOTH, side=LEFT)
    CH3_Name.bind("<1>", (lambda event: TextPad(CH3_Name)))
    CH4_Name = Entry(Frame5, width=6)
    CH4_Name.pack(fill=BOTH, side=LEFT)
    CH4_Name.bind("<1>", (lambda event: TextPad(CH4_Name)))
    CH5_Name = Entry(Frame5, width=6)
    CH5_Name.pack(fill=BOTH, side=LEFT)
    CH5_Name.bind("<1>", (lambda event: TextPad(CH5_Name)))
    CH6_Name = Entry(Frame5, width=6)
    CH6_Name.pack(fill=BOTH, side=LEFT)
    CH6_Name.bind("<1>", (lambda event: TextPad(CH6_Name)))
    CH7_Name = Entry(Frame5, width=6)
    CH7_Name.pack(fill=BOTH, side=LEFT)
    CH7_Name.bind("<1>", (lambda event: TextPad(CH7_Name)))
    CH8_Name = Entry(Frame5, width=6)
    CH8_Name.pack(fill=BOTH, side=LEFT)
    CH8_Name.bind("<1>", (lambda event: TextPad(CH8_Name)))

    #Frame6
    Label14_5 = Label(Frame6, text="O2 corrected?", padx=10, pady=1)
    Label14_5.pack(side=LEFT)
    var21 = IntVar()
    var22 = IntVar()
    var23 = IntVar()
    var24 = IntVar()
    var25 = IntVar()
    var26 = IntVar()
    var27 = IntVar()
    var28 = IntVar()
    O21_Correct = Checkbutton(Frame6, text="", variable=var21, onvalue=1, offvalue=0, padx=4, pady=1)
    O21_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O21Correct == "Y":
        O21_Correct.select()
    O22_Correct = Checkbutton(Frame6, text="", variable=var22, onvalue=1, offvalue=0, padx=4, pady=1)
    O22_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O22Correct == "Y":
        O22_Correct.select()
    O23_Correct = Checkbutton(Frame6, text="", variable=var23, onvalue=1, offvalue=0, padx=4, pady=1)
    O23_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O23Correct == "Y":
        O23_Correct.select()
    O24_Correct = Checkbutton(Frame6, text="", variable=var24, onvalue=1, offvalue=0, padx=4, pady=1)
    O24_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O24Correct == "Y":
        O24_Correct.select()
    O25_Correct = Checkbutton(Frame6, text="", variable=var25, onvalue=1, offvalue=0, padx=4, pady=1)
    O25_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O25Correct == "Y":
        O25_Correct.select()
    O26_Correct = Checkbutton(Frame6, text="", variable=var26, onvalue=1, offvalue=0, padx=4, pady=1)
    O26_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O26Correct == "Y":
        O26_Correct.select()
    O27_Correct = Checkbutton(Frame6, text="", variable=var27, onvalue=1, offvalue=0, padx=4, pady=1)
    O27_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O27Correct == "Y":
        O27_Correct.select()
    O28_Correct = Checkbutton(Frame6, text="", variable=var28, onvalue=1, offvalue=0, padx=4, pady=1)
    O28_Correct.pack(expand=True, side=LEFT, fill=BOTH)
    if O28Correct == "Y":
        O28_Correct.select()

    #Frame6_2    
    Label13_2 = Label(Frame6_2, text="Units          ", padx=10, pady=1)
    Label13_2.pack(side=LEFT)
    Ch1_Units = Entry(Frame6_2, width=6)
    Ch1_Units.pack(fill=BOTH, side=LEFT)
    Ch1_Units.bind("<1>", (lambda event: TextPad(Ch1_Units)))
    Ch2_Units = Entry(Frame6_2, width=6)
    Ch2_Units.pack(fill=BOTH, side=LEFT)
    Ch2_Units.bind("<1>", (lambda event: TextPad(Ch2_Units)))
    Ch3_Units = Entry(Frame6_2, width=6)
    Ch3_Units.pack(fill=BOTH, side=LEFT)
    Ch3_Units.bind("<1>", (lambda event: TextPad(Ch3_Units)))
    Ch4_Units = Entry(Frame6_2, width=6)
    Ch4_Units.pack(fill=BOTH, side=LEFT)
    Ch4_Units.bind("<1>", (lambda event: TextPad(Ch4_Units)))
    Ch5_Units = Entry(Frame6_2, width=6)
    Ch5_Units.pack(fill=BOTH, side=LEFT)
    Ch5_Units.bind("<1>", (lambda event: TextPad(Ch5_Units)))
    Ch6_Units = Entry(Frame6_2, width=6)
    Ch6_Units.pack(fill=BOTH, side=LEFT)
    Ch6_Units.bind("<1>", (lambda event: TextPad(Ch6_Units)))
    Ch7_Units = Entry(Frame6_2, width=6)
    Ch7_Units.pack(fill=BOTH, side=LEFT)
    Ch7_Units.bind("<1>", (lambda event: TextPad(Ch7_Units)))
    Ch8_Units = Entry(Frame6_2, width=6)
    Ch8_Units.pack(fill=BOTH, side=LEFT)
    Ch8_Units.bind("<1>", (lambda event: TextPad(Ch8_Units)))
    
    #Frame6_5
    Label14 = Label(Frame6_5, text="Ave. Interval", padx=10, pady=1)
    Label14.pack(side=LEFT)
    CH1_Ave = Entry(Frame6_5, width=5)
    CH1_Ave.pack(side=LEFT)
    CH1_Ave.bind("<1>", (lambda event: NumPad(CH1_Ave)))
    Label14_8 = Label(Frame6_5, text="O2 Ref Level", padx=10, pady=1)
    Label14_8.pack(side=LEFT)
    O2_Ref = Entry(Frame6_5, width=5)
    O2_Ref.pack(side=LEFT)
    O2_Ref.bind("<1>", (lambda event: NumPad(O2_Ref)))
    
    #Frame7
    Label15 = Label(Frame7, text="Logging Files Created", padx=10, pady=1)
    Label15.pack(side=LEFT)
    var19 = IntVar()
    var20 = IntVar()
    
    DailyFiles = Checkbutton(Frame7, text="Daily", variable=var19, onvalue=1, offvalue=0, padx=2, pady=1)
    DailyFiles.pack(expand=True, side=LEFT, fill=BOTH)
    if Daily_Files == 1:
        DailyFiles.select()
    MonthlyFiles = Checkbutton(Frame7, text="Monthly", variable=var20, onvalue=1, offvalue=0, padx=2, pady=1)
    MonthlyFiles.pack(expand=True, side=LEFT, fill=BOTH)
    if Monthly_Files == 1:
        MonthlyFiles.select()
    
    #Frame8 
    Button1 = Button(Frame8, text="SAVE", padx=10, pady=1, command=lambda: CheckPassword(SaveSettings), bg=ButtonColour)
    Button1.pack(side=LEFT)
    Button2 = Button(Frame8, text="CANCEL", padx=10, pady=1, command=CancelSettings, bg=ButtonColour)
    Button2.pack(side=LEFT)
    ButtonCal = Button(Frame8, text="Calibrate Inputs", padx=10, pady=1, command=lambda: CheckPassword(CalInputs), bg=ButtonColour)
    ButtonCal.pack( side = LEFT, padx=4 )
    ButtonClock = Button(Frame8, text="Set Clock", padx=10, pady=1, command=SetClock, bg=ButtonColour)
    ButtonClock.pack( side = LEFT, padx=4 )
    
    Button3 = Button(Frame8, text="->", padx=6, pady=1, command=NextPage, bg=ButtonColour)
    Button3.pack(side=RIGHT)
    Button4 = Button(Frame8, text="<-", padx=6, pady=1, command=LastPage, bg=ButtonColour)
    Button4.pack(side=RIGHT)
    Button4["state"]="disabled"
    
    # Now populate info from the settings files
    FileName = SavePath + 'settings.data'
    fd = open(FileName, 'rb')
    dataset = pickle.load(fd)
    fd.close()
    if dataset[31] == "Y":
        O21_Correct.select()
    if dataset[32] == "Y":
        O22_Correct.select()
    if dataset[33] == "Y":
        O23_Correct.select()
    if dataset[34] == "Y":
        O24_Correct.select()
    if dataset[35] == "Y":
        O25_Correct.select()
    if dataset[36] == "Y":
        O26_Correct.select()
    if dataset[37] == "Y":
        O27_Correct.select()
    if dataset[38] == "Y":
        O28_Correct.select()
    if dataset[0] == 1:
        CH1_Active.select()
    if dataset[1] == 1:
        CH2_Active.select()
    if dataset[2] == 1:
        CH3_Active.select()
    if dataset[3] == 1:
        CH4_Active.select()
    if dataset[4] == 1:
        CH5_Active.select()
    if dataset[5] == 1:
        CH6_Active.select()
    if dataset[6] == 1:
        CH7_Active.select()
    if dataset[7] == 1:
        CH8_Active.select()
    if dataset[8] == 1:
        DailyFiles.select()
    if dataset[9] == 1:
        MonthlyFiles.select()
    CH1_4mA.insert(0,(dataset[10]))
    CH1_20mA.insert(0,(dataset[11]))
    CH2_4mA.insert(0,(dataset[12]))
    CH2_20mA.insert(0,(dataset[13]))
    CH3_4mA.insert(0,(dataset[14]))
    CH3_20mA.insert(0,(dataset[15]))
    CH4_4mA.insert(0,(dataset[16]))
    CH4_20mA.insert(0,(dataset[17]))
    CH5_4mA.insert(0,(dataset[18]))
    CH5_20mA.insert(0,(dataset[19]))
    CH6_4mA.insert(0,(dataset[20]))
    CH6_20mA.insert(0,(dataset[21]))
    CH7_4mA.insert(0,(dataset[22]))
    CH7_20mA.insert(0,(dataset[23]))
    CH8_4mA.insert(0,(dataset[24]))
    CH8_20mA.insert(0,(dataset[25]))
    CH1_Ave.insert(0,(dataset[26]))
    O2_Ref.insert(0,(dataset[39]))    
    Ch1_Units.insert(0,(dataset[40]))
    Ch2_Units.insert(0,(dataset[41]))
    Ch3_Units.insert(0,(dataset[42]))
    Ch4_Units.insert(0,(dataset[43]))
    Ch5_Units.insert(0,(dataset[44]))
    Ch6_Units.insert(0,(dataset[45]))
    Ch7_Units.insert(0,(dataset[46]))
    Ch8_Units.insert(0,(dataset[47]))
    if dataset[48] == 1:
        Use_Mod1.select()
    if dataset[49] == 1:
        Use_Mod2.select()
    if dataset[50] == 1:
        Use_Mod3.select()
    if dataset[51] == 1:
        Use_Mod4.select()
    if dataset[52] == 1:
        Use_Mod5.select()
    if dataset[53] == 1:
        Use_Mod6.select()
    if dataset[54] == 1:
        Use_Mod7.select()
    if dataset[55] == 1:
        Use_Mod8.select()
        
    FileName = SavePath + 'config.data'
    fd = open(FileName, 'rb')
    dataset2 = pickle.load(fd)
    fd.close()
    CH1_Name.insert(0,(dataset2[0]))
    CH2_Name.insert(0,(dataset2[1]))
    CH3_Name.insert(0,(dataset2[2]))
    CH4_Name.insert(0,(dataset2[3]))
    CH5_Name.insert(0,(dataset2[4]))
    CH6_Name.insert(0,(dataset2[5]))
    CH7_Name.insert(0,(dataset2[6]))
    CH8_Name.insert(0,(dataset2[7]))
    
    def Save_Modbus():
        global Slave_ID
        global Modbus_Baud
        global Modbus_Bits
        global Modbus_Parity
        global Modbus_StopBits
        global Modbus_Timeout
        Slave_ID = SlaveID.get()
        Modbus_Baud = int(ModbusBaud.get())
        Modbus_Bits = int(ModbusBits.get())
        Modbus_Parity = ModbusParity.get() 
        Modbus_StopBits = int(ModbusStopBits.get())
        Modbus_Timeout = int(ModbusTimeout.get())
        
        # perform error checking on user entry
        checked = 0
        try:
            value = int(Slave_ID)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Slave ID value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Slave_ID) < 128 and int(Slave_ID) > 0:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Slave ID must be between 1 and 127")
                SettingsWindow.tkraise()
        
        try:
            value = int(Modbus_Baud)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Baud Rate value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Modbus_Baud) == 1200 or int(Modbus_Baud) == 2400 or int(Modbus_Baud) == 4800 or int(Modbus_Baud) == 9600 or int(Modbus_Baud) == 14400 or int(Modbus_Baud) == 19200 or int(Modbus_Baud) == 38400:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Baud rate must be: 1200, 2400, 4800, 9600, 14400, 19200 or 38400")
                SettingsWindow.tkraise()
        
        try:
            value = int(Modbus_Bits)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Modbus bits value error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Modbus_Bits) == 7 or int(Modbus_Bits) == 8:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Bits must be 7 ot 8")
                SettingsWindow.tkraise()        
                
                
        try:
            value = int(Modbus_Parity)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Modbus Parity entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Modbus_Parity) == 0 or int(Modbus_Parity) == 1 or int(Modbus_Parity) == 2:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Parity must be 0 (none), 1 (Odd) or 2 (Even)")
                SettingsWindow.tkraise()
        
        try:
            value = int(Modbus_StopBits)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Modbus Stop bits entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Modbus_StopBits) == 1 or int(Modbus_StopBits) == 2:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Stop Bits must be 1 or 2")
                SettingsWindow.tkraise()        
        
        try:
            value = int(Modbus_Timeout)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Modbus Timeout entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Modbus_Timeout) > 0 and int(Modbus_Timeout) < 10001:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Timeout must be from 1 to 10000")
                SettingsWindow.tkraise()
                
        if checked == 12:    
            FileName = SavePath + 'config.data'
            fd = open(FileName, 'rb')
            newdataset = pickle.load(fd)
            fd.close()
            newdataset[40] = Slave_ID
            newdataset[41] = Modbus_Baud
            newdataset[42] = Modbus_Bits
            newdataset[43] = Modbus_Parity
            newdataset[44] = Modbus_StopBits
            newdataset[45] = Modbus_Timeout
            Outputdataset = newdataset
            fw = open(FileName, 'wb')
            pickle.dump(Outputdataset, fw)
            fw.close()
            SettingsWindow.lower()
            messagebox.showinfo("Please note", "System must be re-started for changes to take effect")
            SettingsWindow.tkraise()
                
            SettingsWindow.destroy()
    
    def Save_ModbusTCP():
        global client
        return
        client = ModbusTcpClient('192.168.55.1', port = 502)
    
    
    def Save_Report_Info():
        global Address_1
        global Address_2
        global Address_3
        global Post_Code
        global Permit_No
        global Site_Contact
        global Plant_ID
        Address_1 = Address1.get()
        Address_2 = Address2.get()
        Address_3 = Address3.get()
        Post_Code = Postcode.get()
        Permit_No= PermitNo.get()
        Site_Contact = SiteContact.get()
        Plant_ID = PlantID.get()
        
        checked = 0
        #try:
        #    value = int()
        #except ValueError:
        #    SettingsWindow.lower()
        #    messagebox.showinfo("ERROR", "Temperatute entry error")
        #    SettingsWindow.tkraise()
        #else:
        #    checked = checked + 1
        #    if int(Run_If_Temp) < 700 and int(Run_If_Temp) > -100:
        #        checked = checked + 1
        #    else:
        #        SettingsWindow.lower()
        #        messagebox.showinfo("ERROR", "Temperature must be between -100 and 700")
        #        SettingsWindow.tkraise()
                
        if checked == 0:    
            FileName = SavePath + 'MCP_config.data'
            fd = open(FileName, 'rb')
            newdataset = pickle.load(fd)
            fd.close()
            newdataset[4] = Address_1
            newdataset[5] = Address_2
            newdataset[6] = Address_3
            newdataset[7] = Post_Code
            newdataset[8] = Permit_No
            newdataset[9] = Site_Contact
            newdataset[10] = Plant_ID
            
            Outputdataset = newdataset
            fw = open(FileName, 'wb')
            pickle.dump(Outputdataset, fw)
            fw.close()
            #SettingsWindow.lower()
            # messagebox.showinfo("Please note", "System must be re-started for changes to take effect")
            #SettingsWindow.tkraise()
                
            SettingsWindow.destroy()
    
    def Save_MCP():
        global Chk_Status
        global Run_If_Temp
        global Use_Stdby
        global User_Pass
        global Dwell_Time
        global Meas_Time
        global Purge_Time
        Chk_Status = ChkStatVar.get()
        Run_If_Temp = RunIfTemp.get()
        Dwell_Time = DwellTime.get()
        Meas_Time = MeasTime.get()
        Purge_Time = PurgeTime.get()
        Use_Stdby = UseStdbyVar.get()
        User_Pass = "0000" 
        #print("run if")
        #print(Run_If_Temp)
        # perform error checking on user entry
        checked = 0
        try:
            value = int(Run_If_Temp)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Temperatute entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Run_If_Temp) < 700 and int(Run_If_Temp) > -100:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Temperature must be between -100 and 700")
                SettingsWindow.tkraise()
        
        
        try:
            value = int(Dwell_Time)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Dwell Time entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Dwell_Time) < 361 and int(Dwell_Time) > 4:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Dwell Time must be between 5 and 360")
                SettingsWindow.tkraise()
                
        try:
            value = int(Meas_Time)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Measurement Time entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Meas_Time) < 721 and int(Meas_Time) > 4:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Measurement Time must be between 5 and 720")
                SettingsWindow.tkraise()
                
        try:
            value = int(Purge_Time)
        except ValueError:
            SettingsWindow.lower()
            messagebox.showinfo("ERROR", "Purge Time entry error")
            SettingsWindow.tkraise()
        else:
            checked = checked + 1
            if int(Purge_Time) < 721 and int(Purge_Time) > 3:
                checked = checked + 1
            else:
                SettingsWindow.lower()
                messagebox.showinfo("ERROR", "Purge Time must be between 4 and 720")
                SettingsWindow.tkraise()
        
        
        
        if checked == 8:
            DataHold = int(Purge_Time) + 2
            FileName = SavePath + 'MCP_config.data'
            fd = open(FileName, 'rb')
            newdataset = pickle.load(fd)
            fd.close()
            newdataset[0] = Chk_Status
            newdataset[1] = Run_If_Temp
            newdataset[2] = Use_Stdby
            newdataset[3] = User_Pass
            newdataset[11] = Dwell_Time
            newdataset[12] = Meas_Time
            newdataset[13] = Purge_Time
    
            Outputdataset = newdataset
            fw = open(FileName, 'wb')
            pickle.dump(Outputdataset, fw)
            fw.close()
            #SettingsWindow.lower()
            # messagebox.showinfo("Please note", "System must be re-started for changes to take effect")
            #SettingsWindow.tkraise()
                
            SettingsWindow.destroy()
    
    
    # Page 2 of settings
    P2Frame1 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame1.pack(side=TOP, fill=BOTH)
    P2Frame2 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame2.pack(side=TOP)
    P2Frame3 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame3.pack(side=TOP)
    P2Frame4 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame4.pack(side=TOP)
    P2Frame5 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame5.pack(side=TOP)
    P2Frame6 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame6.pack(side=TOP)
    P2Frame7 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame7.pack(side=TOP)
    P2Frame8 = Frame(Page2, bd=2, padx=10, pady=1, relief=FLAT)
    P2Frame8.pack(side=BOTTOM, fill=X)

    #Frames
    Label1 = Label(P2Frame1, text="          Modbus RTU setup          ", padx=10, font='Helvetica 14 bold')
    Label1.pack(side=TOP)
    #Slave_ID = 1
    #Modbus_Baud = 9600
    #Modbus_Bits = 8
    #Modbus_Parity = 0
    #Modbus_StopBits = 1
    #Modbus_Timeout = 0.0001
    SlaveID_Label = Label(P2Frame2, text="Slave ID -", padx=10)
    SlaveID_Label.pack(side=LEFT)
    SlaveID = Entry(P2Frame2, width = 8)
    SlaveID.pack(side=LEFT)
    SlaveID.insert(0,Slave_ID)
    SlaveID.bind("<1>", (lambda event: NumPad(SlaveID)))
    
    Modbus_Baud_Label = Label(P2Frame3, text="Baud Rate -", padx=10)
    Modbus_Baud_Label.pack(side=LEFT)
    ModbusBaud = Entry(P2Frame3, width = 8)
    ModbusBaud.pack(side=LEFT)
    ModbusBaud.insert(0,Modbus_Baud)
    ModbusBaud.bind("<1>", (lambda event: NumPad(ModbusBaud)))
    
    Modbus_Bits_Label = Label(P2Frame4, text="Bits -", padx=10)
    Modbus_Bits_Label.pack(side=LEFT)
    ModbusBits = Entry(P2Frame4, width = 8)
    ModbusBits.pack(side=LEFT)
    ModbusBits.insert(0,Modbus_Bits)
    ModbusBits.bind("<1>", (lambda event: NumPad(ModbusBits)))
    
    Modbus_Parity_Label = Label(P2Frame5, text="Parity (0, 1 or 2) -", padx=10)
    Modbus_Parity_Label.pack(side=LEFT)
    ModbusParity = Entry(P2Frame5, width = 8)
    ModbusParity.pack(side=LEFT)
    ModbusParity.insert(0,Modbus_Parity)
    ModbusParity.bind("<1>", (lambda event: NumPad(ModbusParity)))
    
    Modbus_StopBits_Label = Label(P2Frame6, text="Stop bits -", padx=10)
    Modbus_StopBits_Label.pack(side=LEFT)
    ModbusStopBits = Entry(P2Frame6, width = 8)
    ModbusStopBits.pack(side=LEFT)
    ModbusStopBits.insert(0,Modbus_StopBits)
    ModbusStopBits.bind("<1>", (lambda event: NumPad(ModbusStopBits)))
    
    Modbus_Timeout_Label = Label(P2Frame7, text="Timeout (ms / 10) -", padx=10)
    Modbus_Timeout_Label.pack(side=LEFT)
    ModbusTimeout = Entry(P2Frame7, width = 8)
    ModbusTimeout.pack(side=LEFT)
    ModbusTimeout.insert(0,Modbus_Timeout)
    ModbusTimeout.bind("<1>", (lambda event: NumPad(ModbusTimeout)))
    
    #P2Frame8
    Button5 = Button(P2Frame8, text="SAVE", padx=10, pady=1, command=lambda: CheckUserPassword(Save_Modbus), bg=ButtonColour)
    Button5.pack(side=LEFT)
    Button6 = Button(P2Frame8, text="CANCEL", padx=10, pady=1, command=CancelSettings, bg=ButtonColour)
    Button6.pack(side=LEFT)
    Button7 = Button(P2Frame8, text="->", padx=6, pady=1, command=NextPage, bg=ButtonColour)
    Button7.pack(side=RIGHT)
    Button8 = Button(P2Frame8, text="<-", padx=6, pady=1, command=LastPage, bg=ButtonColour)
    Button8.pack(side=RIGHT)
    Button8["state"]="disabled"
    
    
    # Page 3 of settings
    P3Frame1 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame1.pack(side=TOP, fill=BOTH)
    P3Frame2 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame2.pack(side=TOP)
    P3Frame3 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame3.pack(side=TOP)
    P3Frame4 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame4.pack(side=TOP)
    P3Frame5 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame5.pack(side=TOP)
    P3Frame6 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame6.pack(side=TOP)
    P3Frame7 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame7.pack(side=TOP)
    P3Frame8 = Frame(Page3, bd=2, padx=10, pady=1, relief=FLAT)
    P3Frame8.pack(side=BOTTOM, fill=X)
    
    P3TitleLabel = Label(P3Frame1, text="Internal Cabinet TCP Modbus Setup", padx=10, pady=2, font='Helvetica 14 bold')
    P3TitleLabel.pack(side=TOP)
    
    # P3Frame2
    TCPID_Label = Label(P3Frame2, text="Modbus TCP Slave unit ID -", padx=10)
    TCPID_Label.pack(side=LEFT)
    TCPID = Entry(P3Frame2, width = 8)
    TCPID.pack(side=LEFT)
    TCPID.insert(0,TCP_ID)
    TCPID.bind("<1>", (lambda event: NumPad(TCPID)))
    
    TCPIP_Label = Label(P3Frame3, text="TCP IP address -", padx=10)
    TCPIP_Label.pack(side=LEFT)
    TCPIP = Entry(P3Frame3, width = 16)
    TCPIP.pack(side=LEFT)
    TCPIP.insert(0,TCP_IP)
    TCPIP.bind("<1>", (lambda event: NumPad(TCPIP)))
    
    TCPID["state"]="disabled"
    TCPIP["state"]="disabled"
    
    
    #Modbus_Bits_Label = Label(P3Frame4, text="Bits -", padx=10)
    #Modbus_Bits_Label.pack(side=LEFT)
    #ModbusBits = Entry(P3Frame4, width = 8)
    #ModbusBits.pack(side=LEFT)
    #ModbusBits.insert(0,Modbus_Bits)
    #ModbusBits.bind("<1>", (lambda event: NumPad(ModbusBits)))
    
    #Modbus_Parity_Label = Label(P3Frame5, text="Parity (0, 1 or 2) -", padx=10)
    #Modbus_Parity_Label.pack(side=LEFT)
    #ModbusParity = Entry(P3Frame5, width = 8)
    #ModbusParity.pack(side=LEFT)
    #ModbusParity.insert(0,Modbus_Parity)
    #ModbusParity.bind("<1>", (lambda event: NumPad(ModbusParity)))
    
    
    #P3Frame8
    Button9 = Button(P3Frame8, text="SAVE", padx=10, pady=1, command=lambda: CheckPassword(Save_ModbusTCP), bg=ButtonColour)
    Button9.pack(side=LEFT)
    Button10 = Button(P3Frame8, text="CANCEL", padx=10, pady=1, command=CancelSettings, bg=ButtonColour)
    Button10.pack(side=LEFT)
    Button11 = Button(P3Frame8, text="->", padx=6, pady=1, command=NextPage, bg=ButtonColour)
    Button11.pack(side=RIGHT)
    Button12 = Button(P3Frame8, text="<-", padx=6, pady=1, command=LastPage, bg=ButtonColour)
    Button12.pack(side=RIGHT)
    Button11["state"]="normal"
    Button9["state"]="disabled"

    # Page 4 of settings
    P4Frame1 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame1.pack(side=TOP, fill=BOTH)
    P4Frame2 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame2.pack(side=TOP)
    P4Frame3 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame3.pack(side=TOP)
    P4Frame4 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame4.pack(side=TOP)
    P4Frame5 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame5.pack(side=TOP)
    P4Frame6 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame6.pack(side=TOP)
    P4Frame7 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame7.pack(side=TOP)
    P4Frame8 = Frame(Page4, bd=2, padx=10, pady=1, relief=FLAT)
    P4Frame8.pack(side=BOTTOM, fill=X)
    
    # P4Frame1
    Page4_Label = Label(P4Frame1, text="MCP Setup Options:-", padx=10, font='Helvetica 14 bold')
    Page4_Label.pack(side=TOP)
    
    # P4Frame2
    RunIfTemp_Label = Label(P4Frame2, text="Plant running if Stack Temp (Deg C) > : ", padx=10)
    RunIfTemp_Label.pack(side=LEFT)
    RunIfTemp = Entry(P4Frame2, width = 8)
    RunIfTemp.pack(side=LEFT)
    RunIfTemp.insert(0,Run_If_Temp)
    RunIfTemp.bind("<1>", (lambda event: NumPad(RunIfTemp)))
    
    # P4Frame3
    ChkStatVar = IntVar()
    ChkStatus = Checkbutton(P4Frame3, text="Enable Status checking of gas analyser?", variable=ChkStatVar, onvalue=1, offvalue=0, padx=10, pady=4)
    ChkStatus.pack(side=LEFT) 
    if Chk_Status == 1:
        ChkStatus.select()
    
    # P4Frame4 
    UseStdbyVar = IntVar()
    UseStdby = Checkbutton(P4Frame4, text="Put Gas Analyser in Standby if plant off?", variable=UseStdbyVar, onvalue=1, offvalue=0, padx=10, pady=4)
    UseStdby.pack(side=LEFT)
    if Use_Stdby == "1":
        UseStdby.select()
    
    # P4Frame5
    DwellTime_Label = Label(P4Frame5, text="Dwell Time (secs) : ", padx=10)
    DwellTime_Label.pack(side=LEFT)
    DwellTime = Entry(P4Frame5, width = 8)
    DwellTime.pack(side=LEFT)
    DwellTime.insert(0,Dwell_Time)
    DwellTime.bind("<1>", (lambda event: NumPad(DwellTime)))
    
    # P4Frame6
    MeasTime_Label = Label(P4Frame6, text="Measurement time (mins) : ", padx=10)
    MeasTime_Label.pack(side=LEFT)
    MeasTime = Entry(P4Frame6, width = 8)
    MeasTime.pack(side=LEFT)
    MeasTime.insert(0,Meas_Time)
    MeasTime.bind("<1>", (lambda event: NumPad(MeasTime)))
    
    # P4Frame7
    PurgeTime_Label = Label(P4Frame7, text="Purge Time (mins) : ", padx=10)
    PurgeTime_Label.pack(side=LEFT)
    PurgeTime = Entry(P4Frame7, width = 8)
    PurgeTime.pack(side=LEFT)
    PurgeTime.insert(0,Purge_Time)
    PurgeTime.bind("<1>", (lambda event: NumPad(PurgeTime)))
    
    #P4Frame8
    Button13 = Button(P4Frame8, text="SAVE", padx=10, pady=1, command=lambda: CheckPassword(Save_MCP), bg=ButtonColour)
    Button13.pack(side=LEFT)
    Button14 = Button(P4Frame8, text="CANCEL", padx=10, pady=1, command=CancelSettings, bg=ButtonColour)
    Button14.pack(side=LEFT)
    Button15 = Button(P4Frame8, text="->", padx=6, pady=1, command=NextPage, bg=ButtonColour)
    Button15.pack(side=RIGHT)
    Button16 = Button(P4Frame8, text="<-", padx=6, pady=1, command=LastPage, bg=ButtonColour)
    Button16.pack(side=RIGHT)
    Button15["state"]="normal"
    Button13["state"]="normal"
    
    # Page 5 of settings
    P5Frame1 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame1.pack(side=TOP, fill=BOTH)
    P5Frame2 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame2.pack(side=TOP)
    P5Frame3 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame3.pack(side=TOP)
    P5Frame4 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame4.pack(side=TOP)
    P5Frame5 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame5.pack(side=TOP)
    P5Frame6 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame6.pack(side=TOP)
    P5Frame7 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame7.pack(side=TOP)
    P5Frame8 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame8.pack(side=TOP)
    P5Frame9 = Frame(Page5, bd=2, padx=10, pady=1, relief=FLAT)
    P5Frame9.pack(side=BOTTOM, fill=X)
    
    # P5Frame1
    Page5_Label = Label(P5Frame1, text="Report generation Options:-", padx=10, font='Helvetica 14 bold')
    Page5_Label.pack(side=TOP)
    
    # P5Frame2
    Address1_Label = Label(P5Frame2, text="Site Address", padx=10)
    Address1_Label.pack(side=LEFT)
    Address1 = Entry(P5Frame2, width = 20)
    Address1.pack(side=LEFT)
    Address1.insert(0,Address_1)
    Address1.bind("<1>", (lambda event: TextPad(Address1)))
    
    # P5Frame3
    Address2_Label = Label(P5Frame3, text="            ", padx=10, width = 10)
    Address2_Label.pack(side=LEFT)
    Address2 = Entry(P5Frame3, width = 20)
    Address2.pack(side=LEFT)
    Address2.insert(0,Address_2)
    Address2.bind("<1>", (lambda event: TextPad(Address2)))
    
    # P5Frame4
    Address3_Label = Label(P5Frame4, text="            ", padx=10, width = 10)
    Address3_Label.pack(side=LEFT)
    Address3 = Entry(P5Frame4, width = 20)
    Address3.pack(side=LEFT)
    Address3.insert(0,Address_3)
    Address3.bind("<1>", (lambda event: TextPad(Address3)))
    
    # P5Frame5
    Postcode_Label = Label(P5Frame5, text="Postcode    ", padx=10)
    Postcode_Label.pack(side=LEFT)
    Postcode = Entry(P5Frame5, width = 20)
    Postcode.pack(side=LEFT)
    Postcode.insert(0,Post_Code)
    Postcode.bind("<1>", (lambda event: TextPad(Postcode)))

    # P5Frame6
    SiteContact_Label = Label(P5Frame6, text="Site Contact", padx=10)
    SiteContact_Label.pack(side=LEFT)
    SiteContact = Entry(P5Frame6, width = 20)
    SiteContact.pack(side=LEFT)
    SiteContact.insert(0,Site_Contact)
    SiteContact.bind("<1>", (lambda event: TextPad(SiteContact)))
    
    # P5Frame7
    PermitNo_Label = Label(P5Frame7, text="Permit No.  ", padx=10)
    PermitNo_Label.pack(side=LEFT)
    PermitNo = Entry(P5Frame7, width = 20)
    PermitNo.pack(side=LEFT)
    PermitNo.insert(0,Permit_No)
    PermitNo.bind("<1>", (lambda event: TextPad(PermitNo)))
    
    # P5Frame8
    PlantID_Label = Label(P5Frame8, text="Plant ID     ", padx=10)
    PlantID_Label.pack(side=LEFT)
    PlantID = Entry(P5Frame8, width = 20)
    PlantID.pack(side=LEFT)
    PlantID.insert(0,Plant_ID)
    PlantID.bind("<1>", (lambda event: TextPad(PlantID)))
    
    #P5Frame8
    Button17 = Button(P5Frame9, text="SAVE", padx=10, pady=1, command=lambda: CheckUserPassword(Save_Report_Info), bg=ButtonColour)
    Button17.pack(side=LEFT)
    Button18 = Button(P5Frame9, text="CANCEL", padx=10, pady=1, command=CancelSettings, bg=ButtonColour)
    Button18.pack(side=LEFT)
    Button19 = Button(P5Frame9, text="->", padx=6, pady=1, command=NextPage, bg=ButtonColour)
    Button19.pack(side=RIGHT)
    Button20 = Button(P5Frame9, text="<-", padx=6, pady=1, command=LastPage, bg=ButtonColour)
    Button20.pack(side=RIGHT)
    Button19["state"]="disabled"
    Button13["state"]="normal"
    
def ConfigAlarms():
    global CH1DispName
    global CH2DispName
    global CH3DispName
    global CH4DispName
    global CH5DispName
    global CH6DispName
    global CH7DispName
    global CH8DispName
    global CH1MinAlarm
    global CH2MinAlarm
    global CH3MinAlarm
    global CH4MinAlarm
    global CH5MinAlarm
    global CH6MinAlarm
    global CH7MinAlarm
    global CH8MinAlarm
    global CH1MaxAlarm
    global CH2MaxAlarm
    global CH3MaxAlarm
    global CH4MaxAlarm
    global CH5MaxAlarm
    global CH6MaxAlarm
    global CH7MaxAlarm
    global CH8MaxAlarm
    global Ch1MinAlOn
    global Ch2MinAlOn
    global Ch3MinAlOn
    global Ch4MinAlOn
    global Ch5MinAlOn
    global Ch6MinAlOn
    global Ch7MinAlOn
    global Ch8MinAlOn
    global Ch1MaxAlOn
    global Ch2MaxAlOn
    global Ch3MaxAlOn
    global Ch4MaxAlOn
    global Ch5MaxAlOn
    global Ch6MaxAlOn
    global Ch7MaxAlOn
    global Ch8MaxAlOn
    global ButtonColour
    global SavePath
    AlarmsWindow = Toplevel(root)
    AlarmsWindow.title("ALARM SETTINGS")
    
    def SaveAlarms():
        global Ch1MinAlOn
        global Ch1MaxAlOn
        global Ch2MinAlOn
        global Ch2MaxAlOn
        global Ch3MinAlOn
        global Ch3MaxAlOn
        global Ch4MinAlOn
        global Ch4MaxAlOn
        global Ch5MinAlOn
        global Ch5MaxAlOn
        global Ch6MinAlOn
        global Ch6MaxAlOn
        global Ch7MinAlOn
        global Ch7MaxAlOn
        global Ch8MinAlOn
        global Ch8MaxAlOn
        global CH1MinAlarm
        global CH2MinAlarm
        global CH3MinAlarm
        global CH4MinAlarm
        global CH5MinAlarm
        global CH6MinAlarm
        global CH7MinAlarm
        global CH8MinAlarm
        global CH1MaxAlarm
        global CH2MaxAlarm
        global CH3MaxAlarm
        global CH4MaxAlarm
        global CH5MaxAlarm
        global CH6MaxAlarm
        global CH7MaxAlarm
        global CH8MaxAlarm
        global CH1DispName
        global CH2DispName
        global CH3DispName
        global CH4DispName
        global CH5DispName
        global CH6DispName
        global CH7DispName
        global CH8DispName
        global SavePath
        Ch1MinAlOn = var1.get()
        Ch1MaxAlOn = var2.get()
        Ch2MinAlOn = var3.get()
        Ch2MaxAlOn = var4.get()
        Ch3MinAlOn = var5.get()
        Ch3MaxAlOn = var6.get()
        Ch4MinAlOn = var7.get()
        Ch4MaxAlOn = var8.get()
        Ch5MinAlOn = var9.get()
        Ch5MaxAlOn = var10.get()
        Ch6MinAlOn = var11.get()
        Ch6MaxAlOn = var12.get()
        Ch7MinAlOn = var13.get()
        Ch7MaxAlOn = var14.get()
        Ch8MinAlOn = var15.get()
        Ch8MaxAlOn = var16.get()
        
        CH1MinAlarm = CH1Min.get()
        CH2MinAlarm = CH2Min.get()
        CH3MinAlarm = CH3Min.get()
        CH4MinAlarm = CH4Min.get()
        CH5MinAlarm = CH5Min.get()
        CH6MinAlarm = CH6Min.get()
        CH7MinAlarm = CH7Min.get()
        CH8MinAlarm = CH8Min.get()
        CH1MaxAlarm = CH1Max.get()
        CH2MaxAlarm = CH2Max.get()
        CH3MaxAlarm = CH3Max.get()
        CH4MaxAlarm = CH4Max.get()
        CH5MaxAlarm = CH5Max.get()
        CH6MaxAlarm = CH6Max.get()
        CH7MaxAlarm = CH7Max.get()
        CH8MaxAlarm = CH8Max.get()
        
        # input error checking
        checked = 0
        try:
            value = int(CH1MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch1 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH1MinAlarm) < 999999 and int(CH1MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch1 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH2MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch2 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH2MinAlarm) < 999999 and int(CH2MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch2 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH3MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch3 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH3MinAlarm) < 999999 and int(CH3MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch3 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH4MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch4 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH4MinAlarm) < 999999 and int(CH4MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch4 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH5MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch5 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH5MinAlarm) < 999999 and int(CH5MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch5 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH6MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch6 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH6MinAlarm) < 999999 and int(CH6MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch6 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH7MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch7 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH7MinAlarm) < 999999 and int(CH7MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch7 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH8MinAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch8 Min value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH8MinAlarm) < 999999 and int(CH8MinAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch8 Min value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH1MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch1 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH1MaxAlarm) < 999999 and int(CH1MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch1 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        
        try:
            value = int(CH2MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch2 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH2MaxAlarm) < 999999 and int(CH2MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch2 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH3MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch3 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH3MaxAlarm) < 999999 and int(CH3MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch3 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH4MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch4 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH4MaxAlarm) < 999999 and int(CH4MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch4 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH5MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch5 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH5MaxAlarm) < 999999 and int(CH5MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch5 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH6MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch6 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH6MaxAlarm) < 999999 and int(CH6MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch6 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH7MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch7 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH7MaxAlarm) < 999999 and int(CH7MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch7 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        try:
            value = int(CH8MaxAlarm)
        except ValueError:
            AlarmsWindow.lower()
            messagebox.showinfo("ERROR", "Ch8 Max value error")
            AlarmsWindow.tkraise()
        else:
            checked = checked + 1
            if int(CH8MaxAlarm) < 999999 and int(CH8MaxAlarm) > -9999:
                checked = checked + 1
            else:
                AlarmsWindow.lower()
                messagebox.showinfo("ERROR", "Ch8 Max value >999999 or <-9999")
                AlarmsWindow.tkraise()
        
        if checked == 32:        
            # save new settings to config file
            FileName = SavePath + 'config.data'
            dataset = [CH1DispName, CH2DispName, CH3DispName, CH4DispName, CH5DispName, CH6DispName, CH7DispName, CH8DispName, CH1MinAlarm, CH2MinAlarm, CH3MinAlarm, CH4MinAlarm, CH5MinAlarm, CH6MinAlarm, CH7MinAlarm, CH8MinAlarm, CH1MaxAlarm, CH2MaxAlarm, CH3MaxAlarm, CH4MaxAlarm, CH5MaxAlarm, CH6MaxAlarm, CH7MaxAlarm, CH8MaxAlarm, Ch1MinAlOn, Ch2MinAlOn, Ch3MinAlOn, Ch4MinAlOn, Ch5MinAlOn, Ch6MinAlOn, Ch7MinAlOn, Ch8MinAlOn, Ch1MaxAlOn, Ch2MaxAlOn, Ch3MaxAlOn, Ch4MaxAlOn, Ch5MaxAlOn, Ch6MaxAlOn, Ch7MaxAlOn, Ch8MaxAlOn, Slave_ID, Modbus_Baud, Modbus_Bits, Modbus_Parity, Modbus_StopBits, Modbus_Timeout]
            fw = open(FileName, 'wb')
            pickle.dump(dataset, fw)
            fw.close()
            
            # close window after saving
            AlarmsWindow.destroy()
             
    def AlarmsDone():
        AlarmsWindow.destroy()

    # Cal screen GUI setup
    Frame1 = Frame(AlarmsWindow, bd=2, padx=10, pady=10, relief=SUNKEN)
    Frame1.pack(expand=True, side=TOP, fill=BOTH)
    
    FrameTitles = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    FrameTitles.pack(expand=True, side=TOP, fill=BOTH)
    Frame2 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame2.pack(expand=True, side=TOP, fill=BOTH)
    Frame3 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame3.pack(expand=True, side=TOP, fill=BOTH)
    Frame4 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame4.pack(expand=True, side=TOP, fill=BOTH)
    Frame5 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame5.pack(expand=True, side=TOP, fill=BOTH)
    Frame6 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame6.pack(expand=True, side=TOP, fill=BOTH)
    Frame7 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame7.pack(expand=True, side=TOP, fill=BOTH)
    Frame8 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame8.pack(expand=True, side=TOP, fill=BOTH)
    Frame9 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame9.pack(expand=True, side=TOP, fill=BOTH)
    Frame10 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame10.pack(expand=True, side=TOP, fill=BOTH)
    
    Button1 = Button(Frame10, text="SAVE", padx=10, pady=10, command=SaveAlarms, bg=ButtonColour)
    Button1.pack(side=LEFT, pady=10)
    Button2 = Button(Frame10, text="CANCEL", padx=10, pady=10, command=AlarmsDone, bg=ButtonColour)
    Button2.pack(side=LEFT, pady=10)
    
    Label1 = Label(FrameTitles, text="Channel", padx=10, pady=10)
    Label1.pack(side=LEFT)
    Label2 = Label(FrameTitles, text="Name", width = 10, padx=10, pady=10)
    Label2.pack(side=LEFT)
    Label3 = Label(FrameTitles, text="Low Level", width = 20, padx=10, pady=10)
    Label3.pack(side=LEFT)
    Label4 = Label(FrameTitles, text="High Level", padx=10, pady=10)
    Label4.pack(side=LEFT)
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    
    
    CH1_Label = Label(Frame2, text="Channel 1", padx=10, pady=4)
    CH1_Label.pack(side=LEFT)
    CH1_Name = Label(Frame2, text=CH1DispName, width = 10, padx=10, pady=4)
    CH1_Name.pack(side=LEFT)
    #CH1_Name.bind("<1>", (lambda event: TextPad(CH1_Name)))
    CH1Min = Entry(Frame2, width=5)
    CH1Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH1Min.bind("<1>", (lambda event: NumPad(CH1Min)))
    CH1Min.insert(0,CH1MinAlarm)
    CH1_MinOn = Checkbutton(Frame2, text="enabled", variable=var1, onvalue=1, offvalue=0, padx=10, pady=4)
    CH1_MinOn.pack(side=LEFT)
    if Ch1MinAlOn == 1:
        CH1_MinOn.select()
    CH1Max = Entry(Frame2, width=5)
    CH1Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH1Max.bind("<1>", (lambda event: NumPad(CH1Max)))
    CH1Max.insert(0,CH1MaxAlarm)
    CH1_MaxOn = Checkbutton(Frame2, text="enabled", variable=var2, onvalue=1, offvalue=0, padx=10, pady=4)
    CH1_MaxOn.pack(side=LEFT)
    if Ch1MaxAlOn == 1:
        CH1_MaxOn.select()
    
    CH2_Label = Label(Frame3, text="Channel 2", padx=10, pady=4)
    CH2_Label.pack(side=LEFT)
    CH2_Name = Label(Frame3, text=CH2DispName, width = 10, padx=10, pady=4)
    CH2_Name.pack(side=LEFT)
    CH2Min = Entry(Frame3, width=5)
    CH2Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH2Min.bind("<1>", (lambda event: NumPad(CH2Min)))
    CH2Min.insert(0,CH2MinAlarm)
    CH2_MinOn = Checkbutton(Frame3, text="enabled", variable=var3, onvalue=1, offvalue=0, padx=10, pady=4)
    CH2_MinOn.pack(side=LEFT)
    if Ch2MinAlOn == 1:
        CH2_MinOn.select()
    CH2Max = Entry(Frame3, width=5)
    CH2Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH2Max.bind("<1>", (lambda event: NumPad(CH2Max)))
    CH2Max.insert(0,CH2MaxAlarm)
    CH2_MaxOn = Checkbutton(Frame3, text="enabled", variable=var4, onvalue=1, offvalue=0, padx=10, pady=4)
    CH2_MaxOn.pack(side=LEFT)
    if Ch2MaxAlOn == 1:
        CH2_MaxOn.select()
    
    CH3_Label = Label(Frame4, text="Channel 3", padx=10, pady=4)
    CH3_Label.pack(side=LEFT)
    CH3_Name = Label(Frame4, text=CH3DispName, width = 10, padx=10, pady=4)
    CH3_Name.pack(side=LEFT)
    CH3Min = Entry(Frame4, width=5)
    CH3Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH3Min.bind("<1>", (lambda event: NumPad(CH3Min)))
    CH3Min.insert(0,CH3MinAlarm)
    CH3_MinOn = Checkbutton(Frame4, text="enabled", variable=var5, onvalue=1, offvalue=0, padx=10, pady=4)
    CH3_MinOn.pack(side=LEFT)
    if Ch3MinAlOn == 1:
        CH3_MinOn.select()
    CH3Max = Entry(Frame4, width=5)
    CH3Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH3Max.bind("<1>", (lambda event: NumPad(CH3Max)))
    CH3Max.insert(0,CH3MaxAlarm)
    CH3_MaxOn = Checkbutton(Frame4, text="enabled", variable=var6, onvalue=1, offvalue=0, padx=10, pady=4)
    CH3_MaxOn.pack(side=LEFT)
    if Ch3MaxAlOn == 1:
        CH3_MaxOn.select()
    
    CH4_Label = Label(Frame5, text="Channel 4", padx=10, pady=4)
    CH4_Label.pack(side=LEFT)
    CH4_Name = Label(Frame5, text=CH4DispName, width = 10, padx=10, pady=4)
    CH4_Name.pack(side=LEFT)
    CH4Min = Entry(Frame5, width=5)
    CH4Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH4Min.bind("<1>", (lambda event: NumPad(CH4Min)))
    CH4Min.insert(0,CH4MinAlarm)
    CH4_MinOn = Checkbutton(Frame5, text="enabled", variable=var7, onvalue=1, offvalue=0, padx=10, pady=4)
    CH4_MinOn.pack(side=LEFT)
    if Ch4MinAlOn == 1:
        CH4_MinOn.select()
    CH4Max = Entry(Frame5, width=5)
    CH4Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH4Max.bind("<1>", (lambda event: NumPad(CH4Max)))
    CH4Max.insert(0,CH4MaxAlarm)
    CH4_MaxOn = Checkbutton(Frame5, text="enabled", variable=var8, onvalue=1, offvalue=0, padx=10, pady=4)
    CH4_MaxOn.pack(side=LEFT)
    if Ch4MaxAlOn == 1:
        CH4_MaxOn.select()
    
    CH5_Label = Label(Frame6, text="Channel 5", padx=10, pady=4)
    CH5_Label.pack(side=LEFT)
    CH5_Name = Label(Frame6, text=CH5DispName, width = 10, padx=10, pady=4)
    CH5_Name.pack(side=LEFT)
    CH5Min = Entry(Frame6, width=5)
    CH5Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH5Min.bind("<1>", (lambda event: NumPad(CH5Min)))
    CH5Min.insert(0,CH5MinAlarm)
    CH5_MinOn = Checkbutton(Frame6, text="enabled", variable=var9, onvalue=1, offvalue=0, padx=10, pady=4)
    CH5_MinOn.pack(side=LEFT)
    if Ch5MinAlOn == 1:
        CH5_MinOn.select()
    CH5Max = Entry(Frame6, width=5)
    CH5Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH5Max.bind("<1>", (lambda event: NumPad(CH5Max)))
    CH5Max.insert(0,CH5MaxAlarm)
    CH5_MaxOn = Checkbutton(Frame6, text="enabled", variable=var10, onvalue=1, offvalue=0, padx=10, pady=4)
    CH5_MaxOn.pack(side=LEFT)
    if Ch5MaxAlOn == 1:
        CH5_MaxOn.select()
    
    CH6_Label = Label(Frame7, text="Channel 6", padx=10, pady=4)
    CH6_Label.pack(side=LEFT)
    CH6_Name = Label(Frame7, text=CH6DispName, width = 10, padx=10, pady=4)
    CH6_Name.pack(side=LEFT)
    CH6Min = Entry(Frame7, width=5)
    CH6Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH6Min.bind("<1>", (lambda event: NumPad(CH6Min)))
    CH6Min.insert(0,CH6MinAlarm)
    CH6_MinOn = Checkbutton(Frame7, text="enabled", variable=var11, onvalue=1, offvalue=0, padx=10, pady=4)
    CH6_MinOn.pack(side=LEFT)
    if Ch6MinAlOn == 1:
        CH6_MinOn.select()
    CH6Max = Entry(Frame7, width=5)
    CH6Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH6Max.bind("<1>", (lambda event: NumPad(CH6Max)))
    CH6Max.insert(0,CH6MaxAlarm)
    CH6_MaxOn = Checkbutton(Frame7, text="enabled", variable=var12, onvalue=1, offvalue=0, padx=10, pady=4)
    CH6_MaxOn.pack(side=LEFT)
    if Ch6MaxAlOn == 1:
        CH6_MaxOn.select()
    
    CH7_Label = Label(Frame8, text="Channel 7", padx=10, pady=4)
    CH7_Label.pack(side=LEFT)
    CH7_Name = Label(Frame8, text=CH7DispName, width = 10, padx=10, pady=4)
    CH7_Name.pack(side=LEFT)
    CH7Min = Entry(Frame8, width=5)
    CH7Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH7Min.bind("<1>", (lambda event: NumPad(CH7Min)))
    CH7Min.insert(0,CH7MinAlarm)
    CH7_MinOn = Checkbutton(Frame8, text="enabled", variable=var13, onvalue=1, offvalue=0, padx=10, pady=4)
    CH7_MinOn.pack(side=LEFT)
    if Ch7MinAlOn == 1:
        CH7_MinOn.select()
    CH7Max = Entry(Frame8, width=5)
    CH7Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH7Max.bind("<1>", (lambda event: NumPad(CH7Max)))
    CH7Max.insert(0,CH7MaxAlarm)
    CH7_MaxOn = Checkbutton(Frame8, text="enabled", variable=var14, onvalue=1, offvalue=0, padx=10, pady=4)
    CH7_MaxOn.pack(side=LEFT)
    if Ch7MaxAlOn == 1:
        CH7_MaxOn.select()
    
    CH8_Label = Label(Frame9, text="Channel 8", padx=10, pady=4)
    CH8_Label.pack(side=LEFT)
    CH8_Name = Label(Frame9, text=CH8DispName, width = 10, padx=10, pady=4)
    CH8_Name.pack(side=LEFT)
    CH8Min = Entry(Frame9, width=5)
    CH8Min.pack(expand=True, side=LEFT, fill=BOTH)
    CH8Min.bind("<1>", (lambda event: NumPad(CH8Min)))
    CH8Min.insert(0,CH8MinAlarm)
    CH8_MinOn = Checkbutton(Frame9, text="enabled", variable=var15, onvalue=1, offvalue=0, padx=10, pady=4)
    CH8_MinOn.pack(side=LEFT)
    if Ch8MinAlOn == 1:
        CH8_MinOn.select()
    CH8Max = Entry(Frame9, width=5)
    CH8Max.pack(expand=True, side=LEFT, fill=BOTH)
    CH8Max.bind("<1>", (lambda event: NumPad(CH8Max)))
    CH8Max.insert(0,CH8MaxAlarm)
    CH8_MaxOn = Checkbutton(Frame9, text="enabled", variable=var16, onvalue=1, offvalue=0, padx=10, pady=4)
    CH8_MaxOn.pack(side=LEFT)
    if Ch8MaxAlOn == 1:
        CH8_MaxOn.select()

def ExportData():
    global ButtonColour
    global PathtoUSB
    
    def Eject():
        ExportWindow.lower()
        os.system('sudo umount /dev/sda1 && sudo eject /dev/sda')
        messagebox.showinfo("DONE", "USB drive ejected")
        ExportWindow.tkraise()
        ExportWindow.destroy()
    
    def Export_Clicked():
        global PathtoUSB

        #ExportWindow.lower()
        #location = filedialog.askdirectory(parent=root, initialdir="/media/pi")
        ##busses = usb.busses()
        ##for bus in busses:
        ##    devices = bus.devices
        ##    for dev in devices:
        ##        print("Device:", dev.filename)
        ##        print("  idProduct: %d (ox%o4x)" % (dev.idProduct, dev.idProduct))
        ##        print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
        DrivesConnected = len(os.listdir("/media/pi"))
        DrivesConnected = os.listdir("/media/pi")
        print(DrivesConnected)
        #ExportWindow.tkraise()
        NoDrivesConnected = len(os.listdir("/media/pi"))
        if NoDrivesConnected == 0:
            ExportWindow.lower()
            messagebox.showinfo("Error", "No USB drive detected")
            ExportWindow.tkraise()
        elif NoDrivesConnected > 1:
            ExportWindow.lower()
            messagebox.showinfo("Error", "Multiple USB drives detected")
            ExportWindow.tkraise()
        elif NoDrivesConnected == 1:
            DrivesConnected = str(os.listdir("/media/pi"))
            PathtoUSB = "/media/pi/" + DrivesConnected[2:-2]
            ExportWindow.lower()
            messagebox.showinfo("Success", "USB drive detected")
            ExportWindow.tkraise()
        DispPath = PathtoUSB[9:]    
        Label2.config(text=DispPath)
    
    def Export_Cancel():
        ExportWindow.destroy()
        
    def Export_Now():
        PlsWait['text'] = "Please Wait..."
        PlsWait.update()
        if PDFVar.get() == 1:
            if Label2.cget("text") != "Not Set":
                # generate a monthly report from CSV data sets and copy to USB drive
                StartDate = datetime.strptime(Choose_start.get(), '%d/%m/%Y')
                ggg = StartDate
                SourceFile = DataPath+(str(ggg.strftime("%m%Y"))+'.csv')
                
                MakeReport(SourceFile,str(ggg.strftime("%m%Y")))
                src = str(ggg.strftime("%m%Y"))+"_"+Plant_ID+"_Monthly Report.pdf"
                dst = PathtoUSB
                shutil.copy(src, dst)
                ExportWindow.lower()
                messagebox.showinfo("DONE", "PDF report saved to USB drive")
                ExportWindow.tkraise()
            else:
                # no file location selected for export
                ExportWindow.lower()
                messagebox.showinfo("ERROR", "No destination folder selected")
                ExportWindow.tkraise()
                
        if CSVVar.get() == 1:
            if Label2.cget("text") != "Not Set":
                # caluclate how many days from start date to end date for loop size
                StartDate = datetime.strptime(Choose_start.get(), '%d/%m/%Y')
                EndDate = datetime.strptime(Choose_end.get(), '%d/%m/%Y')
                NoOfDays = EndDate - StartDate
                DaysMissed = 0
                ggg = StartDate
                for i in range(1, ((NoOfDays.days)+2)):
                    # create file names for chosen date range
                    # copy files to selected folder
                    src = (str(ggg.strftime("%m%d%Y"))+'.csv')
                    dst = Label2.cget("text")
                    if os.path.isfile(src) == False:
                        DaysMissed += 1
                    else:
                        shutil.copy(src, dst)
                    ggg = StartDate + timedelta(days=i)
                    #ggg = StartDate + datetime.timedelta(days=i)
                # loop round to next date
                ExportWindow.lower()
                if DaysMissed == 0:
                    messagebox.showinfo("DONE", "Data exported to USB drive")
                    ExportWindow.tkraise()
                else:
                    messagebox.showinfo("EXPORT ERROR", str(DaysMissed)+" days of data could not be found")
                    ExportWindow.tkraise()
                    
                # Now do monthly export    
                # caluclate how many months from start date to end date for loop size
                StartDate = datetime.strptime(Choose_start.get(), '%d/%m/%Y')
                EndDate = datetime.strptime(Choose_end.get(), '%d/%m/%Y')
                NoOfDays = EndDate - StartDate
                DaysMissed = 0
                ggg = StartDate
                NoOfMonths = (math.ceil(((NoOfDays.days)+2)/31)+1)
                for i in range(1, (NoOfMonths)):
                    # create file names for chosen date range
                    # copy files to selected folder
                    src = (str(ggg.strftime("%m%Y"))+'.csv')
                    dst = Label2.cget("text")
                    if os.path.isfile(src) == False:
                        DaysMissed += 1
                    else:
                        shutil.copy(src, dst)
                    ggg = StartDate + datetime.timedelta(days=i)
                # loop round to next date
                ExportWindow.lower()
                if DaysMissed == 0:
                    messagebox.showinfo("DONE", "Data exported to USB drive")
                    ExportWindow.tkraise()
                else:
                    messagebox.showinfo("EXPORT ERROR", str(DaysMissed)+" months of data could not be found")
                    ExportWindow.tkraise()
                
                # Now do Alarm Log export    
                # caluclate how many months from start date to end date for loop size
                StartDate = datetime.strptime(Choose_start.get(), '%d/%m/%Y')
                EndDate = datetime.strptime(Choose_end.get(), '%d/%m/%Y')
                NoOfDays = EndDate - StartDate
                DaysMissed = 0
                ggg = StartDate
                NoOfMonths = (math.ceil(((NoOfDays.days)+2)/31)+1)
                for i in range(1, (NoOfMonths)):
                    # create file names for chosen date range
                    # copy files to selected folder
                    src = (str(ggg.strftime("%m%Y"))+'Alarms.csv')
                    dst = Label2.cget("text")
                    if os.path.isfile(src) == False:
                        DaysMissed += 1
                    else:
                        shutil.copy(src, dst)
                    ggg = StartDate + datetime.timedelta(days=i)
      
                ExportWindow.destroy()
            else:
                # no file location selected for export
                ExportWindow.lower()
                messagebox.showinfo("ERROR", "No destination folder selected")
                ExportWindow.tkraise()
        PlsWait['text'] = "   "    
    
    ExportWindow = Toplevel(root)
    ExportWindow.title("Export Data to USB drive")
    # Screen GUI setup
    Frame1 = Frame(ExportWindow, bd=2, padx=10, pady=1, relief=SUNKEN)
    Frame1.pack(expand=True, side=TOP, fill=BOTH)
    Frame2 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame2.pack(expand=True, side=TOP, fill=BOTH)
    Frame3 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame3.pack(expand=True, side=TOP, fill=BOTH)
    Frame3_5 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame3_5.pack(expand=True, side=TOP, fill=BOTH)
    Frame4 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame4.pack(expand=True, side=TOP, fill=BOTH)
    Frame5 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame5.pack(expand=True, side=TOP, fill=BOTH)
    Frame6 = Frame(Frame1, bd=2, padx=10, pady=1, relief=FLAT)
    Frame6.pack(expand=True, side=TOP, fill=BOTH)
    #Frame2    
    Label1 = Label(Frame2, text="Select Start Date for export", padx=10, pady=10)
    Label1.pack(side=LEFT)
    Choose_start = DateEntry(Frame2, padx=10, pady=10, width=12)
    Choose_start.pack(side=LEFT)
    #Frame3    
    #Label1 = Label(Frame3, text="Select End Date for export (for CSV reports only)", wraplength= 180,padx=10, pady=10)
    #Label1.pack(side=LEFT)
    #Choose_end = DateEntry(Frame3, padx=10, pady=10, width=12)
    #Choose_end.pack(side=LEFT)
    
    #Frame3_5 - What report type CSV or PDF?
    CSVVar = IntVar()
    PDFVar = IntVar()
    #CSV_Active = Checkbutton(Frame3_5, text="CSV raw data", variable=CSVVar, onvalue=1, offvalue=0, padx=4, pady=1)
    #CSV_Active.pack(expand=True, side=LEFT, fill=BOTH)
    PDF_Active = Checkbutton(Frame3_5, text="PDF Monthly Report", variable=PDFVar, onvalue=1, offvalue=0, padx=4, pady=1)
    PDF_Active.pack(expand=True, side=LEFT, fill=BOTH)
    PDF_Active.select()
    
    #Frame4    
    Button1 = Button(Frame4, text="Click to confirm USB drive inserted", padx=10, pady=10, command=Export_Clicked, bg=ButtonColour)
    Button1.pack(side=TOP)
    PlsWait = Label(Frame4, text="   ", padx=10, pady=10)
    PlsWait.pack(side=LEFT)
    #ReportProgress = ttk.Progressbar(Frame4, orient=HORIZONTAL, length=100, mode = 'indeterminate')
    #ReportProgress.pack(expand=True)
    #Frame5
    Label1_5 = Label(Frame5, text="Destination folder - ", padx=10, pady=10)
    Label1_5.pack(side=LEFT)
    Label2 = Label(Frame5, text="Not Set", padx=10, pady=10)
    Label2.pack(side=LEFT)
    #Frame6    
    Button2 = Button(Frame6, text="EXPORT NOW", padx=10, pady=10, command=Export_Now, bg=ButtonColour)
    Button2.pack(side=LEFT)
    Button3 = Button(Frame6, text="CANCEL", padx=10, pady=10, command=Export_Cancel, bg=ButtonColour)
    Button3.pack(side=LEFT)
    Button4 = Button(Frame6, text="EJECT USB", padx=10, pady=10, command=Eject, bg=ButtonColour)
    Button4.pack(side=LEFT)
    
def ConfigGraph():
    global XMin
    global YMin
    global XMax
    global YMax
    global ButtonColour
    global TempXMin
    global TempXMax
    global SavePath
    TempXMin = XMin
    TempXMax = XMax
    
    def XminUp():
        global TempXMin
        TempXMin += 1
        XaxisMin.delete(0,"end")
        XaxisMin.insert(0,TempXMin)
        
    def XminDwn():
        global TempXMin
        TempXMin -= 1
        XaxisMin.delete(0,"end")
        XaxisMin.insert(0,TempXMin)
    
    def XmaxDwn():
        global TempXMax
        TempXMax -= 1
        XaxisMax.delete(0,"end")
        XaxisMax.insert(0,TempXMax)

    def XmaxUp():
        global TempXMax
        TempXMax += 1
        XaxisMax.delete(0,"end")
        XaxisMax.insert(0,TempXMax)
        
    def YminUp():
        global YMin
        YMin += 1
        YaxisMin.delete(0,"end")
        YaxisMin.insert(0,YMin)
        
    def YminDwn():
        global YMin
        YMin -= 1
        YaxisMin.delete(0,"end")
        YaxisMin.insert(0,YMin)
    
    def YmaxDwn():
        global YMax
        YMax -= 1
        YaxisMax.delete(0,"end")
        YaxisMax.insert(0,YMax)

    def YmaxUp():
        global YMax
        YMax += 1
        YaxisMax.delete(0,"end")
        YaxisMax.insert(0,YMax)
        
    def GraphDone():
        global XMin
        global XMax
        global YMin
        global YMax
        global SavePath
     
        if XMin != int(XaxisMin.get()):
            SetGraphWindow.lower()
            response = messagebox.askokcancel("Clear Plot", "Changing the time axis will clear the grapgh, Continue?")
            SetGraphWindow.tkraise()
            if response == TRUE:    
                ClearGraph()
                XMin = int(XaxisMin.get())
        if XMax != int(XaxisMax.get()):
            SetGraphWindow.lower()
            response = messagebox.askokcancel("Clear Plot", "Changing the time axis will clear the grapgh, Continue?")
            SetGraphWindow.tkraise()
            if response == TRUE:    
                ClearGraph()
                XMax = int(XaxisMax.get())
        YMin = int(YaxisMin.get())
        YMax = int(YaxisMax.get())
        
        checked = 0
        
        try:
            value = int(XMin)
        except ValueError:
            SetGraphWindow.lower()
            messagebox.showinfo("ERROR", "X axis Min value error")
            SetGraphWindow.tkraise()
        else:
            checked = checked + 1
            if int(XMin) < 1 and int(XMin) > -1:
                checked = checked + 1
            else:
                SetGraphWindow.lower()
                messagebox.showinfo("ERROR", "X axis Min value must be zero")
                SetGraphWindow.tkraise()
        
        try:
            value = int(XMax)
        except ValueError:
            SetGraphWindow.lower()
            messagebox.showinfo("ERROR", "X axis Max value error")
            SetGraphWindow.tkraise()
        else:
            checked = checked + 1
            if int(XMax) < 121 and int(XMax) > 1:
                checked = checked + 1
            else:
                SetGraphWindow.lower()
                messagebox.showinfo("ERROR", "X axis Max value >120 or <2")
                SetGraphWindow.tkraise()
                
        try:
            value = int(YMin)
        except ValueError:
            SetGraphWindow.lower()
            messagebox.showinfo("ERROR", "Y axis Min value error")
            SetGraphWindow.tkraise()
        else:
            checked = checked + 1
            if int(YMin) < 99999 and int(YMin) > -9999:
                checked = checked + 1
            else:
                SetGraphWindow.lower()
                messagebox.showinfo("ERROR", "Y axis Min value >99999 or <-9999")
                SetGraphWindow.tkraise()
                
        try:
            value = int(YMax)
        except ValueError:
            SetGraphWindow.lower()
            messagebox.showinfo("ERROR", "Y axis Max value error")
            SetGraphWindow.tkraise()
        else:
            checked = checked + 1
            if int(YMax) < 99999 and int(XMax) > YMin:
                checked = checked + 1
            else:
                SetGraphWindow.lower()
                messagebox.showinfo("ERROR", "Y axis Max value >99999 or Y avix Min value")
                SetGraphWindow.tkraise()
        
        if checked == 8:            
            FileName = SavePath + 'settings.data'
            fd = open(FileName, 'rb')
            newdataset = pickle.load(fd)
            fd.close()
          
            newdataset[27] = XMin
            newdataset[28] = XMax
            newdataset[29] = YMin
            newdataset[30] = YMax
            Outputdataset = newdataset
            fw = open(FileName, 'wb')
            pickle.dump(Outputdataset, fw)
            fw.close()
            
            SetGraphWindow.destroy()

#SettingsWindow.protocol("WM_DELETE_WINDOW", Set_closing)
    
    SetGraphWindow = Toplevel(root)
    SetGraphWindow.title("CONFIGURE GRAPH")
        
    # Cal screen GUI setup
    MainFrame = Frame(SetGraphWindow, bd=2, padx=5, pady=5, relief=SUNKEN)
    MainFrame.pack(expand=True, side=TOP, fill=BOTH)
    MessageFrame = Frame(MainFrame, bd=2, padx=5, pady=5, relief=SUNKEN)
    MessageFrame.pack(expand=True, side=TOP, fill=BOTH)
    Frame1 = Frame(MainFrame, bd=2, padx=10, pady=1, relief=FLAT)
    Frame1.pack(expand=True, side=TOP, fill=BOTH)
    Frame2 = Frame(MainFrame, bd=2, padx=10, pady=1, relief=FLAT)
    Frame2.pack(expand=True, side=TOP, fill=BOTH)
    Frame3 = Frame(MainFrame, bd=2, padx=10, pady=1, relief=FLAT)
    Frame3.pack(expand=True, side=TOP, fill=BOTH)
    Frame4 = Frame(MainFrame, bd=2, padx=10, pady=1, relief=FLAT)
    Frame4.pack(expand=True, side=TOP, fill=BOTH)
    Frame5 = Frame(MainFrame, bd=2, padx=10, pady=1, relief=FLAT)
    Frame5.pack(expand=True, side=TOP, fill=BOTH)
    
    #MessageFrame
    NoteLabel = Label(MessageFrame, text="NOTE - Changing the time axis will reset the graph", padx=10, pady=10)
    NoteLabel.pack(side=LEFT)
    #Frame1    
    Label1 = Label(Frame1, text="Time axis Minimum", width = 18, padx=10, pady=10)
    Label1.pack(side=LEFT)
    Button1 = Button(Frame1, text="-", padx=10, pady=10, command=XminDwn, bg=ButtonColour)
    Button1.pack(side=LEFT)
    Button2 = Button(Frame1, text="+", padx=10, pady=10, command=XminUp, bg=ButtonColour)
    Button2.pack(side=LEFT)
    XaxisMin = Entry(Frame1, width = 5)
    XaxisMin.pack(expand=True, side=LEFT, fill=BOTH)
    XaxisMin.bind("<1>", (lambda event: NumPad(XaxisMin)))
    XaxisMin.insert(0,XMin)
    
    #Frame2
    Label2 = Label(Frame2, text="Time axis Maximum", width = 18, padx=10, pady=10)
    Label2.pack(side=LEFT)
    Button3 = Button(Frame2, text="-", padx=10, pady=10, command=XmaxDwn, bg=ButtonColour)
    Button3.pack(side=LEFT)
    Button4 = Button(Frame2, text="+", padx=10, pady=10, command=XmaxUp, bg=ButtonColour)
    Button4.pack(side=LEFT)
    XaxisMax = Entry(Frame2, width = 5)
    XaxisMax.pack(expand=True, side=LEFT, fill=BOTH)
    XaxisMax.bind("<1>", (lambda event: NumPad(XaxisMax)))
    XaxisMax.insert(0,XMax)
    
    #Frame3    
    Label3 = Label(Frame3, text="Y-axis Minimum", width = 18, padx=10, pady=10)
    Label3.pack(side=LEFT)
    Button5 = Button(Frame3, text="-", padx=10, pady=10, command=YminDwn, bg=ButtonColour)
    Button5.pack(side=LEFT)
    Button6 = Button(Frame3, text="+", padx=10, pady=10, command=YminUp, bg=ButtonColour)
    Button6.pack(side=LEFT)
    YaxisMin = Entry(Frame3, width = 5)
    YaxisMin.pack(expand=True, side=LEFT, fill=BOTH)
    YaxisMin.bind("<1>", (lambda event: NumPad(YaxisMin)))
    YaxisMin.insert(0,YMin)
    
    #Frame4
    Label4 = Label(Frame4, text="Y-axis Maximum", width = 18, padx=10, pady=10)
    Label4.pack(side=LEFT)
    Button7 = Button(Frame4, text="-", padx=10, pady=10, command=YmaxDwn, bg=ButtonColour)
    Button7.pack(side=LEFT)
    Button8 = Button(Frame4, text="+", padx=10, pady=10, command=YmaxUp, bg=ButtonColour)
    Button8.pack(side=LEFT)
    YaxisMax = Entry(Frame4, width = 5)
    YaxisMax.pack(expand=True, side=LEFT, fill=BOTH)
    YaxisMax.bind("<1>", (lambda event: NumPad(YaxisMax)))
    YaxisMax.insert(0,YMax)
    
    #Frame5
    Button9 = Button(Frame5, text="DONE", padx=10, pady=10, command=GraphDone, bg=ButtonColour)
    Button9.pack(side=TOP)
    
def LogOnOff():    
    global RunOn
    global Alarm
    global Output1List
    global Output2List
    global Output3List
    global Output4List
    global Output5List
    global Output6List
    global Output7List
    global Output8List
    global p
    global EcomInStdby
    global Ecom_Mode
    
    def StopLog():
        global RunOn
        global Alarm
        global Output1List
        global Output2List
        global Output3List
        global Output4List
        global Output5List
        global Output6List
        global Output7List
        global Output8List
        global p
        global EcomInStdby
        global Ecom_Mode
        ButtonA['image'] = StartImage
        RunOn = 0
        ClearGraph()
        Output1List.clear()
        Output2List.clear()
        Output3List.clear()
        Output4List.clear()
        Output5List.clear()
        Output6List.clear()
        Output7List.clear()
        Output8List.clear()
        AlarmFlag['text'] = "Stopped"
        AlarmDesc['text'] = "ALARM"
        AlarmFlag['bg'] = "red"
        AlarmFrame.update()
        Alarm = 1
    
    if RunOn == 0:
        ButtonA['image'] = StopImage
        #ButtonA['text'] = "Stop Logging"
        #messagebox.showinfo("Logger", "Logger Running")
        # Put Ecom in Measure mode
        connection = client.connect()
        if connection:
            if Ecom_Mode == "O" or Ecom_Mode == "P":
                rq = client.write_register(0x0022,1, unit=2)
                Ecom_Mode = "M"
                StatusEcom['text']="M"
                StatusEcom['bg'] = "green"
                
            client.close
            EcomInStdby = 0
            # messagebox.showinfo("INFO", "Startup takes 60 seconds, please confirm")
            time.sleep(2)
        else:
            print("No Modbus connection, Unable to put Ecom in Measure mode")    
            
        RunOn = 1
        AlarmFlag['text'] = "Active"
        AlarmDesc['text'] = "NORMAL"
        AlarmFlag['bg'] = "green"
        AlarmFrame.update()
        Alarm = 0
        if Slave_ID != 0:
            print("Starting Modbus RTU client for site connection")
            #run_update_Modbus_Server()
             
        task()
    else:
        
        response = messagebox.askokcancel("Logger", "Stop the logger, Are you Sure? (this will also resst the data plot)")
        if response == TRUE:
            CheckUserPassword(StopLog)

# define what to do every second
def task():
    global RunOn
    global PlotSecs
    global CycleSoFar
    global TimeList
    global Data1List
    global Data2List
    global Data3List
    global Data4List
    global Data5List
    global Data6List
    global Data7List
    global Data8List
    global Output1List
    global Output2List
    global Output3List
    global Output4List
    global Output5List
    global Output6List
    global Output7List
    global Output8List
    global AverageTime
    global CH1MinAlarm
    global CH2MinAlarm
    global CH3MinAlarm
    global CH4MinAlarm
    global CH5MinAlarm
    global CH6MinAlarm
    global CH7MinAlarm
    global CH8MinAlarm
    global CH1MaxAlarm
    global CH2MaxAlarm
    global CH3MaxAlarm
    global CH4MaxAlarm
    global CH5MaxAlarm
    global CH6MaxAlarm
    global CH7MaxAlarm
    global CH8MaxAlarm
    global Ch1MinAlOn
    global Ch2MinAlOn
    global Ch3MinAlOn
    global Ch4MinAlOn
    global Ch5MinAlOn
    global Ch6MinAlOn
    global Ch7MinAlOn
    global Ch8MinAlOn
    global Ch1MaxAlOn
    global Ch2MaxAlOn
    global Ch3MaxAlOn
    global Ch4MaxAlOn
    global Ch5MaxAlOn
    global Ch6MaxAlOn
    global Ch7MaxAlOn
    global Ch8MaxAlOn
    global AlarmSilent
    global Ch1Active
    global Ch2Active
    global Ch3Active
    global Ch4Active
    global Ch5Active
    global Ch6Active
    global Ch7Active
    global Ch8Active
    global Daily_Files
    global Monthly_Files
    global PiHat
    global XMin
    global XMax
    global YMin
    global YMax
    global FirstRound
    global CH1DispName
    global CH2DispName
    global CH3DispName
    global CH4DispName
    global CH5DispName
    global CH6DispName
    global CH7DispName
    global CH8DispName
    global CH1Offset
    global CH1Slope
    global CH2Offset
    global CH2Slope
    global CH3Offset
    global CH3Slope
    global CH4Offset
    global CH4Slope
    global CH5Offset
    global CH5Slope
    global CH6Offset
    global CH6Slope
    global CH7Offset
    global CH7Slope
    global CH8Offset
    global CH8Slope
    global CH14mA
    global CH120mA
    global CH24mA
    global CH220mA
    global CH34mA
    global CH320mA
    global CH44mA
    global CH420mA
    global CH54mA
    global CH520mA
    global CH64mA
    global CH620mA
    global CH74mA
    global CH720mA
    global CH84mA
    global CH820mA
    global AlarmCode
    global O21Correct
    global O22Correct
    global O23Correct
    global O24Correct
    global O25Correct
    global O26Correct
    global O27Correct
    global O28Correct
    global O2Ref
    global Ch1Units
    global Ch2Units
    global Ch3Units
    global Ch4Units
    global Ch5Units
    global Ch6Units
    global Ch7Units
    global Ch8Units
    global SavePath
    global volt1
    global volt2
    global volt3
    global volt4
    global volt5
    global volt6
    global volt7
    global volt8
    global EcomHolding
    global HoldStart
    global EcomInStdby
    global holdvolt1
    global holdvolt2
    global holdvolt3
    global holdvolt4
    global holdvolt5
    global holdvolt6
    global holdvolt7
    global holdvolt8
    global MeasPurge_Counter
    global Ecom_Mode
    
    MCPAlarmCode = "0000000000000000"
    EcomFault = 0

    #TaskStart = (datetime.now(tz=None))
    LogInt = 15 #in seconds
    #set sofwtare scan time in ms
    ScanTime = LogInt*1000
    
    if RunOn == 1:
        root.after(ScanTime, task)  # reschedule event in 'ScanTime' seconds 
    
    #Log how many minutes since start of cycle
    CycleSoFar += (ScanTime/(LogInt*1000))*(LogInt/60)
    # add 1 to the purge / measure counter
    MeasPurge_Counter += (ScanTime/(LogInt*1000))*(LogInt/60)
    # Check on status of Modbus RTU server
    if Ecom_Mode == "S":
        MeasPurge_Counter = 0
    #print("Ecom Mode - "+ Ecom_Mode)
    #print("Purge Counter - "+ str(MeasPurge_Counter))
    
    if ModServer.is_alive() == True:
        StatusRTU['image'] = StatusGreen
    else:
        StatusRTU['image'] = StatusRed
    
    ####### Add code here to read in Modbus values if Modbus TCP is in use to get data from analysers  #######
    
    if Slave_ID != 0:
        Current_Status = "No Comms"
        connection = client.connect()
        EcomData = 0
        if connection:
            EcomData = 1
            request = client.read_holding_registers(0x3000, 10, unit = TCP_ID)
            #print("Air Temp - " + str(request.registers[1]/10))
            #print("Gas Temp - " + str(request.registers[2]/10))    
            #print("Sensor Temp - " + str(request.registers[3]/10))
            #print("O2 (%) - " + str(request.registers[4]/100))
            #print("CO (ppm) - " + str(request.registers[5]))
            #print("NO (ppm) - " + str(request.registers[6]/10))
            #print("NO2 (ppm) - " + str(request.registers[7]/10))
            #print("SO2 (ppm) - " + str(request.registers[8]/10))
            #print("CH4 (ppm) - " + str(request.registers[9]))
            Status_request = client.read_holding_registers(0x1006, 1, unit = TCP_ID)
            
            ModbusIn1 = int(request.registers[Mod1Reg])
            ModbusIn2 = int(request.registers[Mod2Reg])
            ModbusIn3 = int(request.registers[Mod3Reg])
            ModbusIn4 = int(request.registers[Mod4Reg])
            ModbusIn5 = int(request.registers[Mod5Reg])
            ModbusIn6 = int(request.registers[Mod6Reg])
            ModbusIn7 = int(request.registers[Mod7Reg])
            ModbusIn8 = int(request.registers[Mod8Reg])


            MCPAlarmCode = MCPAlarmCode[:3] + "0" + MCPAlarmCode[-12:]
            #if Status_request.registers[0] == 1:
            #    Current_Status = "Automatic Mode"
            #elif Status_request.registers[0] == 256:
            #    Current_Status = "Auto-Zero Active"
            #elif Status_request.registers[0] == 512 or Status_request.registers[0] == 513:
            #    Current_Status = "Auto-Zero done"
            #elif Status_request.registers[0] == 1024:
            #    Current_Status = "Measurement pump Active"
            #elif Status_request.registers[0] == 2048:
            #    Current_Status = "Flue gas input activated"
            #elif Status_request.registers[0] == 4096 or Status_request.registers[0] == 4097:
            #    Current_Status = "Standby or Purging"    
            if Status_request.registers[0] == 8192 or Status_request.registers[0] == 8193:
                Current_Status = "In Shut down mode"
                MCPAlarmCode = MCPAlarmCode[:3] + "1" + MCPAlarmCode[-12:]
            elif Status_request.registers[0] == 16384:
                Current_Status = "System Failure"
                MCPAlarmCode = MCPAlarmCode[:3] + "1" + MCPAlarmCode[-12:]
            elif Status_request.registers[0] == 32768:
                Current_Status = "Semi-continuous purge mode active"
            else:
                Current_Status = str(Status_request.registers[0])
            
            print("Ecom Status - "+Current_Status)
            
            # #### Break out Ecom fault signals from ststus code
            # x 0001 = bit 1 = Auto mode running
            # x 0100 = bit 9 = Auto Zero Running
            # x 0200 = bit 10 = Auto Zero finished
            # x 0400 = bit 11 = Pump on
            # x 0800 = bit 12 = measuring Flue gas
            # x 1000 = bit 13 = Stanby or purging
            # x 2000 = bit 14 = In shutdown mode
            # x 4000 = bit 15 = System failure
            # x 8000 = bit 16 = Semi continuous purge mode
            StatCodeDec = Status_request.registers[0]
            #StatCodeBin = bin(StatCodeDec)
            StatCodeBin = '{0:16b}'.format(StatCodeDec)
            #print("Bin - " + str(StatCodeBin))
            EcomFault = 0 
            if StatCodeBin[0:1] == "1":
                print("Semi continuous purge mode")
            if StatCodeBin[1:2] == "1":
                print("System failure")
                EcomFault += 1
            if StatCodeBin[2:3] == "1":
                print("In shutdown mode")
                EcomFault += 1
                # Override the Ecom Shutdown!
                AlarmFlag['bg'] = "yellow"
                AlarmFrame.update()
                
                rq = client.write_register(0x0025,1, unit=2)
                Ecom_Mode = "M"
            if StatCodeBin[3:4] == "1":
                print("Standby or Purging")
            if StatCodeBin[4:5] == "1":
                print("measuring Flue gas")
            if StatCodeBin[5:6] == "1":
                print("Pump on")
            if StatCodeBin[6:7] == "1":
                print("Auto Zero finished")
            if StatCodeBin[7:8] == "1":
                print("Auto Zero Running")
            if StatCodeBin[14:15] == "1":
                print("Automatic Mode")
                EcomFault += 1
            
            #client = ModbusTcpClient('192.168.55.1', port = 502)
            #print("Status - " + str(Status_request.registers[1]))
            # code below puts Ecom in Standby
            #rq = client.write_register(0x0025,1, unit=2)

            # code below puts Ecom in Measure mode
            #rq = client.write_register(0x0022,1, unit=2)
            client.close
        else:
            StatCodeDec = 0
            StatCodeBin = '{0:16b}'.format(StatCodeDec)
            print("No TCP Modbus connection, Trying again")
            MCPAlarmCode = MCPAlarmCode[:2] + "1" + MCPAlarmCode[-13:]
            ModbusIn1 = 0
            ModbusIn2 = 0
            ModbusIn3 = 0
            ModbusIn4 = 0
            ModbusIn5 = 0
            ModbusIn6 = 0
            ModbusIn7 = 0
            ModbusIn8 = 0
    
    
    # Code here deals with Ecom status, purge requests & updating Plant status icon
    #If current Stack Temp > setpoint then flag plant as running
    if (int(ModbusIn2) / 10) > int(Run_If_Temp):
        #print("########## plant on identified")
        #print(EcomInStdby)
        StatusPlant['image'] = StatusGreen
        PlantStat = 1
        # Put Ecom in Measure mode
        # BUT - only if within Meas_Time not Purge_Time
        if 1 == 1:
            connection = client.connect()
            if connection:
                if Ecom_Mode == "S":
                    if StatCodeBin[7:8] != "1":
                        # Auto Zero Running
                        # if going from Standby to Measure, set held values to zero
                        rq = client.write_register(0x0022,1, unit=2)
                        Ecom_Mode = "M"
                        StatusEcom['text']="M"
                        StatusEcom['bg'] = "green"
                        holdvolt1 = 0
                        holdvolt2 = 0
                        holdvolt3 = 0
                        holdvolt4 = 0
                        holdvolt5 = 0
                        holdvolt6 = 0
                        holdvolt7 = 0
                        holdvolt8 = 0
                if MeasPurge_Counter <= int(Meas_Time):
                    #go to measure mode
                    if StatCodeBin[7:8] != "1":
                        # Auto Zero Running
                        if Ecom_Mode == "O" or Ecom_Mode == "P" or Ecom_Mode == "S":
                            
                            rq = client.write_register(0x0022,1, unit=2)
                            Ecom_Mode = "M"
                            StatusEcom['text']="M"
                            StatusEcom['bg'] = "green"
                elif MeasPurge_Counter <= (int(Meas_Time)+int(Purge_Time)) and MeasPurge_Counter > int(Meas_Time):
                    # go to purge mode (if not already in it)
                    if Ecom_Mode == "O" or Ecom_Mode == "M":
                        if StatCodeBin[7:8] != "1":
                        # Auto Zero Running
                            rq = client.write_register(0x0025,1, unit=2)
                            Ecom_Mode = "P"
                            StatusEcom['text']="P"
                            StatusEcom['bg'] = "green"
                elif MeasPurge_Counter <= (int(Meas_Time)+int(Purge_Time)+(float(Dwell_Time)/60)) and MeasPurge_Counter > (int(Meas_Time)+int(Purge_Time)):
                    if Ecom_Mode == "P":
                        if StatCodeBin[7:8] != "1":
                        # Auto Zero Running
                            rq = client.write_register(0x0022,1, unit=2)
                            Ecom_Mode = "D"
                            StatusEcom['text']="D"
                            StatusEcom['bg'] = "green"
                if MeasPurge_Counter >= (int(Meas_Time) + int(Purge_Time) + (float(Dwell_Time)/60)):
                    # if at end of purge cycle, reset the counter
                    MeasPurge_Counter = 0
                    Ecom_Mode = "M"
                    StatusEcom['text']="M"
                    StatusEcom['bg'] = "green"
                client.close
            else:
                print("No Modbus connection, Unable to put Ecom in Measure mode")    
            
    else:
        StatusPlant['image'] = StatusRed
        PlantStat = 0
        # Put Ecom in Standby mode
        if Ecom_Mode == "M" or Ecom_Mode == "P" or Ecom_Mode == "O" or Ecom_Mode == "D":
            if StatCodeBin[7:8] != "1":
            # Auto Zero Running
                #rq = client.write_register(0x0025,1, unit=2)
                #Ecom_Mode = "S"
                #StatusEcom['text']="S"
                #StatusEcom['bg'] = "green"
                connection = client.connect()
                if connection:
                    if Ecom_Mode == "M" or Ecom_Mode == "O" or Ecom_Mode == "P" or Ecom_Mode == "D":
                        rq = client.write_register(0x0025,1, unit=2)
                        Ecom_Mode = "S"
                        StatusEcom['text']="S"
                        StatusEcom['bg'] = "red"
                        MeasPurge_Counter = 0
                    client.close
                else:
                    print("No Modbus connection, Unable to put Ecom in Standby mode")   
            
    # Check if O2 is above 19.5%, if so, mark plant as off in logged data (but keep Ecom sampling until stack is cool
    if (int(ModbusIn3) / 100) > 19.5:
        StatusPlant['image'] = StatusRed
        PlantStat = 0

    # update plot across the YMax time span

    if PlotSecs > XMax:
        FirstRound = 1
        PlotSecs = 0
        #del Data1List[0:len(Data1List)]
        #del Data2List[0:len(Data2List)]
        #del Data3List[0:len(Data3List)]
        #del Data4List[0:len(Data4List)]
        #del TimeList[0:len(TimeList)]
        # del OutputList[0:len(OutputList)]
    if PiHat == "CUSTARD":
        
        # This section reads in the analogue value from CH1 of Custard Pi
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(21, GPIO.IN)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        GPIO.output(24, True)
        GPIO.output(23, False)
        GPIO.output(19, True)

        word1= [1, 1, 1, 1, 1]

        GPIO.output(24, False)
        anip=0

        for x in range (0,5):
            GPIO.output(19, word1[x])
            time.sleep(0.01)
            GPIO.output(23, True)
            time.sleep(0.01)
            GPIO.output(23, False)
        
        for x in range (0,12):
            GPIO.output(23,True)
            time.sleep(0.01)
            bit=GPIO.input(21)
            time.sleep(0.01)
            GPIO.output(23,False)
            value=bit*2**(12-x-1)
            anip=anip+value
        
        GPIO.output(24, True)
    # Final result as volts (will need scaling to suit sensor)
        volt = anip*3.3/4096
    
    elif PiHat == "SEEED":
        values = [0]*4
        GAIN = 1
        for i in range(4):
            # Read the specified ADC channel using the previously set gain value.
            values[i] = adc1.read_adc(i, gain=GAIN)
            
        # Print the ADC values.
        #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        volt1 = int('{0:>6}'.format(*values))
        volt2 = int('{1:>6}'.format(*values))
        volt3 = int('{2:>6}'.format(*values))
        volt4 = int('{3:>6}'.format(*values))
        values = [0]*4
        GAIN = 1
        if FTBoards_Installed == 2: 
            for i in range(4):
                # Read the specified ADC channel using the previously set gain value.
                values[i] = adc2.read_adc(i, gain=GAIN)
                
            # Print the ADC values.
            #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
            volt5 = int('{0:>6}'.format(*values))
            volt6 = int('{1:>6}'.format(*values))
            volt7 = int('{2:>6}'.format(*values))
            volt8 = int('{3:>6}'.format(*values))
        else:
            volt5 = 0
            volt6 = 0
            volt7 = 0
            volt8 = 0
                
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Add code for sclaing of data to volts and sclaing for 4-20mA
    
    #convert using calibration data
    volt1 = ((volt1*CH1Slope)+CH1Offset)
    volt2 = ((volt2*CH2Slope)+CH2Offset)
    volt3 = ((volt3*CH3Slope)+CH3Offset)
    volt4 = ((volt4*CH4Slope)+CH4Offset)
    volt5 = ((volt5*CH5Slope)+CH5Offset)
    volt6 = ((volt6*CH6Slope)+CH6Offset)
    volt7 = ((volt7*CH7Slope)+CH7Offset)
    volt8 = ((volt8*CH8Slope)+CH8Offset)
    
    #CH14mA
    # convert for 4-20mA range
    volt1 = round(((volt1-4)/16*CH120mA),2)
    volt2 = round(((volt2-4)/16*CH220mA),2)
    volt3 = round(((volt3-4)/16*CH320mA),2)
    volt4 = round(((volt4-4)/16*CH420mA),2)
    volt5 = round(((volt5-4)/16*CH520mA),2)
    volt6 = round(((volt6-4)/16*CH620mA),2)
    volt7 = round(((volt7-4)/16*CH720mA),2)
    volt8 = round(((volt8-4)/16*CH820mA),2)
    
    #### Change values from 4-20mA values to modbus values if modbus is selected in settings
    #print ("Current Status")
    #print(Current_Status)
    #if Current_Status == "513" and Current_Status == "1281":
    if Current_Status == "3584" or Current_Status == "3585":
        if Ecom_Mode != "D":
            # Ecom is in measure mode
            if Current_Status != "No Comms":
                EcomHolding = 0
            if Ch1Mod == 1:
                volt1 = ModbusIn1/ModCorrect1
                holdvolt1 = volt1
            if Ch2Mod == 1:
                volt2 = ModbusIn2/ModCorrect2
                holdvolt2 = volt2
            if Ch3Mod == 1:
                volt3 = ModbusIn3/ModCorrect3
                holdvolt3 = volt3
            if Ch4Mod == 1:
                volt4 = ModbusIn4/ModCorrect4
                holdvolt4 = volt4
            if Ch5Mod == 1:
                volt5 = ModbusIn5/ModCorrect5
                holdvolt5 = volt5
            if Ch6Mod == 1:
                volt6 = ModbusIn6/ModCorrect6
                holdvolt6 = volt6
            if Ch7Mod == 1:
                volt7 = ModbusIn7/ModCorrect7
                holdvolt7 = volt7
            if Ch8Mod == 1:
                volt8 = ModbusIn8/ModCorrect8
                holdvolt8 = volt8
    if Current_Status == "4096" or Current_Status == "38400" or Current_Status == "513" or Current_Status == "1281" or Current_Status == "1537" or Current_Status == "1280" or Current_Status == "5120" or Ecom_Mode == "D":
        if Ecom_Mode != "S":
            print("Ecom - holding previous data during purge")
            #print(holdvolt3)
            if Ch2Mod == 1:
                volt2 = ModbusIn2/ModCorrect2
                holdvolt2 = volt2
            #volt1 = holdvolt1
            #volt2 = holdvolt2
            volt3 = holdvolt3
            volt4 = holdvolt4
            volt5 = holdvolt5
            volt6 = holdvolt6
            volt7 = holdvolt7
            volt8 = holdvolt8
            # Ecom is busy purging, hold data for up to 10 minutes (DataHold = 10)
            EcomHolding = EcomHolding + 1
            HoldNow = 0
            now = datetime.now()
            HoldStartHr = int(str(now.strftime("%H")))
            HoldStartMin = int(str(now.strftime("%M")))
            if HoldStartHr == 0:
                HoldStartHr = 24
            if EcomHolding == 1:
                HoldStart = (HoldStartHr * 60) + HoldStartMin
            else:
                HoldNow = (HoldStartHr * 60) + HoldStartMin
                #print("Hold Ecom")
                #print(EcomHolding)
                #print(HoldStart)
                #print(HoldNow)
            if HoldNow > HoldStart + DataHold:
                # ecom been in standby too long, stop holding data and alarm
                print("Ecom in purge longer than "+str(DataHold)+" minutes")
                MCPAlarmCode = MCPAlarmCode[:1] + "1" + MCPAlarmCode[-14:]
                    #if Ch1Mod == 1:
                    #    volt1 = 0
                    #if Ch2Mod == 1:
                    #    volt2 = 0
                if Ch1Mod == 1:
                    volt1 = ModbusIn1/ModCorrect1
                if Ch2Mod == 1:
                    volt2 = ModbusIn2/ModCorrect2
                if Ch3Mod == 1:
                    
                    volt3 = 0
                if Ch4Mod == 1:
                    volt4 = 0
                if Ch5Mod == 1:
                    volt5 = 0
                if Ch6Mod == 1:
                    volt6 = 0
                if Ch7Mod == 1:
                    volt7 = 0
                if Ch8Mod == 1:
                    volt8 = 0       
    if Ecom_Mode == "S":
        # Ecom is in Standby becuase plant not operating
        #if Ch1Mod == 1:
        #    volt1 = 0
        #if Ch2Mod == 1:
        #    volt2 = 0
        if Ch1Mod == 1:
            volt1 = ModbusIn1/ModCorrect1
        if Ch2Mod == 1:
            volt2 = ModbusIn2/ModCorrect2
        if Ch3Mod == 1:
            volt3 = 0
        if Ch4Mod == 1:
            volt4 = 0
        if Ch5Mod == 1:
            volt5 = 0
        if Ch6Mod == 1:
            volt6 = 0
        if Ch7Mod == 1:
            volt7 = 0
        if Ch8Mod == 1:
            volt8 = 0
            
    # Set data in tags ready for Modbus tranmission
    CH1_Raw = int(volt1)
    CH2_Raw = int(volt2*10)
    CH3_Raw = int(volt3*100)
    CH4_Raw = int(volt4)
    CH5_Raw = int(volt5*10)
    CH6_Raw = int(volt6*10)
    CH7_Raw = int(volt7*10)
    CH8_Raw = int(volt8)
    
    # Add O2 correction if selected
    O2Data = -10
    # identify which channel holds O2 data
    if CH1DispName == "O2":
        O2Data = volt1
    if CH2DispName == "O2":
        O2Data = volt2
    if CH3DispName == "O2":
        O2Data = volt3
    if CH4DispName == "O2":
        O2Data = volt4
    if CH5DispName == "O2":
        O2Data = volt5
    if CH6DispName == "O2":
        O2Data = volt6
    if CH7DispName == "O2":
        O2Data = volt7
    if CH8DispName == "O2":
        O2Data = volt8
    if O2Data == -10:
        # No O2 data was found    
        messagebox.showinfo("ERROR", "No O2 Data was found to apply corrections with. One channel must be named O2.")
        # apply O2 corrections if channel is marked for correction
    else:
        # if O2 not above a set level - do corrections
        if O2Data < O2CutOff:
            if O21Correct == "Y":
                # do correction 
                volt1 = volt1 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O22Correct == "Y":
                # do correction
                volt2 = volt2 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O23Correct == "Y":
                # do correction
                volt3 = volt3 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O24Correct == "Y":
                # do correction
                volt4 = volt4 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O25Correct == "Y":
                # do correction
                volt5 = volt5 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O26Correct == "Y":
                # do correction
                volt6 = volt6 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O27Correct == "Y":
                # do correction
                volt7 = volt7 * ((20.95-int(O2Ref))/(20.95-O2Data))
            if O28Correct == "Y":
                # do correction
                volt8 = volt8 * ((20.95-int(O2Ref))/(20.95-O2Data))
            
    CH1_Corr = int(volt1)
    CH2_Corr = int(volt2*10)
    CH3_Corr = int(volt3*100)
    CH4_Corr = int(volt4)
    CH5_Corr = int(volt5*10)
    CH6_Corr = int(volt6*10)
    CH7_Corr = int(volt7*10)
    CH8_Corr = int(volt8)  
    
    
    # DEAL WITH ALARMS HERE
    AlarmCount = 0
    AlarmFlag['text'] = ""      
    
    if EcomFault > 0: 
        #Ecom Status Fault
        AlarmCount += 1
        AlarmFlag['text'] += "\n" +"Ecom Operation error"
        AlarmDesc['text'] = "ALARM"
        if AlarmFlag['bg'] != "yellow":
            AlarmFlag['bg'] = "red"
    if MCPAlarmCode[1:2] == "1":
        # Ecom in purge too long
        AlarmCount += 1
        AlarmFlag['text'] += "\n" +"Ecom Purge Error"
        AlarmDesc['text'] = "ALARM"
        AlarmFlag['bg'] = "red"
    if MCPAlarmCode[2:3] == "1":
        # Ecom in purge too long
        AlarmCount += 1
        AlarmFlag['text'] += "\n" +"Ecom Comms Error"
        AlarmDesc['text'] = "ALARM"
        AlarmFlag['bg'] = "red"   
    if MCPAlarmCode[3:4] == "1":
        # Ecom in purge too long
        AlarmCount += 1
        AlarmFlag['text'] += "\n" +"Ecom General Fault"
        AlarmDesc['text'] = "ALARM"
        AlarmFlag['bg'] = "red"
        
        
    CurrentCode = AlarmCode
    # add 1 to alarm count if system is not logging
    if RunOn == 0:
        AlarmCount += 1
        AlarmFlag['text'] += "\n" +"Stopped"
        AlarmDesc['text'] = "ALARM"
        AlarmFlag['bg'] = "red"
        
    if Ch1MaxAlOn == 1:
        if volt1 > int(CH1MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch1 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            #print("CurCode Before -"+CurrentCode)
            CurrentCode = "1" + CurrentCode[-15:]
            #print("CurCode After  -"+CurrentCode)
        else:
            CurrentCode = "0" + CurrentCode[-15:]
        
    if Ch2MaxAlOn == 1:
        if volt2 > int(CH2MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch2 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:1] + "1" + CurrentCode[-14:]
        else:
            CurrentCode = CurrentCode[:1] + "0" + CurrentCode[-14:]
    
    if Ch3MaxAlOn == 1:
        if volt3 > int(CH3MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch3 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:2] + "1" + CurrentCode[-13:]
        else:
            CurrentCode = CurrentCode[:2] + "0" + CurrentCode[-13:]
    
    if Ch4MaxAlOn == 1:
        if volt4 > int(CH4MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch4 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:3] + "1" + CurrentCode[-12:]
        else:
            CurrentCode = CurrentCode[:3] + "0" + CurrentCode[-12:]
            
    if Ch5MaxAlOn == 1:
        if volt5 > int(CH5MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch5 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:4] + "1" + CurrentCode[-11:]
        else:
            CurrentCode = CurrentCode[:4] + "0" + CurrentCode[-11:]
            
    if Ch6MaxAlOn == 1:
        if volt6 > int(CH6MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch6 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:5] + "1" + CurrentCode[-10:]
        else:
            CurrentCode = CurrentCode[:5] + "0" + CurrentCode[-10:]
    
    if Ch7MaxAlOn == 1:
        if volt7 > int(CH7MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch7 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:6] + "1" + CurrentCode[-9:]
        else:
            CurrentCode = CurrentCode[:6] + "0" + CurrentCode[-9:]
    
    if Ch8MaxAlOn == 1:
        if volt8 > int(CH8MaxAlarm):
            AlarmFlag['text'] += "\n" +"Ch8 Max"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:7] + "1" + CurrentCode[-8:]
        else:
            CurrentCode = CurrentCode[:7] + "0" + CurrentCode[-8:]

    if Ch1MinAlOn == 1:
        if volt1 < int(CH1MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch1 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:8] + "1" + CurrentCode[-7:]
        else:
            CurrentCode = CurrentCode[:8] + "0" + CurrentCode[-7:]
                
    if Ch2MinAlOn == 1:
        if volt2 < int(CH2MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch2 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:9] + "1" + CurrentCode[-6:]
        else:
            CurrentCode = CurrentCode[:9] + "0" + CurrentCode[-6:]

    if Ch3MinAlOn == 1:
        if volt3 < int(CH3MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch3 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:10] + "1" + CurrentCode[-5:]
        else:
            CurrentCode = CurrentCode[:10] + "0" + CurrentCode[-5:]
                
    if Ch4MinAlOn == 1:
        if volt4 < int(CH4MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch4 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:11] + "1" + CurrentCode[-4:]
        else:
            CurrentCode = CurrentCode[:11] + "0" + CurrentCode[-4:]
    
    if Ch5MinAlOn == 1:
        if volt5 < int(CH5MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch5 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:12] + "1" + CurrentCode[-3:]
        else:
            CurrentCode = CurrentCode[:12] + "0" + CurrentCode[-3:]
    
    if Ch6MinAlOn == 1:
        if volt6 < int(CH6MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch6 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:13] + "1" + CurrentCode[-2:]
        else:
            CurrentCode = CurrentCode[:13] + "0" + CurrentCode[-2:]
    
    if Ch7MinAlOn == 1:
        if volt7 < int(CH7MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch7 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:14] + "1" + CurrentCode[-1:]
        else:
            CurrentCode = CurrentCode[:14] + "0" + CurrentCode[-1:]
            AlarmCount += 1
    
    if Ch8MinAlOn == 1:
        if volt8 < int(CH8MinAlarm):
            AlarmFlag['text'] += "\n" +"Ch8 Min"
            AlarmDesc['text'] = "ALARM"
            AlarmFlag['bg'] = "red"
            AlarmCount += 1
            CurrentCode = CurrentCode[:15] + "1"
        else:
            CurrentCode = CurrentCode[:15] + "0"
    
    if AlarmCount > 0:
        if UseRelays == 1:
            if AlarmSilent == 0:
                relay_on(1)
        if AlarmSilent == 0:
            alert.play()
    elif AlarmCount == 0:
        AlarmFlag['text'] = "Active"
        AlarmDesc['text'] = "NORMAL"
        AlarmFlag['bg'] = "green"
        if UseRelays == 1:
            relay_off(1)
    
    AlarmFrame.update()
    
    # code to log alarm events
    # first need to check to see if the Alarm code has changed and create a text string to store
    AlarmString = ""

    if CurrentCode[:1] == "1":
        if CurrentCode[:1] != AlarmCode[:1]:
            AlarmString += ", Channel1 High"
    if CurrentCode[1:2] == "1":
        if CurrentCode[1:2] != AlarmCode[1:2]:
            AlarmString += ", Channel2 High"
    if CurrentCode[2:3] == "1":
        if CurrentCode[2:3] != AlarmCode[2:3]:
            AlarmString += ", Channel3 High"
    if CurrentCode[3:4] == "1":
        if CurrentCode[3:4] != AlarmCode[4:4]:
            AlarmString += ", Channel4 High"
    if CurrentCode[4:5] == "1":
        if CurrentCode[4:5] != AlarmCode[4:5]:
            AlarmString += ", Channel5 High"
    if CurrentCode[5:6] == "1":
        if CurrentCode[5:6] != AlarmCode[5:6]:
            AlarmString += ", Channel6 High"
    if CurrentCode[6:7] == "1":
        if CurrentCode[6:7] != AlarmCode[6:7]:
            AlarmString += ", Channel7 High"
    if CurrentCode[7:8] == "1":
        if CurrentCode[7:8] != AlarmCode[7:8]:
            AlarmString += ", Channel8 High"
    if CurrentCode[8:9] == "1":
        if CurrentCode[8:9] != AlarmCode[8:9]:
            AlarmString += ", Channel1 Low"            
    if CurrentCode[9:10] == "1":
        if CurrentCode[9:10] != AlarmCode[9:10]:
            AlarmString += ", Channel2 Low"
    if CurrentCode[10:11] == "1":
        if CurrentCode[10:11] != AlarmCode[10:11]:
            AlarmString += ", Channel3 Low"
    if CurrentCode[11:12] == "1":
        if CurrentCode[11:12] != AlarmCode[11:12]:
            AlarmString += ", Channel4 Low"
    if CurrentCode[12:13] == "1":
        if CurrentCode[12:13] != AlarmCode[12:13]:
            AlarmString += ", Channel5 Low"
    if CurrentCode[13:14] == "1":
        if CurrentCode[13:14] != AlarmCode[13:14]:
            AlarmString += ", Channel6 Low"
    if CurrentCode[14:15] == "1":
        if CurrentCode[14:15] != AlarmCode[14:15]:
            AlarmString += ", Channel7 Low"   
    if CurrentCode[15:16] == "1":
        if CurrentCode[15:16] != AlarmCode[15:16]:
            AlarmString += ", Channel8 Low" 
    #print(AlarmString)
    #create filename based on this month
    now = datetime.now()
    FileName = str(now.strftime("%m%Y"))+'Alarms.csv'
    FileName = DataPath+FileName
    #check if file exists, if not, create a file with headers first
    response = os.path.isfile(FileName)
    if response == False:
        fd = open(FileName,'a')
        fd.write("Alarm Log - " + str(now.strftime("%m/%Y")) +"\n")
        fd.close()
    if AlarmString != "":
        fd = open(FileName,'a')
        TimeNow = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        fd.write(TimeNow + AlarmString + "\n")
        fd.close()
    AlarmCode = CurrentCode

# Update live readings
    if Ch1Active == 1:
        StatLabel1['text'] =(CH1DispName+" = "+str('{0:.2f}'.format(volt1)))
    else:
        StatLabel1['text'] =""
    if Ch2Active == 1:
        StatLabel2['text'] =(CH2DispName+" = "+str('{0:.2f}'.format(volt2)))
    else:
        StatLabel2['text'] =""
    if Ch3Active == 1:
        StatLabel3['text'] =(CH3DispName+" = "+str('{0:.2f}'.format(volt3)))
    else:
        StatLabel3['text'] =""
    if Ch4Active == 1:
        StatLabel4['text'] =(CH4DispName+" = "+str('{0:.2f}'.format(volt4)))
    else:
        StatLabel4['text'] =""
    if Ch5Active == 1:
        StatLabel5['text'] =(CH5DispName+" = "+str('{0:.2f}'.format(volt5)))
    else:
        StatLabel5['text'] =""
    if Ch6Active == 1:
        StatLabel6['text'] =(CH6DispName+" = "+str('{0:.2f}'.format(volt6)))
    else:
        StatLabel6['text'] =""
    if Ch7Active == 1:
        StatLabel7['text'] =(CH7DispName+" = "+str('{0:.2f}'.format(volt7)))
    else:
        StatLabel7['text'] =""
    if Ch8Active == 1:
        StatLabel8['text'] =(CH8DispName+" = "+str('{0:.2f}'.format(volt8)))
    else:
        StatLabel8['text'] =""
# Update graph data
    ArrayFlag = 0
    Output1List.append(volt1)
    Output2List.append(volt2)
    Output3List.append(volt3)
    Output4List.append(volt4)
    Output5List.append(volt5)
    Output6List.append(volt6)
    Output7List.append(volt7)
    Output8List.append(volt8)
    if FirstRound == 0:
        TimeList.append(PlotSecs)
        Data1List.append(volt1)
        Data2List.append(volt2)
        Data3List.append(volt3)
        Data4List.append(volt4)
        Data5List.append(volt5)
        Data6List.append(volt6)
        Data7List.append(volt7)
        Data8List.append(volt8)
    else:
        #print("PlotSecs - ")
        #print(str(PlotSecs))
        ArrayFlag = int(round(PlotSecs*(60000/ScanTime)))
        #print(ArrayFlag)
        #TimeList[ArrayFlag]=ArrayFlag
        TimeList[ArrayFlag]=PlotSecs
        
        Data1List[ArrayFlag]=(volt1)
        Data2List[ArrayFlag]=(volt2)
        Data3List[ArrayFlag]=(volt3)
        Data4List[ArrayFlag]=(volt4)
        Data5List[ArrayFlag]=(volt5)
        Data6List[ArrayFlag]=(volt6)
        Data7List[ArrayFlag]=(volt7)
        Data8List[ArrayFlag]=(volt8)
        
    # slice the DataList(s) so the values are order with latest at the end
    # current latest value is at location ArrayFlag
    NewData1List = Data1List[ArrayFlag:]
    NewData1List.extend(Data1List[:(ArrayFlag)])
    NewData2List = Data2List[ArrayFlag:]
    NewData2List.extend(Data2List[:(ArrayFlag)])
    NewData3List = Data3List[ArrayFlag:]
    NewData3List.extend(Data3List[:(ArrayFlag)])
    NewData4List = Data4List[ArrayFlag:]
    NewData4List.extend(Data4List[:(ArrayFlag)])
    NewData5List = Data5List[ArrayFlag:]
    NewData5List.extend(Data5List[:(ArrayFlag)])
    NewData6List = Data6List[ArrayFlag:]
    NewData6List.extend(Data6List[:(ArrayFlag)])
    NewData7List = Data7List[ArrayFlag:]
    NewData7List.extend(Data7List[:(ArrayFlag)])
    NewData8List = Data8List[ArrayFlag:]
    NewData8List.extend(Data8List[:(ArrayFlag)])
    #NewTimeList = TimeList[ArrayFlag:]
    #NewTimeList.extend(TimeList[:(ArrayFlag)])
    #print(Data1List)
    #print(NewData1List)
    #print("__________________")
    if Ch1Active == 1:
        line1.set_xdata(TimeList)
        line1.set_ydata(NewData1List)
    if Ch2Active == 1:
        line2.set_xdata(TimeList)
        line2.set_ydata(NewData2List)
    if Ch3Active == 1:
        line3.set_xdata(TimeList)
        line3.set_ydata(NewData3List)
    if Ch4Active == 1:        
        line4.set_xdata(TimeList)
        line4.set_ydata(NewData4List)
    if Ch5Active == 1:        
        line5.set_xdata(TimeList)
        line5.set_ydata(NewData5List)
    if Ch6Active == 1:        
        line6.set_xdata(TimeList)
        line6.set_ydata(NewData6List)
    if Ch7Active == 1:        
        line7.set_xdata(TimeList)
        line7.set_ydata(NewData7List)
    if Ch8Active == 1:        
        line8.set_xdata(TimeList)
        line8.set_ydata(NewData8List)
    
    PlotSecs += ScanTime/(60*1000)
    
    line1.axes.set_ylim(YMin, YMax)
    line1.axes.set_xlim(XMin, XMax)
    
    #line1.legend()
#plt.plot(x2, y2, label='Second Line')
    #line1.axes.autoscale(enable=True, axis='y')
    #line2.axes.autoscale(enable=True, axis='y')
    #a.show()
    f.canvas.draw()
    Ave_Available = 0
    #print("CycleSoFar")
    #print(CycleSoFar)
    #print("Ave_time")
    #print(Ave_time)
    if CycleSoFar >= int(Ave_time):
        Ave_Available = 1
        #calculate the average, delete the array and store the data in .CSV file
        
        AverageCh1 = str(round(sum(Output1List)/len(Output1List),2))
        AverageCh2 = str(round(sum(Output2List)/len(Output2List),2))
        AverageCh3 = str(round(sum(Output3List)/len(Output3List),2))
        AverageCh4 = str(round(sum(Output4List)/len(Output4List),2))
        AverageCh5 = str(round(sum(Output5List)/len(Output5List),2))
        AverageCh6 = str(round(sum(Output6List)/len(Output6List),2))
        AverageCh7 = str(round(sum(Output7List)/len(Output7List),2))
        AverageCh8 = str(round(sum(Output8List)/len(Output8List),2))
        CH1_Average = (sum(Output1List)/len(Output1List))
        CH2_Average = (sum(Output2List)/len(Output2List))*10
        CH3_Average = (sum(Output3List)/len(Output3List))*100
        CH4_Average = (sum(Output4List)/len(Output4List))
        CH5_Average = (sum(Output5List)/len(Output5List))*10
        CH6_Average = (sum(Output6List)/len(Output6List))*10
        CH7_Average = (sum(Output7List)/len(Output7List))*10
        CH8_Average = (sum(Output8List)/len(Output8List))
        Output1List.clear()
        Output2List.clear()
        Output3List.clear()
        Output4List.clear()
        Output5List.clear()
        Output6List.clear()
        Output7List.clear()
        Output8List.clear()
        
        
        
        #If O2 correction in on, change units label to show what O2 correction is applied
        if O21Correct == "Y":
            Ch1Unit_s = Ch1Units + " @" + O2Ref +"% O2"
        else:
            Ch1Unit_s = Ch1Units
        if O22Correct == "Y":
            Ch2Unit_s = Ch2Units + " @" + O2Ref +"% O2"
        else:
            Ch2Unit_s = Ch2Units
        if O23Correct == "Y":
            Ch3Unit_s = Ch3Units + " @" + O2Ref +"% O2"
        else:
            Ch3Unit_s = Ch3Units
        if O24Correct == "Y":
            Ch4Unit_s = Ch4Units + " @" + O2Ref +"% O2"
        else:
            Ch4Unit_s = Ch4Units
        if O25Correct == "Y":
            Ch5Unit_s = Ch5Units + " @" + O2Ref +"% O2"
        else:
            Ch5Unit_s = Ch5Units
        if O26Correct == "Y":
            Ch6Unit_s = Ch6Units + " @" + O2Ref +"% O2"
        else:
            Ch6Unit_s = Ch6Units
        if O27Correct == "Y":
            Ch7Unit_s = Ch7Units + " @" + O2Ref +"% O2"
        else:
            Ch7Unit_s = Ch7Units
        if O28Correct == "Y":
            Ch8Unit_s = Ch8Units + " @" + O2Ref +"% O2"
        else:
            Ch8Unit_s = Ch8Units
            
        if Daily_Files == 1:
            #create filename based on todays date
            now = datetime.now()
            FileName = str(now.strftime("%m%d%Y"))+'.csv'
            FileName = DataPath+FileName
            #check if file exists, if not, create a file with headers first
            response = os.path.isfile(FileName)
            if response == False:
                fd = open(FileName,'a')
                fd.write("Time" + "," + CH1DispName + " " + Ch1Unit_s + "," + CH2DispName +" "+Ch2Unit_s  + "," + CH3DispName +" "+Ch3Unit_s  + "," + CH4DispName +" "+Ch4Unit_s + "," + CH5DispName +" "+Ch5Unit_s  + "," + CH6DispName +" "+Ch6Unit_s  + "," + CH7DispName +" "+Ch7Unit_s  + "," + CH8DispName +" "+Ch8Unit_s  + ","+"Plant Status"+ ","+"Status code"+"\n")
                fd.close()
            fd = open(FileName,'a')
            TimeNow = str(now.strftime("%H:%M:%S"))
            #print("WRITING DATA TO DAILY FILE")
            fd.write(TimeNow + "," + AverageCh1 + "," + AverageCh2 + "," + AverageCh3 + "," + AverageCh4+ "," + AverageCh5 + "," + AverageCh6 + "," + AverageCh7 + "," + AverageCh8 +","+ str(PlantStat)+","+str(Current_Status) + "\n")
            fd.close()
        if Monthly_Files == 1:
            #create filename based on this month
            now = datetime.now()
            FileName = str(now.strftime("%m%Y"))+'.csv'
            FileName = DataPath+FileName
            #check if file exists, if not, create a file with headers first
            response = os.path.isfile(FileName)
            if response == False:
                fd = open(FileName,'a')
                fd.write("Time" + "," + CH1DispName + " " + Ch1Unit_s + "," + CH2DispName +" "+Ch2Unit_s  + "," + CH3DispName +" "+Ch3Unit_s  + "," + CH4DispName +" "+Ch4Unit_s + "," + CH5DispName +" "+Ch5Unit_s  + "," + CH6DispName +" "+Ch6Unit_s  + "," + CH7DispName +" "+Ch7Unit_s  + "," + CH8DispName +" "+Ch8Unit_s  + ","+"Plant Status"  +"\n")
                fd.close()
            fd = open(FileName,'a')
            TimeNow = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            #print("WRITING DATA TO MONTHLY FILE")
            fd.write(TimeNow + "," + AverageCh1 + "," + AverageCh2 + "," + AverageCh3 + "," + AverageCh4+ "," + AverageCh5 + "," + AverageCh6 + "," + AverageCh7 + "," + AverageCh8 +","+ str(PlantStat) +"\n")
            fd.close()
        CycleSoFar = 0
    

        
    # run this every so often to update live values on RTU modbus server

    
    # if unable to transmit negative numbers, mark all negative numbers as zero
    #if CH1_Raw < 0:
    #    CH1_Raw = 0
    #if CH2_Raw < 0:
    #    CH2_Raw = 0
    #if CH3_Raw < 0:
    #    CH3_Raw = 0
    #if CH4_Raw < 0:
    #    CH4_Raw = 0
    #if CH5_Raw < 0:
    #    CH5_Raw = 0
    #if CH6_Raw < 0:
    #    CH6_Raw = 0
    #if CH7_Raw < 0:
    #    CH7_Raw = 0
    #if CH8_Raw < 0:
    #    CH8_Raw = 0
    #if CH1_Corr < 0:
    #    CH1_Corr = 0
    #if CH2_Corr < 0:
    #    CH2_Corr = 0
    #if CH3_Corr < 0:
    #    CH3_Corr = 0
    #if CH4_Corr < 0:
    #    CH4_Corr = 0
    #if CH5_Corr < 0:
    #    CH5_Corr = 0
    #if CH6_Corr < 0:
    #    CH6_Corr = 0
    #if CH7_Corr < 0:
    #    CH7_Corr = 0
    #if CH8_Corr < 0:
    #    CH8_Corr = 0
    #if CH1_Average < 0:
    #    CH1_Average = 0
    #if CH2_Average < 0:
    #    CH2_Average = 0
    #if CH3_Average < 0:
    #    CH3_Average = 0
    #if CH4_Average < 0:
    #    CH4_Average = 0
    #if CH5_Average < 0:
    #    CH5_Average = 0
    #if CH6_Average < 0:
    #    CH6_Average = 0
    #if CH7_Average < 0:
    #    CH7_Average = 0
    #if CH8_Average < 0:
    #    CH8_Average = 0
    #context[slave_id].setValues(FunctionCode,Register3 , [0x09])

    # Add all data to registers as 16 bit values
    builder = BinaryPayloadBuilder(
        byteorder=Endian.Big,
        wordorder=Endian.Little
        )
    #CH1_Raw = 666
    builder.add_16bit_int(CH1_Raw)
    # Define your functions here

    def LogOnOff():
        # Implement the function logic here
        pass

    def ExportData():
        # Implement the function logic here
        pass

    def CheckUserPassword(callback):
        # Implement the function logic here
        pass

    def ConfigGraph():
        # Implement the function logic here
        pass

    def CheckPassword(callback):
        # Implement the function logic here
        pass

    def SilenceAlarms():
        # Implement the function logic here
        pass

    def About():
        # Implement the function logic here
        pass

    def on_closing():
        root.destroy()
        call("sudo nohup shutdown -h now", shell=True)
        sys.exit()

    # Create the root window
    root = Tk()
    root.attributes('-zoomed', True)
    root.title("MCP Plus - Combustion Plant Data Processing System")

    # Create the figure and subplot
    f = Figure(figsize=(5.4, 4), dpi=100)
    a = f.add_subplot(111)
    a.set_ylabel("units")
    a.set_title("Data plot (time in minutes)")

    # Create the frames
    TopFrame = Frame(root, bd=2, padx=1, pady=1, relief=SUNKEN)
    TopFrame.pack(side=TOP, fill=X)
    GraphFrame = Frame(root, bd=2, padx=1, pady=1, relief=SUNKEN)
    GraphFrame.pack(expand=True, side=LEFT)
    StatusFrame = Frame(root, bd=2, padx=1, pady=10, relief=SUNKEN)
    StatusFrame.pack(side=LEFT, fill=Y)
    AlarmFrame = Frame(root, bd=2, padx=10, pady=10, relief=SUNKEN)
    AlarmFrame.pack(expand=True, side=BOTTOM, fill=BOTH)

    # Create the canvas for the graph
    canvas = FigureCanvasTkAgg(f, master=GraphFrame)
    canvas.get_tk_widget().pack()

    # Add the logo image
    logo = Image.open(SavePath + "DRM.png")
    Ablogo = Image.open(SavePath + "CRS.jpg")
    logo = logo.resize((100,80), Image.ANTIALIAS)
    Ablogo = Ablogo.resize((91,41), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    Ablogo = ImageTk.PhotoImage(Ablogo)
    LogoImage = Label(TopFrame, image=logo, width=100, height=80)
    LogoImage.pack(side=LEFT)

    # Add the controls and icons
    ControlsFrame = Frame(TopFrame, bd=2, padx=10, pady=10, relief=SUNKEN)
    ControlsFrame.pack(expand=True, side=LEFT, fill=X)

    IconsFrame = Frame(TopFrame, bd=2, padx=10, pady=10, relief=SUNKEN)
    IconsFrame.pack(fill=Y, side=RIGHT)

    # Add the status icons
    IconsTitle = Label(IconsFrame, text="Status", font='Helvetica 10')
    IconsTitle.pack(side=TOP)

    Icon1 = Frame(IconsFrame, relief=FLAT)
    Icon1.pack(side=TOP)

    Icon2 = Frame(IconsFrame, relief=FLAT)
    Icon2.pack(side=TOP)

    Icon3 = Frame(IconsFrame, relief=FLAT)
    Icon3.pack(side=TOP)

    # Create the status icon images
    StatusDia = 8
    AnImage = Image.new("RGB", (StatusDia, StatusDia), "lightgrey")
    draw = ImageDraw.Draw(AnImage)
    draw.ellipse((1, 1, StatusDia-1, StatusDia-1), fill="green", outline="black")
    AnImage.save('StatusGreen.png')
    StatusGreen = PhotoImage(file='StatusGreen.png')

    StatusDia = 8
    AnImage = Image.new("RGB", (StatusDia, StatusDia), "lightgrey")
    draw = ImageDraw.Draw(AnImage)
    draw.ellipse((1, 1, StatusDia-1, StatusDia-1), fill="red", outline="black")
    AnImage.save('StatusRed.png')
    StatusRed = PhotoImage(file='StatusRed.png')

    # Add the status icons and labels
    Icon1Label = Label(Icon1, text="Modbus", font='Helvetica 10')
    Icon1Label.pack(side=LEFT)
    StatusRTU = Label(Icon1, image=StatusRed)
    StatusRTU.pack(side=LEFT)

    PlantStat = 0
    Icon2Label = Label(Icon2, text="Plant ", font='Helvetica 10')
    Icon2Label.pack(side=LEFT)
    StatusPlant = Label(Icon2, image=StatusRed)
    StatusPlant.pack(side=LEFT)

    StatusEcom_Label = Label(Icon3, text="Ecom ", font='Helvetica 10')
    StatusEcom_Label.pack(side=LEFT)
    StatusEcom = Label(Icon3, text="O", bg="red", font='Helvetica 10')
    StatusEcom.pack(side=LEFT)

    # Add the control buttons
    ControlsTitle = Label(ControlsFrame, text="CONTROLS")
    ControlsTitle.pack(side=TOP)

    ExportImage = PhotoImage(file=SavePath+'Export.png')
    StartImage = PhotoImage(file=SavePath+'Start.png')
    StopImage = PhotoImage(file=SavePath+'Stop.png')
    AlarmOnImage = PhotoImage(file=SavePath+'AlarmOn.png')
    AlarmOffImage = PhotoImage(file=SavePath+'AlarmOff.png')
    AlarmSettingsImage = PhotoImage(file=SavePath+'AlarmSettings.png')
    GraphSettingsImage = PhotoImage(file=SavePath+'GraphSettings.png')
    SettingsImage = PhotoImage(file=SavePath+'Settings.png')
    AboutImage = PhotoImage(file=SavePath+'About.png')

    ButtonA = Button(ControlsFrame, image=StartImage, borderwidth=0, padx=5, pady=8, command=LogOnOff)
    ButtonA.pack(side=LEFT, padx=4)

    ButtonB = Button(ControlsFrame, image=ExportImage, borderwidth=0, padx=5, pady=8, command=ExportData)
    ButtonB.pack(side=LEFT, padx=4)

    ButtonC = Button(ControlsFrame, image=SettingsImage, borderwidth=0, padx=5, pady=8, command=lambda: CheckUserPassword(SettingsClicked))
    ButtonC.pack(side=LEFT, padx=4)

    ButtonD = Button(ControlsFrame, image=GraphSettingsImage, borderwidth=0, padx=5, pady=8, command=ConfigGraph)
    ButtonD.pack(side=LEFT, padx=4)

    ButtonE = Button(ControlsFrame, image=AlarmSettingsImage, borderwidth=0, padx=5, pady=8, command=lambda: CheckPassword(ConfigAlarms))
    ButtonE.pack(side=LEFT, padx=4)

    ButtonF = Button(ControlsFrame, image=AlarmOffImage, borderwidth=0, padx=5, pady=8, command=SilenceAlarms)
    ButtonF.pack(side=LEFT, padx=4)

    ButtonG = Button(ControlsFrame, image=AboutImage, borderwidth=0, padx=5, pady=8, command=About)
    ButtonG.pack(side=LEFT, padx=4)

    # Add the status labels
    StatusTitle = Label(StatusFrame, width=20, text="Current Readings")
    StatusTitle.pack(side=TOP)

    if Ch1Active == 1:
        labelit = (CH1DispName+" - ##")
    else:
        labelit = ""
    StatLabel1 = Label(StatusFrame, text=(labelit))
    StatLabel1.pack(side=TOP)

    if Ch2Active == 1:
        labelit = (CH2DispName+" - ##")
    else:
        labelit = ""
    StatLabel2 = Label(StatusFrame, text=(labelit))
    StatLabel2.pack(side=TOP)

    if Ch3Active == 1:
        labelit = (CH3DispName+" - ##")
    else:
        labelit = ""
    StatLabel3 = Label(StatusFrame, text=(labelit))
    StatLabel3.pack(side=TOP)

    if Ch4Active == 1:
        labelit = (CH4DispName+" - ##")
    else:
        labelit = ""
    StatLabel4 = Label(StatusFrame, text=(labelit))
    StatLabel4.pack(side=TOP)

    if Ch5Active == 1:
        labelit = (CH5DispName+" - ##")
    else:
        labelit = ""
    StatLabel5 = Label(StatusFrame, text=(labelit))
    StatLabel5.pack(side=TOP)

    if Ch6Active == 1:
        labelit = (CH6DispName+" - ##")
    else:
        labelit = ""
    StatLabel6 = Label(StatusFrame, text=(labelit))
    StatLabel6.pack(side=TOP)

    if Ch7Active == 1:
        labelit = (CH7DispName+" - ##")
    else:
        labelit = ""
    StatLabel7 = Label(StatusFrame, text=(labelit))
    StatLabel7.pack(side=TOP)

    if Ch8Active == 1:
        labelit = (CH8DispName+" - ##")
    else:
        labelit = ""
    StatLabel8 = Label(StatusFrame, text=(labelit))
    StatLabel8.pack(side=TOP)

    # Add the alarm labels
    AlarmTitle = Label(AlarmFrame, text="ALARMS")
    AlarmTitle.pack(side=TOP)

    AlarmFlag = Label(AlarmFrame, text="ALARM", bg="red", wraplength=70)
    AlarmFlag.pack(side=TOP, expand=True, fill=BOTH)

    AlarmDesc = Label(AlarmFrame, text="Stopped")
    AlarmDesc.pack(side=BOTTOM)

    # Initial plot
    x = 0
    y = 0
    z = 0

    if Ch1Active == 1:
        line1, = a.plot(x, y, color='green', linestyle='solid', linewidth=1)

    if Ch2Active == 1:
        line2, = a.plot(x, z, color='red', linestyle='solid', linewidth=1)

    if Ch3Active == 1:
        line3, = a.plot(x, z, color='blue', linestyle='solid', linewidth=1)

    if Ch4Active == 1:
        line4, = a.plot(x, z, color='purple', linestyle='solid', linewidth=1)

    if Ch5Active == 1:
        line5, = a.plot(x, z, color='yellow', linestyle='solid', linewidth=1)

    if Ch6Active == 1:
        line6, = a.plot(x, z, color='cyan', linestyle='solid', linewidth=1)

    if Ch7Active == 1:
        line7, = a.plot(x, z, color='pink', linestyle='solid', linewidth=1)

    if Ch8Active == 1:
        line8, = a.plot(x, z, color='grey', linestyle='solid', linewidth=1)

    line1.axes.set_xlim(0, XMax)
    line1.axes.set_ylim(YMin, YMax)

    if Ch1Active == 1:
        line1.set_label(CH1DispName)
        line1.axes.legend()

    if Ch2Active == 1:
        line2.set_label(CH2DispName)
        line2.axes.legend()

    if Ch3Active == 1:
        line3.set_label(CH3DispName)
        line3.axes.legend()

    if Ch4Active == 1:
        line4.set_label(CH4DispName)
        line4.axes.legend()

    if Ch5Active == 1:
        line5.set_label(CH5DispName)
        line5.axes.legend()

    if Ch6Active == 1:
        line6.set_label(CH6DispName)
        line6.axes.legend()

    if Ch7Active == 1:
        line7.set_label(CH7DispName)
        line7.axes.legend()

    if Ch8Active == 1:
        line8.set_label(CH8DispName)
        line8.axes.legend()

    f.canvas.draw()

    # Set the closing event handler
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main event loop
    root.mainloop()
