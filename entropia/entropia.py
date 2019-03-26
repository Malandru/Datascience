#!/usr/bin/python
import pandas as pd
from sys import argv
from math import log

def get_targetlist(column, filename):
    csv = pd.read_csv(filename)
    target = None

    for i, key in enumerate(csv.keys()):
        if i == column:
            target = key
            break
    else:
        print 'Columna fuera de rango'
        exit(0)
    print target
    return list(csv[target])

def append(key, data):
    try:
        data[key] += 1.0
    except KeyError:
        data[key] = 1.0

def main():
    column = int(argv[1])
    filename = argv[2]
    target = get_targetlist(column, filename)
    data = {}
    for value in target:
        append(value, data)
    # print data
    n, H = len(target), 0
    for key in data.keys():
        pxi = data[key] / n
        H += pxi * log(pxi, 2)
    H = - H
    print H

main()
