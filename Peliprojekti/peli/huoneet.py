# Tuodaan huoneissa olevat esineet Näin jokaiselle huoneelle voidaan määrittää sen esineet.
from peli.esineet import tutkimuspaperi, avainkortti, usb_kotelo, kuppi, muistilappu
# Luokka, jonka avulla luodaan pelin huoneet.
class Huone:
    # Jokaisella huoneella on nimi, kuvaus, mahdolliset vihjeet ja esineet.
    def __init__(self, nimi, kuvaus, vihje, esineet):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje
        self.esineet = esineet

    # __str__ määrittää, miten huone tulostetaan pelaajalle.
    def __str__(self):
        return f"\n---- {self.nimi.upper()} ----\n{self.kuvaus}"

    # Metodi, kun pelaaja haluaa tutkia huonetta tarkemmin tai palata takaisin.
    def tutki_tarkemmin(self, pelaaja):
        # while True:lla kysytään uudestaan, jos pelaaja antaa virheellisen vastauksen.
        while True:
            vastaus = input("\nHaluatko tutkia huonetta tarkemmin? (kyllä/ei): ").lower()
            if vastaus == "kyllä":
                print("\n---- TARKEMPI TUTKIMUS ----")
                print(self.vihje)

                # Huoneesta löytyvä vihje lisätään pelaajan löytämien vihjeiden listaan.
                pelaaja.lisaa_vihje(self.vihje)
                print("\nPoistut huoneesta.")
                return

            elif vastaus == "ei":
                print("\nPoistut huoneesta.")
                return
            else:
                # Jos vastaus ei ole "kyllä" tai "ei", kysytään vastaus uudelleen.
                print("Vastaa kyllä tai ei.")

# --------------------------------------------------
# PELIN HUONEET
# --------------------------------------------------
# Työhuoneessa pelaaja löytää tutkimuspaperin ja USB-kotelon.
# Huoneen tarkemmasta tutkimisesta saadaan myös PIN-koodiin liittyvä vihje.
tyohuone = Huone("Työhuone",
"""Edvardin työhuone on suuri ja hämärä.
Pöydällä on tietokone ja useita papereita.
Seinällä oleva kello on pysähtynyt.""",
"""Tutkit työpöytää tarkemmin.
Löydät paperin, jossa lukee:
'400 x 25. Muista kokonaisteho ja käytä viimeisiä numeroita.'""", [tutkimuspaperi, usb_kotelo])

# Kirjastosta löytyy vihje, joka antaa PIN-koodiin vuoden 2024.
kirjasto = Huone("Kirjasto",
"""Kirjastossa on korkeat kirjahyllyt ja vanha kirjoituspöytä.
Jotkut kirjat näyttävät olevan hieman vinossa.""",
"""Tutkit kirjahyllyä tarkemmin.
Yhden tutkimuskansion välistä löytyy merkintä:
'Ensimmäinen toimiva prototyyppi valmistui vuonna 2024.'""", [])

# Keittiössä pelaaja voi löytää Sofian avainkortin ja teekupin, joista saa murhaan liittyviä vihjeitä.
keittio = Huone("Keittiö",
"""Keittiössä on vielä illallisen jälkiä.
Pöydällä on astioita ja vedenkeitin.
Huoneessa on hieman outo tunnelma.""",
"""Tutkit keittiötä tarkemmin.
Vedenkeitin on kylmä ja yksi kupeista on täysin kuiva.
Seinäkello näyttää aikaa 22.17.""", [avainkortti, kuppi])

# Olohuoneesta löytyy muistilappu,ja tarkemmassa tutkimisessa saadaan PIN-koodin 1. numero.
olohuone = Huone("Olohuone",
"""Olohuoneessa on suuri sohva, takka ja vanha taulu.
Kaikki näyttää ensisilmäyksellä normaalilta.""",
"""Tutkit sohvan ympäristöä tarkemmin.
Sohvan vierestä löytyy Elisan huivi.
Pöydällä oleva lasi on lähes koskematon.
Lisäksi taulussa on merkintä:
kuusi vuotta sitten kaikki muuttui""", [muistilappu])

# Ruokasalista löytyvä lappu antaa PIN-koodin seuraavan osan, pelaajan täytyy laskea vähenyslasku.
ruokasali = Huone("Ruokasali",
"""Ruokasalissa on pitkä pöytä, jonka ympärillä on viisi tuolia.
Illallisen jäljet ovat edelleen näkyvissä.""",
"""Illallisen jälkeen Edvardin paikalla on pieni lappu.
Lapussa lukee:
Uusi paneeli: 28 %
Vanha paneeli: 20 %""", [])

# Palautetaan kaikkien huoneiden esineet alkuperäiseen tilanteeseen, kun pelaaja aloittaa uuden pelin.
# Esineitä poistetaan huoneista sitä mukaa, kun niitä kerätään
# joten huoneiden esinelistat täytyy palauttaa alkuperäisiksi uuden pelin alussa.
def nollaa_huoneet():
    tyohuone.esineet = [tutkimuspaperi, usb_kotelo]
    kirjasto.esineet = []
    keittio.esineet = [avainkortti, kuppi]
    olohuone.esineet = [muistilappu]
    ruokasali.esineet = []