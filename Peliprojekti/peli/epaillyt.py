class Epailty:
    def __init__(self, nimi, ikä, rooli, motiivi):
        self.nimi = nimi
        self.ikä = ikä
        self.rooli = rooli
        self.motiivi = motiivi

    # Määrittää, miten epäilty näytetään pelaajalle.
    def __str__(self):
        return f"Nimi: {self.nimi} \nIkä: {self.ikä} vuotta vanha \nRooli: {self.rooli} \nMotiivi: {self.motiivi}"

elisa = Epailty("Elisa Kivi", 48, "Edvardin vaimo", "Elisa ja Edvard olivat riidelleet")
james = Epailty("James Kivi", 50, "Edvardin veli", "Jamesilla oli taloudellisia ongelmia")
viktor = Epailty("Viktor Salonen", 49, "Edvardin liikekumppani", "Viktor halusi suuremman osuuden uudesta teknologiasta")
sofia = Epailty("Sofia Niemi", 44, "Edvardin sihteeri", "Sofia tiesi paljon Edvardin tutkimuksesta")

# Lista kaikista pelin epäillyistä, jota käytetään päävalikossa, kun pelaaja haluaa tutkia epäiltyjä.
epaillyt = [elisa, james, viktor, sofia]