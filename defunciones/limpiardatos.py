#!/usr/bin/python
from sys import argv

def readfile(file):
    line = file.readline()
    print line.rstrip()
    while True:
        line = file.readline()
        if line == '': break
        line = line.rstrip()
        line = line.replace('"', '')
        line = ''.join(line.split())
        print line

def main():
    filename = argv[1]
    file = open(filename)
    readfile(file)
    file.close()

main()