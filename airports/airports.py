import pandas
import sys

def add(airport, country, data):
    try:
        key = country
        data[key].append(airport)
    except KeyError:
        data[key] = [airport]

user_country = sys.argv[1]
file = sys.argv[2]
csv = pandas.read_csv(file)

countries = list(csv['country'])
airports = list(csv['airport name'])

data = {}

i, lim = 0, len(countries)
while i < lim:
    add(airports[i], countries[i], data)
    i += 1

for airport in data[user_country]:
    print airport
print '\nTotal of airports', len(data[user_country])