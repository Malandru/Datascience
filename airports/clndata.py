import pandas as pd

def is_string(value):
    try:
        float(value)
        return False
    except ValueError:
        return True

def print_header(header):
    line = ''
    for h in header:
        line += h + ','
    print line[:-1]

def main():
    file = '../inputdata/flights.csv'
    csv = pd.read_csv(file)

    # header = ['AIRLINE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT', 'ARRIVAL_DELAY']
    header = {'AIRLINE': True, 'ORIGIN_AIRPORT': True, 'DESTINATION_AIRPORT': True, 'ARRIVAL_DELAY': False}
    print_header(header.keys())

    """ Tabla de verdad usada disminuir la condicion de la llaver con respecto a la cadena
    STR | STR | RES
     0  |  0  |  1
     0  |  1  |  0
     1  |  0  |  0
     1  |  1  |  1
    """
    i, lim = 0, len(csv['AIRLINE'])
    while i < lim:
        line = ''
        for key in header.keys():
            value = csv[key][i]
            if header[key] != is_string(value):
                break
            line += str(value) + ','
        else:
            print line[:-1]
        i += 1

main()