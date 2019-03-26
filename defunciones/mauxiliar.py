from os import system

command = 'grep ^\\"{} -m 1 --text decateml.csv'
for i in range(1, 33):
    x = str(i).zfill(2)
    # print command.format(x)
    system(command.format(x))