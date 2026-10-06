class Esine:
    def __init__(self, nimi, kuvaus, vihje):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje

    def tutki(self):
        print(f"\n--- {self.nimi.upper()} ---")
        print(self.kuvaus)
        print(f"\nVihje: {self.vihje}")

# Lukittu esine perii Esine-luokan ominaisuudet ja tarvitsee PIN-koodin avaamiseen.
class LukittuEsine(Esine):
    def __init__(self, nimi, kuvaus, vihje, pin):
        super().__init__(nimi, kuvaus, vihje)
        self.pin = pin

# ==================================================
# Kerättävät esineet
# ==================================================
tutkimuspaperi = Esine("Tutkimuspaperi",
"""Paperissa on aurinkopaneeliin liittyviä laskelmia.
Muistiinpanoissa pohditaan, miten aurinkoenergia voisi vähentää riippuvuutta fossiilisista polttoaineista.
Paperin alareunassa lukee: "400 W / paneeli - 25 paneelia.""",
"Laske teho. Kaksi ensimmäistä numeroa ratkaisevat.")

avainkortti = Esine("Yrityksen avainkortti",
"""Kortti kuuluu yrityksen henkilökunnalle.
Kortissa lukee:
Sofia Niemi - sihteeri.
Kortilla pääsee myös Albertin työhuoneeseen.""",
"Sofialla oli pääsy Albertin työhuoneeseen.")

usb_kotelo = Esine("USB-kotelo",
"""Pieni musta kotelo löytyy työhuoneen laatikosta.
USB-muistitikkua ei ole. Kotelon pohjassa lukee: J.K.""",
"USB-kotelossa on Jamesin nimikirjaimet.")

kuppi = Esine("Teekuppi",
"""Keittiöstä löytyy kuppi, jonka pitäisi kuulua Sofialle.
Kupissa ei kuitenkaan ole teetä ja kuppi on täysin kuiva,
eikä vedenkeittimessä ole merkkejä siitä, että sitä olisi käytetty.""",
"Sofian kertomus teen valmistamisesta vaikuttaa epäilyttävältä.")

paivakirja = Esine("Päiväkirja",
"""Vanha päiväkirja löytyy kirjahyllyn välistä. Useat sivut ovat täynnä 
aurinkoenergiaan liittyviä muistiinpanoja. Yksi sivu on revitty irti.""",
"Päiväkirjan merkinnän mukaan ensimmäinen toimiva prototyyppi valmistui vuonna 2025.")

muistilappu = Esine("Muistilappu", "Muistilapussa on mysteeri",
"koodi = Olo.(1Num) - Ruok.(1 Num) - Tutk.(2 Num) - Päiv.(2 Num)")

# Lista kaikista pelin kerättävistä esineistä, jota käytetään esimerkiksi tallennuksessa.
esineet = [tutkimuspaperi, avainkortti, usb_kotelo, kuppi, paivakirja, muistilappu]

# ==================================================
# Lukittu esine
# ==================================================
tietokone = LukittuEsine("Albertin tietokone",
"""Tietokone on päällä, mutta näyttö on lukittu.
Näytöllä näkyy vain PIN-koodin syöttökenttä.""",
"Tietokoneessa saattaa olla jotain salaista",
"681025")