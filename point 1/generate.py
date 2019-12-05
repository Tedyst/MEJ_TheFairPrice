import random

medie = 0
samples = 10000

f = open("samples.txt", "w")

for joc in range(1, samples+1):
    # False is the black marble
    v = [False, True]
    nr = 0
    while random.choice(v) is False:
        nr += 1
        v.append(True)
    f.write(str(medie/joc) + '\n')
    medie += nr

print(medie/samples)
