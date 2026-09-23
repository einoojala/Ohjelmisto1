luvut = []
while True:
    arvo = input("Anna luku: ")

    if arvo == "":
        break

    luvut.append(int(arvo))

luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)