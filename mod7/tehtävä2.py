import random
tahkot = int(input("Anna tahkojen määrä: "))

def noppa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

while True:
    silmaluku = noppa(tahkot)
    print(silmaluku)

    if silmaluku == tahkot:
        break