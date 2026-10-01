class Epailty:
    def __init__(self, nimi, ika, rooli, motiivi):
        self.nimi = nimi
        self.ika = ika
        self.rooli = rooli
        self.motiivi = motiivi

    # Määrittää, miten epäilty näytetään pelaajalle.
    def __str__(self):
        return f"Nimi: {self.nimi}\nIkä: {self.ika} vuotta\nRooli: {self.rooli}\nMotiivi: \n{self.motiivi}"

elisa = Epailty("Elisa Kivi", 48, "Albertin vaimo",
"""Elisa ja Albert olivat riidelleet viime aikoina usein.
He olivat eri mieltä Albertin työstä ja siitä,
kuinka paljon aikaa hän käytti tutkimukseensa.""")

james = Epailty("James Kivi", 50, "Albertin veli",
"""Jamesilla oli taloudellisia ongelmia.
Hän oli kiinnostunut siitä, kuinka paljon Albertin
uudesta teknologiasta voisi saada rahaa.""")

viktor = Epailty("Viktor Salonen", 49, "Albertin liikekumppani",
"""Viktor halusi suuremman osuuden uuden teknologian
tulevista tuotoista. Hän oli myös uhannut kertoa 
Albertin tutkimuksesta muille.""")

sofia = Epailty("Sofia Niemi", 44, "Albertin sihteeri",
"""Sofia tiesi paljon Albertin tutkimuksesta.
Hän oli eri mieltä siitä, miten tutkimusta pitäisi käyttää.
Sofialla oli myös pääsy Albertin työhuoneeseen.""")

# Lista kaikista pelin epäillyistä, jota käytetään päävalikossa, kun pelaaja haluaa tutkia epäiltyjä.
epaillyt = [elisa, james, viktor, sofia]