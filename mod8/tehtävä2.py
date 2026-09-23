nimet = set()

while True:
    anna_nimi = input("Anna nimi (Enter lopettaa): ")

    if anna_nimi == "":
        break

    anna_nimi = anna_nimi.capitalize()

    if anna_nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(anna_nimi)

print("Syötetyt nimet:")
for nimi in nimet:
    print(nimi)