import analysis
import re
import sys

labl, valc = None, None 
labels, data = [], {}
indxlst = None
def set_values(_input, indxlst, values):
    global labl
    global valc
    key, val = _input[labl].decode('utf-8'), float(_input[valc])
    try:
        data[key] += val
    except KeyError:
        data[key] = val
    for loc, index in enumerate(indxlst):
        values[loc] += [float(_input[index])]

def read_values(file):
    global indxlst
    values = [[] for e in indxlst]
    try:
        while True:
            _input = file.readline()
            if re.findall(r'matches', _input) != []:
                print _input
                print '----------------------------------\n'
                break
            _input = _input.split('\\')
            set_values(_input, indxlst, values)
    except EOFError: pass
    return values

def print_info(numbers):
    media = analysis.promedio(numbers)
    var = analysis.varianza(numbers, media)
    print 'Mayor:', max(numbers)
    print 'Menor:', min(numbers)
    print 'Media:', media
    print 'Varianza:', var
    print 'Desviacion estantar:', var ** 0.5
    print '----------------------------------'

def read_parameters():
    global labl
    global valc
    global indxlst
    labl, valc = -1, -1
    regex = sys.argv[1]
    indxlst = [i for i, e in enumerate(regex) if e == 'n']
    while labl == -1 or labl in indxlst:
        labl = input('Columna de etiquetas: ')
    while not valc in indxlst:
        valc = input('Columna de datos: ')

def main():
    read_parameters()
    file = open(sys.argv[2], 'r')
    values = read_values(file)
    #print values
    for col in values:
        print_info(col)
    print data
    analysis.pastel(data.values(), data.keys())

main()