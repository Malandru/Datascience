#!/usr/bin/python
from unidecode import unidecode
from sys import argv

def to_utf8(string):
    string = unidecode(string.decode('latin-1'))
    string = string.rstrip()
    return string

def readfile(file):
    line = file.readline()
    print to_utf8(line)
    while True:
        line = file.readline()
        if line == '': break
        line = to_utf8(line)
        coma = line.find(',') + 1
        clave = line[:coma]
        text =  line[coma:].lower()
        text = text.replace('"', '').strip()
        text = '"' + text + '"'
        line = clave + text
        print line

def main():
    filename = argv[1]
    file = open(filename)
    readfile(file)
    file.close()

main()