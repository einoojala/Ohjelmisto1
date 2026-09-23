import random
luku = random.randint(1, 10)
arvaus = int(input("Anna luku: "))

while arvaus != luku:
    if arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")

    arvaus = int(input("Anna luku: "))

print("Oikein")