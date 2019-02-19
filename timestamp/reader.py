import re
file = open('data.csv')

file.readline()
file.readline()

while True:
    line = file.readline()
    if line == '': break
    line = line.split(',')
    dates = line[1:3]

    for date in dates:
        numbers = re.findall(r'\d+', date)
        for num in numbers:
            print num

file.close()