import re

def readallfile():
    while True:
        line = raw_input().split(',')
        dates = line[:2]
        amount = float(line[2])
        print_nmbrs(dates)
        print amount

def print_nmbrs(mylist):
    for elem in mylist:
        numbers = re.findall(r'\d+', elem)
        for num in numbers:
            print num,
        print ''
        

labels = raw_input()
print labels

try:
    readallfile()
except EOFError:
    pass