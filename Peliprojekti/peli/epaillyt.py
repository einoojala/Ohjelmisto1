# Luokka, jonka avulla luodaan pelin epäillyt.
class Epailty:
    # __init__ alustaa uuden epäillyn tiedot, parametreina nimi, ikä, rooli ja motiivi.
    def __init__(self, nimi, ikä, rooli, motiivi):
        self.nimi = nimi
        self.ikä = ikä
        self.rooli = rooli
        self.motiivi = motiivi

    # __str__ määrittää, miten epäilty tulostetaan, kun epäiltyä halutaan näyttää pelaajalle.
    def __str__(self):
        return f"Nimi: {self.nimi}, \nIkä: {self.ikä} vuotta vanha, \nRooli: {self.rooli} \nMotiivi: {self.motiivi}"

# Luodaan pelin neljä epäiltyä Epailty-luokan avulla. Jokaiselleannetaan omat tiedot.
elisa = Epailty("Elisa Kivi", 48, "Edvardin vaimo", "Elisa ja Edvard olivat riidelleet")
james = Epailty("James Kivi", 50, "Edvardin veli", "Jamesilla oli taloudellisia ongelmia")
viktor = Epailty("Viktor Salonen", 49, "Edvardin liikekumppani", "Viktor halusi suuremman osuuden uudesta teknologiasta")
sofia = Epailty("Sofia Niemi", 44, "Edvardin sihteeri", "Sofia tiesi paljon Edvardin tutkimuksesta")

#Listaa käytetään esimerkiksi paavalikko.py-tiedostossa, kun pelaaja haluaa nähdä ja tutkia epäiltyjä.
epaillyt = [elisa, james, viktor, sofia]