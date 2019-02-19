import matplotlib.pyplot as plt

def promedio(numbers):
    return sum(numbers) / len(numbers)

def varianza(numbers, media):
    suma = 0
    for x in numbers:
        suma += (x - media) ** 2
    return suma / (len(numbers) - 1) #retorna s^2

def pastel(numbers, labels=None):
    plt.pie(numbers, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.show()