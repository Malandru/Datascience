import matplotlib.pyplot as plt
from itertools import izip
import numpy as np

def graph(formula, x_range):
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()

def media(numbers):
    return sum(numbers) / len(numbers)

def cuad(lista, prom):
    suma = 0
    for x in lista:
        suma += (x - prom) ** 2
    return suma

def dsvstd(lista, prom):
    var = cuad(lista, prom) / (len(lista) - 1)
    return var ** 0.5

def get_formula(times, amounts):
    n = len(times)
    sx = sum(times)
    sy = sum(amounts)
    sxy = sum([x * y for x, y in izip(times, amounts)])
    sx2 = sum([x * x for x in times])

    b = (n*sxy - sx*sy) / (n*sx2 - sx ** 2)
    a = (sx2*sy - sxy*sx) / (n*sx2 - sx ** 2)

    if a >= 0: a = '+' + str(a)
    else: a = str(a)
    
    return str(b) + '*x' + a
    
    # xm = media(times)
    # ym = media(amounts)
    # num = [(x - xm)*(y - ym) for x, y in izip(times, amounts)]
    # den = cuad(times, xm) * cuad(amounts, ym)

    # r = sum(num) / (den ** 0.5)
    # m = r * dsvstd(amounts, ym) / dsvstd(times, xm)
    # b = ym - m * xm

    # if b > 0: b = '+' + str(b)
    # else: b = str(b)
    # return str(m) + '*x' + b

def main():
    times, amounts = [], []
    try:
        print raw_input()
        while True:
            data = raw_input().split(',')
            times.append(float(data[0]))
            amounts.append(float(data[1]))
    except EOFError:
        pass
    print '\nGetting the line equation...'
    formula = get_formula(times, amounts)
    print 'Ecuation: [ y =', formula,']\n'
    print 'Plotting...'
    size = len(times) / 2
    plt.scatter(times[:size], amounts[:size], marker='.', c='black')
    plt.xlabel('Distance (miles)')
    plt.ylabel('Amount ($)')
    # plt.show()
    print 'Showing graph'
    graph(formula, range(0, int(max(times)) + 1))

main()