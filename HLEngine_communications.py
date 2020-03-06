import serial
import smtplib
import os

def find_Port():
    try:
        ser = serial.Serial("COM1", rate)
        print("Connected to COM1")
    except:
        print("Disconnected to COM1")
    
    try:
        ser = serial.Serial("COM2", rate)
        print("Connected to COM2")
    except:
        print("Disconnected to COM2")

    
    try:
        ser = serial.Serial("COM3", rate)
        print("Connected to COM3")
    except:
        print("Disconnected to COM3")


    try:
        ser = serial.Serial("COM4", rate)
        print("Connected to COM4")
    except:
        print("Disconnected to COM4")

    try:
        ser = serial.Serial("COM5", rate)
        print("Connected to COM5")
    except:
        print("Disconnected to COM5")

    try:
        ser = serial.Serial("COM6", rate)
        print("Connected to COM6")
    except:
        print("Disconnected to COM6")


    try:
        ser = serial.Serial("COM7", rate)
        print("Connected to COM7")
    except:
        print("Disconnected to COM7")

    try:
        ser = serial.Serial("COM8", rate)
        print("Connected to COM8")
    except:
        print("Disconnected to COM8")

    try:
        ser = serial.Serial("COM9", rate)
        print("Connected to COM9")
    except:
        print("Disconnected to COM9")

    try:
        ser = serial.Serial("COM10", rate)
        print("Connected to COM10")
    except:
        print("Disconnected to COM10")

    try:
        ser = serial.Serial("COM11", rate)
        print("Connected to COM11")
    except:
        print("Disconnected to COM11")

    try:
        ser = serial.Serial("COM12", rate)
        print("Connected to COM12")
    except:
        print("Disconnected to COM12")

    try:
        ser = serial.Serial("COM13", rate)
        print("Connected to COM13")
    except:
        print("Disconnected to COM13")

    try:
        ser = serial.Serial("COM14", rate)
        print("Connected to COM14")
    except:
        print("Disconnected to COM14")

    try:
        ser = serial.Serial("COM15", rate)
        print("Connected to COM15")
    except:
        print("Disconnected to COM15")

    try:
        ser = serial.Serial("COM16", rate)
        print("Connected to COM16")
    except:
        print("Disconnected to COM16")

    try:
        ser = serial.Serial("COM17", rate)
        print("Connected to COM17")
    except:
        print("Disconnected to COM17")

    try:
        ser = serial.Serial("COM18", rate)
        print("Connected to COM18")
    except:
        print("Disconnected to COM18")

    try:
        ser = serial.Serial("COM19", rate)
        print("Connected to COM19")
    except:
        print("Disconnected to COM19")

    try:
        ser = serial.Serial("COM20", rate)
        print("Connected to COM20")
    except:
        print("Disconnected to COM20")

    try:
        ser = serial.Serial("/dev/ttyUSB0", rate)
        print("Connected to /dev/ttyUSB0")
    except:
        print("Disconnected to /dev/ttyUSB0")

    try:
        ser = serial.Serial("/dev/ttyUSB1", rate)
        print("Connected to /dev/ttyUSB1")
    except:
        print("Disconnected to /dev/ttyUSB1")


def serSend(port,rate,data):
    try:
        ser = serial.Serial(port, rate)
        ser.write(data)
        return ("done")
    except:
        return ("HLEngine:issue with the  port")

def serRecieve(port,rate):
    try:
        ser = serial.Serial(port, rate)
        Serial_data = ser.readline()
        return (Serial_data)
    except:
        return ("HLEngine:issue with the  port")


def sendMail(mailid,psd,to,msg):
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(mailid,psd)
        content=msg
        server.sendmail(mailid,to,content)
        server.quit()
        return ("HLEngine :mail_sent")
    except:
        return ("HLEngine :failed to send mail")

def shutDown_windows():
    os.system("shutdown /s /t 1")

def reboot_windows():
    os.system("restart /s /t 1")







