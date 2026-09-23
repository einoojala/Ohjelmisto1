import random
def noppa():
    luku = random.randint(1, 6)
    return luku

while True:
    silmaluku = noppa()
    print(silmaluku)

    if silmaluku == 6:
        break