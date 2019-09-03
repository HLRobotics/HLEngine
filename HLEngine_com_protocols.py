import serial
import smtplib

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





