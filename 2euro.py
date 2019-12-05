import random

samples = 10000
winning = 0

for joc in range(1, samples+1):
    # False is the black marble
    v = [False, True]
    nr = 0
    while random.choice(v) is False:
        nr += 1
        v.append(True)
    if len(v) > 3:
        winning += 1

print(str(winning/samples*100) + '%')
