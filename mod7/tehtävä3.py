def polttoaine(maara: float):
    litra = maara * 3.785
    return litra

gallona = float(input("Anna bensiinimäärä (Gallonat): "))

while gallona >=0:
    tulos = polttoaine(gallona)
    print(f"Polttoaine määrä gallonoina {gallona} ja litroina {tulos: .2f} litraa")
    gallona = float(input("Anna bensiinimäärä (Gallonat): "))