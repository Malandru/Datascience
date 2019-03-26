import pandas as pd
from matplotlib import pyplot as plt
from sys import argv
from math import isnan

def insert(key, value, data):
    if isnan(value): return
    try:
        value = float(value)
        data[key].append(value)
    except KeyError:
        data[key] = [value]

def avg(data):
    return sum(data) / len(data)

option = argv[1]
file = argv[2]
csv = pd.read_csv(file)

airlines = list(csv['AIRLINE'])
airports = list(csv['ORIGIN_AIRPORT'])
delays = list(csv['ARRIVAL_DELAY'])
info = None

if option == 'airport':
    info = airports
elif option == 'airline':
    info = airlines

data = {}
i, lim = 0, len(info)
while i < lim:
    insert(info[i], delays[i], data)
    i += 1

lowest_key = data.keys()[0]
lowest_val = avg(data[lowest_key])

highest_key = lowest_key
highest_val = lowest_val
for key in data.keys():
    media = avg(data[key])
    if media < lowest_val:
        lowest_key = key
        lowest_val = media
    elif media > highest_val:
        highest_key = key
        highest_val = media
    plt.bar(key, media, label=key)

print '{} {} has the lowest delay with value {}'.format(lowest_key, option, lowest_val)
print '{} {} has the highest delay with value {}'.format(highest_key, option, highest_val)

plt.legend()
plt.grid(1)
plt.show()