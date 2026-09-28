# Tuodaan huoneissa käytettävät esineet.
from peli.esineet import tutkimuspaperi, avainkortti, usb_kotelo, kuppi, muistilappu

# Luokka, jonka avulla luodaan pelin huoneet.
class Huone:
    def __init__(self, nimi, kuvaus, vihje, esineet):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje
        self.esineet = esineet

    # Määrittää, miten huone tulostetaan pelaajalle.
    def __str__(self):
        return f"\n---- {self.nimi.upper()} ----\n{self.kuvaus}"

    # Antaa pelaajalle mahdollisuuden tutkia huonetta tarkemmin.
    def tutki_tarkemmin(self, pelaaja):
        while True:
            vastaus = input("\nHaluatko tutkia huonetta tarkemmin? (k/e): ").lower()
            if vastaus == "k":
                print("\n---- TARKEMPI TUTKIMUS ----")
                print(self.vihje)

                # Lisätään huoneesta löytyvä vihje pelaajan vihjelistaan.
                pelaaja.lisaa_vihje(self.vihje)
                print("\nPoistut huoneesta.")
                return

            elif vastaus == "e":
                print("\nPoistut huoneesta.")
                return
            else:
                # Jos vastaus ei ole sallittu, kysytään uudelleen.
                print("Vastaa k tai e.")

# --------------------------------------------------
# PELIN HUONEET
# --------------------------------------------------
tyohuone = Huone("Työhuone",
"""Edvardin työhuone on suuri ja hämärä.
Pöydällä on tietokone ja useita papereita.
Seinällä oleva kello on pysähtynyt.""",
"""Työhuoneen pöydän päiväkirjassa on Edvardin viimeinen merkintä, jossa on kellonaika 22.21. Sen jälkeen ei ole muita merkintöjä.""",
 [tutkimuspaperi, usb_kotelo])

kirjasto = Huone("Kirjasto",
"""Kirjastossa on korkeat kirjahyllyt ja vanha kirjoituspöytä.
Jotkut kirjat näyttävät olevan hieman vinossa.""",
"""Yhden tutkimuskansion välistä löytyy merkintä: 'Ensimmäinen toimiva prototyyppi valmistui vuonna 2024.'"""
, [])

keittio = Huone("Keittiö",
"""Keittiössä on vielä illallisen jälkiä.
Pöydällä on astioita ja vedenkeitin.
Huoneessa on hieman outo tunnelma.""",
"""Vedenkeitin on kylmä ja yksi kupeista on täysin kuiva. Seinäkello näyttää aikaa 22.17.""", 
[avainkortti, kuppi])

olohuone = Huone("Olohuone",
"""Olohuoneessa on suuri sohva, takka ja vanha taulu.
Kaikki näyttää ensisilmäyksellä normaalilta.""",
"""Sohvan vierestä löytyy Elisan huivi ja pyödän lasi on lähes koskematon. Taulussa on merkintä: kuusi vuotta sitten kaikki muuttui""", 
[muistilappu])

ruokasali = Huone("Ruokasali",
"""Ruokasalissa on pitkä pöytä, jonka ympärillä on viisi tuolia.
Illallisen jäljet ovat edelleen näkyvissä.""",
"""Illallisen jälkeen Edvardin paikalla on pieni lappu. Lapussa lukee: Uusi paneeli: 28 %, Vanha paneeli: 20 %""",
[])

# Lista kaikista pelin huoneista.
# Listaa käytetään päävalikossa huoneen valitsemiseen.
huoneet = [tyohuone, kirjasto, keittio, olohuone, ruokasali]

# Palauttaa huoneiden esineet alkuperäiseen tilaansa uuden pelin alussa.
def nollaa_huoneet():
    tyohuone.esineet = [tutkimuspaperi, usb_kotelo]
    kirjasto.esineet = []
    keittio.esineet = [avainkortti, kuppi]
    olohuone.esineet = [muistilappu]
    ruokasali.esineet = []