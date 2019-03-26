#!/usr/bin/python
from pandas import read_csv
from sys import argv

def to_dictionary(csv, key_col, value_col):
    keys = list(csv[key_col])
    values = list(csv[value_col])
    info = {} #{key: value}
    i, lim = 0, len(keys)
    while i < lim:
        info[keys[i]] = values[i]
        i += 1
    return info

def read_def(filename):
    csv = read_csv(filename)
    return list(csv['ent_regis']), list(csv['causa_def'])

def read_info(filenames):
    csv_causas = read_csv(filenames[0])
    csv_entmun = read_csv(filenames[1])

    states = {} #{id: estado}
    states = to_dictionary(csv_entmun, 'ent_regis', 'estado')
    
    causas = {} #{cve: descrip}
    causas = to_dictionary(csv_causas, 'CVE', 'DESCRIP')

    return causas, states

def match(patterns, string):
    for pattern in patterns:
        if pattern in string:
            continue
        return False
    return True

def insert(key, value, data):
    try:
        data[key].append(value)
    except KeyError:
        data[key] = [value]

def main():
    patterns = argv[1:]
    path = '../inputdata/'
    filenames = [path + 'causas.csv', path + 'entidades.csv', path + 'defunciones.csv']

    causas, states = read_info(filenames)
    ubics, causas_def = read_def(filenames[-1])

    data = {} #{estado: [causas asociadas a este estado]}
    for key in causas.keys():
        causa = causas[key]
        if match(patterns, causa):
            try:
                index = causas_def.index(key)
                id = ubics[index]
                insert(states[id], causa, data)
            except ValueError: pass

    for key in data.keys():
        matches = data[key]
        print '\n\t\t\t>>', len(matches), key, '<<\n'
        for i, elem in enumerate(matches, start=1):
            msg = '{}.- {}'.format(i, elem)
            print msg

main()