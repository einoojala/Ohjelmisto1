vuodenajat = ("talvi", "kevät", "kesä", "syksy")

while True:
    syote = input("Anna kuukauden numero (q lopettaa): ")

    if syote == "q":
        break

    kuukausi_numero = int(syote)

    if kuukausi_numero < 1 or kuukausi_numero > 12:
        print("Annoit väärän numeron.")
        continue

    if kuukausi_numero == 12 or kuukausi_numero <= 2:
        vuodenaika = vuodenajat[0]
    elif kuukausi_numero <= 5:
        vuodenaika = vuodenajat[1]
    elif kuukausi_numero <= 8:
        vuodenaika = vuodenajat[2]
    else:
        vuodenaika = vuodenajat[3]

    print(vuodenaika)