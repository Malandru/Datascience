import pandas as pd
import sys

RAT, INI, FIN, EVA = 0, 1, 2, 3

def main():
    file = sys.argv[1]
    csv = pd.read_csv(file)
    # for field in ['movieId', 'rating', 'timestamp']
    movies = csv['movieId']
    ratings = csv['rating']
    times = csv['timestamp']

    data = {}
    i, limit = 0, len(movies)
    while i < limit:
        MOV = movies[i]
        TIM = times[i]
        try:
            data[MOV][RAT] += ratings[i]
            if TIM < data[MOV][INI]:
                data[MOV][INI] = TIM
            elif TIM > data[MOV][FIN]:
                data[MOV][FIN] = TIM
            data[MOV][EVA] += 1
        except KeyError:
            data[MOV] = [ratings[i], TIM, TIM, 1]
        i += 1
    
    ids = data.keys()
    ids.sort()

    print 'movieId,rating avg,first review,last review,evals'
    for id in ids:
        data[id][RAT] /= data[id][EVA]
        s = '{},{},{},{},{}'.format(*([id] + data[id]))
        print s

main()