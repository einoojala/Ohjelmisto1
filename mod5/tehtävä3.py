luvut = []

while True:
    arvo = input("Anna luku: ")

    if arvo == "":
        break

    luvut.append(float(arvo))

print("Pienin luku:", min(luvut))
print("Suurin luku:", max(luvut))