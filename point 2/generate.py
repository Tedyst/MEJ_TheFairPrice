import random

samples = 100000
winning = 0

f = open("samples.txt", "w")

for joc in range(1, samples+1):
    # False is the black marble
    v = [False, True]
    nr = 0
    while random.choice(v) is False:
        nr += 1
        v.append(True)
    f.write(str(winning/joc*100) + '\n')
    if len(v) > 3:
        winning += 1

print(str(winning/samples*100) + '%')
