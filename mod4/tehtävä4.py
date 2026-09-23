vuosi = int(input("Anna vuosiluku: "))

if vuosi % 400 == 0:
    print("On karkausvuosi")
elif vuosi % 100 == 0:
    print("Ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")