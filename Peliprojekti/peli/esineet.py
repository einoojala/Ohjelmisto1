# Luokka tavallisille pelissä oleville esineille.
class Esine:
    def __init__(self, nimi, kuvaus, vihje):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje

    # Näyttää esineen kuvauksen ja mahdollisen vihjeen.
    def tutki(self):
        print(f"\n--- {self.nimi.upper()} ---")
        print(self.kuvaus)

        if self.vihje:
            print(f"\nVihje: {self.vihje}")

# Lukittu esine perii Esine-luokan ominaisuudet ja tarvitsee PIN-koodin avaamiseen.
class LukittuEsine(Esine):
    def __init__(self, nimi, kuvaus, vihje, pin):
        # Käytetään Esine-luokan alustusta nimen, kuvauksen ja vihjeen tallentamiseen.
        super().__init__(nimi, kuvaus, vihje)
        self.pin = pin

    # Tarkistaa pelaajan antaman PIN-koodin.
    def avaaminen(self, pelaaja):
        print("\n---- EDVARDIN TIETOKONE ----")
        print(self.kuvaus)

        koodi = input("Syötä 6-numeroinen PIN-koodi (x = poistu): ")
        if koodi.lower() == "x":
            return

        # Tarkistetaan, onko pelaajan antama PIN-koodi oikea.
        if koodi == self.pin:
            print("\nOikea PIN-koodi!")
            print("Tietokone avautuu.")

            # Merkitään pelaajan tiedoissa PIN-koodi ratkaistuksi.
            pelaaja.pin_ratkaistu = True

            print("\n--- SALAINEN VIESTI ---")
            print("USB-muisti ei kadonnut itsestään.")
            print("Sen vei henkilö, joka tiesi tutkimuksesta")
            print("ja pääsi käsiksi työhuoneeseen.")
            print("Mutta kuka tiesi tarpeeksi?")

            # Lisätään tietokoneesta löytyvä viesti pelaajan vihjeisiin.
            pelaaja.lisaa_vihje("USB-muistin vei henkilö, joka tiesi tutkimuksesta ja pääsi käsiksi työhuoneeseen.")

            # True kertoo kutsuvalle funktiolle, että PIN-koodi ratkaistiin onnistuneesti.
            return True

        else:
            print("\nVäärä PIN-koodi.")
            print("Et onnistunut ratkaisemaan mysteeriä.")
            print("Peli alkaa alusta.")
            # False kertoo main.py:lle, että peli pitää aloittaa alusta.
            return False

# --------------------------------------------------
# Esineet
# --------------------------------------------------

tutkimuspaperi = Esine("Tutkimuspaperi",
"""Paperissa on aurinkopaneeliin liittyviä laskelmia.
Paperin alareunassa lukee:
'400 W / paneeli - 25 paneelia.'""",
"400 W ja 25 paneelia liittyvät Edvardin uuden aurinkopaneelin kokonaistehoon.")

avainkortti = Esine("Yrityksen avainkortti",
"""Kortti kuuluu yrityksen henkilökunnalle.
Kortissa lukee:
Sofia Niemi – sihteeri.
Kortilla pääsee myös Edvardin työhuoneeseen.""",
"Sofialla oli pääsy Edvardin työhuoneeseen.")

usb_kotelo = Esine("USB-kotelo",
"""Pieni musta kotelo löytyy työhuoneen laatikosta.
USB-muistitikkua ei kuitenkaan ole kotelon sisällä.""",
"Joku on vienyt USB-muistitikun kotelosta.")

kuppi = Esine("Teekuppi",
"""Keittiöstä löytyy kuppi, jonka pitäisi kuulua Sofialle.
Kupissa ei kuitenkaan ole teetä ja kuppi on täysin kuiva.""",
"Sofian kertomus teen valmistamisesta vaikuttaa epäilyttävältä.")

muistilappu = Esine("Muistilappu", "Siinä lukee jotain", "= O-R-T-K")

tietokone = LukittuEsine("Edvardin tietokone",
"""Tietokone on päällä, mutta näyttö on lukittu.
Näytöllä näkyy vain PIN-koodin syöttökenttä.""",
"Tietokoneessa saattaa olla jotain salaista",
"680024")