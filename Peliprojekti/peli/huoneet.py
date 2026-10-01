from peli.esineet import tutkimuspaperi, avainkortti, usb_kotelo, kuppi, paivakirja, muistilappu

class Huone:
    def __init__(self, nimi, kuvaus, vihje, esineet):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje
        self.esineet = esineet

    # Määrittää, miten huone tulostetaan pelaajalle.
    def __str__(self):
        return f"\n---- {self.nimi.upper()} ----\n{self.kuvaus}"

    # Antaa pelaajalle mahdollisuuden tutkia huonetta tarkemmin tutki_huonetta funktion yhteydessä.
    def tutki_tarkemmin(self, pelaaja):
        # Saman huoneen tarkempi vihje voidaan tutkia vain kerran.
        if self in pelaaja.tutkitut_huoneet:
            print("\nOlet jo tutkinut tämän huoneen tarkemmin.")
            return

        while True:
            vastaus = input("\nHaluatko tutkia huonetta tarkemmin? (k/e): ").lower()

            if vastaus == "k":
                print("\n---- TARKEMPI TUTKIMUS ----")
                print(self.vihje)

                pelaaja.lisaa_vihje(self.vihje)
                pelaaja.tutkitut_huoneet.append(self)

                print("\nPoistut huoneesta.")
                return
            elif vastaus == "e":
                print("\nPoistut huoneesta.")
                return
            else:
                print("Vastaa k tai e.")
# ==================================================
# PELIN HUONEET
# ==================================================
tyohuone = Huone("Työhuone",
"""Albertin työhuone on suuri ja hämärä.
Pöydällä on tietokone ja useita papereita.
Seinällä oleva kello on pysähtynyt aikaan 22:21.""",
"""Albertin pöydällä on Viktorilta viesti: Jos et anna minulle osuuttani, kerron kaikille tutkimuksestasi.""",
 [tutkimuspaperi, usb_kotelo])

kirjasto = Huone("Kirjasto",
"""Kirjastossa on korkeat kirjahyllyt ja vanha kirjoituspöytä.
Jotkut kirjat näyttävät olevan hieman vinossa.""",
"""Albertin tutkimuskansiosta löytyy Jamesin käsialaa: Paljonko tästä teknologiasta voisi saada rahaa?""",
[paivakirja])

keittio = Huone("Keittiö",
"""Keittiössä on vielä illallisen jälkiä.
Pöydällä on astioita ja vedenkeitin.
Huoneessa on hieman outo tunnelma.""",
"""Sofia kertoi valmistaneensa teetä ennen sähkökatkoa, mutta vedenkeitin on kylmä ja kuppi kuiva.""", 
[avainkortti, kuppi])

olohuone = Huone("Olohuone",
"""Olohuoneessa on suuri sohva, takka ja vanha taulu.
Kaikki näyttää ensisilmäyksellä normaalilta.""",
"""Elisan huivi löytyy sohvan vierestä. Huivin reunassa on tumma tahra. Taulussa on merkintä: kuusi vuotta sitten kaikki muuttui.""", 
[muistilappu])

ruokasali = Huone("Ruokasali",
"""Ruokasalissa on pitkä pöytä, jonka ympärillä on viisi tuolia.
Illallisen jäljet ovat edelleen näkyvissä.""",
"""Illallisen jälkeen Albertin paikalla on lappu: Uusi paneeli 28 %, vanha paneeli 20 %. Tehokkuusero kertoo numeron.""",
[])

# Lista kaikista pelin huoneista, jota käytetään päävalikossa huoneen valitsemiseen.
huoneet = [tyohuone, kirjasto, keittio, olohuone, ruokasali]

# Palauttaa huoneiden esineet alkuperäiseen tilaansa uuden pelin alussa.
def nollaa_huoneet():
    tyohuone.esineet = [tutkimuspaperi, usb_kotelo]
    kirjasto.esineet = [paivakirja]
    keittio.esineet = [avainkortti, kuppi]
    olohuone.esineet = [muistilappu]
    ruokasali.esineet = []