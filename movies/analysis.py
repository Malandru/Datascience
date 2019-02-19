import matplotlib.pyplot as plt
import pandas as pd
import sys
import re

def mkyears(data):
    years = {}
    for movie in data['title']:
        key = re.findall(r'[(]\d+[)]\s*$', movie)
        try:
            if len(key) == 0: key = 'No year'
            else:
                key = key[0]
                key = ''.join(x for x in key if x.isdigit())
            years[key] += 1
        except KeyError:
            years[key] = 1
    return years

def match(pattern, line):
    genres = pattern.split(',')
    for gen in genres:
        if gen not in str(line):
            return False
    return True

def main():
    file = sys.argv[1]
    year = sys.argv[2]
    data = pd.read_csv(file)
    years = mkyears(data)
    # print years
    try:
        print years[int(year)]
    except ValueError:
        pattern = str(year)
        movies = data['movieId']
        genres = data['genres']
        i, lim = 0, len(movies)
        while i < lim:
            if match(pattern, genres[i]):
                print movies[i]
            i += 1
    
main()
