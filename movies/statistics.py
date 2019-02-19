def promedio(numbers):
    return sum(numbers) / len(numbers)

def varianza(numbers, media):
    suma = 0
    for x in numbers:
        suma += (x - media) ** 2
    return suma / (len(numbers) - 1) #retorna s^2

def read_file(numbers):
    try:
        while True:
            numbers.append(float(raw_input()))
    except EOFError:
        pass

print raw_input()
numbers = []
read_file(numbers)
media = promedio(numbers)
print 'Maximo: ', max(numbers)
print 'Minimo: ', min(numbers)
print 'Promedio: ', media
print 'Desv std: ', varianza(numbers, media) ** 0.5