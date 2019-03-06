#!/usr/bin/python
from matplotlib import pyplot as plt
from datetime import datetime
from pandas import read_csv
from sys import argv

def main():
    patterns, file = argv[1:-1], argv[-1]
    csv = read_csv(file)
    data = {}
    # Measurement Timestamp
    data['time'] = list(csv['Measurement Timestamp'])
    # Air Temperature
    data['temp'] = list(csv['Air Temperature'])
    x, y = find(patterns, data)
    # print x, y
    plt.plot(x, y)
    plt.show()

def match(patterns, string):
    for pattern in patterns:
        if pattern not in string:
            return False
    return True

def todate(stamp):
    return datetime.strptime(stamp, '%B/%d/%Y %I:%M:%S %p')

def find(patterns, data):
    stamps = data['time']
    temps = data['temp']
    size = len(stamps)
    indices = [i for i in range(size) if match(patterns, stamps[i])]
    smatch = [todate(stamps[i]) for i in indices]
    tmatch = [temps[i] for i in indices]
    return smatch, tmatch

main()