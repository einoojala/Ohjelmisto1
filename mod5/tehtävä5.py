kerrat = 0
while kerrat < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    kerrat += 1
if kerrat == 5:
    print("Pääsy evätty")