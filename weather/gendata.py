import serial
from datetime import datetime

def main():
    print 'Measurement Timestamp,Air Temperature'
    s = serial.Serial(port='/dev/tty', baudrate=9600)
    temp = s.readline()
    date = datetime.strftime(datetime.now(), '%B/%d/%Y %I:%M:%S %p')
    print '{},{}'.format(date, temp)