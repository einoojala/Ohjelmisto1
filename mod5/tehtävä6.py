import random
pisteet = int(input("Kuinka monta pistettä arvotaan? "))
ympyrassa = 0
arvottu = 0

while arvottu < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        ympyrassa += 1
    arvottu += 1

pii = 4 * ympyrassa / pisteet
print("Piin likiarvo:", pii)