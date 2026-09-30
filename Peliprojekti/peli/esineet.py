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
        if koodi == self.pin:
            print("\nOikea PIN-koodi!")
            print("Tietokone avautuu.")

            # Merkitään pelaajan tiedoissa PIN-koodi ratkaistuksi.
            pelaaja.pin_ratkaistu = True

            print("\n--- SALAINEN VIESTI ---")
            print("Edvardin tietokoneelta löytyy viimeinen merkintä:")
            print("Joku on osoittanut huomattavaa kiinnostusta tutkimukseeni.")
            print("Hänellä on ollut mahdollisuus nähdä työni")
            print("ja päästä käsiksi työhuoneeseen.")
            print("Jos minulle tapahtuu jotain, näitä tietoja kannattaa tutkia tarkemmin.")

            # Lisätään tietokoneesta löytyvä viesti pelaajan vihjeisiin.
            pelaaja.lisaa_vihje("Epäillyllä oli tietoa tutkimuksesta ja pääsy työhuoneeseen.")
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
Muistiinpanoissa pohditaan, miten aurinkoenergia voisi vähentää riippuvuutta fossiilisista polttoaineista.
Paperin alareunassa lukee: "400 W / paneeli - 25 paneelia.""",
"Laske teho. Kaksi ensimmäistä ratkaisevat.")

avainkortti = Esine("Yrityksen avainkortti",
"""Kortti kuuluu yrityksen henkilökunnalle.
Kortissa lukee:
Sofia Niemi - sihteeri.
Kortilla pääsee myös Edvardin työhuoneeseen.""",
"Sofialla oli pääsy Edvardin työhuoneeseen.")

usb_kotelo = Esine("USB-kotelo",
"""Pieni musta kotelo löytyy työhuoneen laatikosta.
USB-muistitikkua ei ole. Kotelon pohjassa lukee: J.K.""",
"USB-kotelossa on Jamesin nimikirjaimet.")

kuppi = Esine("Teekuppi",
"""Keittiöstä löytyy kuppi, jonka pitäisi kuulua Sofialle.
Kupissa ei kuitenkaan ole teetä ja kuppi on täysin kuiva.""",
"Sofian kertomus teen valmistamisesta vaikuttaa epäilyttävältä.")

paivakirja = Esine("Päiväkirja",
"""Vanha päiväkirja löytyy kirjahyllyn välistä. Useat sivut ovat täynnä 
aurinkoenergiaan liittyviä muistiinpanoja. Yksi sivu on revitty irti.""",
"Päiväkirjan merkinnän mukaan ensimmäinen toimiva prototyyppi valmistui vuonna 2024.")

muistilappu = Esine("Muistilappu", "Muistilapussa on mysteeri", "= O(1N) - R(1N) - T(2N) - P(2N)")

tietokone = LukittuEsine("Edvardin tietokone",
"""Tietokone on päällä, mutta näyttö on lukittu.
Näytöllä näkyy vain PIN-koodin syöttökenttä.""",
"Tietokoneessa saattaa olla jotain salaista",
"681024")