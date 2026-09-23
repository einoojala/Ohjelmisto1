pituus = float(input("Kuinka pitkä olet? "))

if pituus >= 140:
    ika = int(input("Mikä on ikäsi: "))
    if ika>= 8:
        print("Pääset kaikkiin laitteisiin")
    else:
        print("Pääset kaikkiiin paitsi tulirekeen")
elif pituus >=100:
    print("Saat mennä lasten laitteisiin")
else:
    print("Et pääse vielä mihinkään")