import pandas as pd
import sys
from os import system

def insert(r, rat, m, mov):
    i, lim = 0, len(rat)
    while i < lim:
        if r > rat[i]: break
        i += 1
    rsort = rat[:i] + [r] + rat[i:]
    msort = mov[:i] + [m] + mov[i:]
    return rsort, msort

def read_file(numbers):
    try:
        while True:
            numbers.append(input())
    except EOFError:
        pass

file = sys.argv[1]
data = pd.read_csv(file)

mvieIds = list(data['movieId'])
ratings = list(data['rating avg'])
evals = list(data['evals'])

matches = []
read_file(matches)

indices = [mvieIds.index(m) for m in matches if m in mvieIds]
rsort = []
msort = []

for i in indices:
    if evals[i] > 750:
        rsort, msort = insert(ratings[i], rsort, mvieIds[i], msort)

# print rsort[:10], msort[:10]
i, lim = 0, 10
while i < lim:
    print 'Rating: ', rsort[i]
    system('cat movies.csv | egrep ^' + str(msort[i]) + ',')
    print '-------------'
    i += 1

print msort[:10]