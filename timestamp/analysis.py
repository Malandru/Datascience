import matplotlib.pyplot as plt

fvtnmnts = 0

def pastel(numbers, labels=None):
    plt.title('Tiempos aproximados')
    plt.pie(numbers, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.show()

def get_inverval(x):
    return '(' + str(x * 15) + '->' + str((x + 1) * 15) + ']'

times = []

try:
    while True:
        times
        times.append(float(input()))
except EOFError:
    pass

fvtnmnts = 60 * 15
labels = [get_inverval(h) for h in range(5)]
data = {lbl: 0 for lbl in labels}
data['Mas'] = 0

t = 0
limit = len(times)
while t < limit:
    x = times[t]
    for i, lbl in enumerate(labels, start=1):
        if x <= fvtnmnts * i:
            data[lbl] += 1
            break
    else:
        data['Mas'] += 1
    t += 1

print data
pastel(data.values(), data.keys())