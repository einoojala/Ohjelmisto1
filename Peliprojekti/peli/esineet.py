# Luokka tavallisille pelissä oleville esineille.
class Esine:
    # Alustetaan uuden esineen tiedot, nimi, kuvaus ja mahdollinen vihje
    def __init__(self, nimi, kuvaus, vihje):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje

    # Metodi, kun pelaaja tutkii inventaariossa olevaa esinettä.
    # Esineen kuvaus ja siihen liittyvä vihje näytetään pelaajalle.
    def tutki(self, pelaaja):
        print(f"\n--- {self.nimi.upper()} ---")
        print(self.kuvaus)

        # Jos on vihje, näytetään pelaajalle ja tallennetaan pelaajan löytämien vihjeiden listaan.
        if self.vihje:
            print(f"\nVihje: {self.vihje}")
            pelaaja.lisaa_vihje(self.vihje)

# LukittuEsine perii Esine-luokan ominaisuudet. käytetään esineisiin, joihin tarvitaan PIN-koodi.
class LukittuEsine(Esine):
    # Alustetaan lukitun esineen tiedot sekä PIN-koodi.
    def __init__(self, nimi, kuvaus, vihje, pin):
        # super() kutsuu perityn Esine-luokan __init__-metodia.
        # Näin nimi, kuvaus ja vihje voidaan alustaa samalla tavalla kuin normi esineessä.
        super().__init__(nimi, kuvaus, vihje)
        # Tallennetaan lukitun esineen PIN-koodi.
        self.pin = pin

    # Metodia käytetään lukitun esineen avaamiseen.
    def avaaminen(self, pelaaja):
        print("\n---- EDVARDIN TIETOKONE ----")
        print(self.kuvaus)

        # Pelaaja yrittää ratkaista tietokoneen PIN-koodin. "x" poistuu.
        koodi = input("Syötä 6-numeroinen PIN-koodi (x = poistu): ")
        if koodi.lower() == "x":
            return

        # Tarkistetaan, onko koodi sama kuin lukitulle esineelle tallennettu PIN-koodi.
        if koodi == self.pin:
            print("\nOikea PIN-koodi!")
            print("Tietokone avautuu.")

            # Tallennetaan pelaajan tietoihin, että PIN-koodi on ratkaistu. 
            # Tämän jälkeen pelaaja voi siirtyä ratkaisemaan murhaajan.
            pelaaja.pin_ratkaistu = True

            # Tietokoneesta paljastuva salainen viesti antaa uuden tärkeän vihjeen murhatutkintaan.
            print("\n--- SALAINEN VIESTI ---")
            print("USB-muisti ei kadonnut itsestään.")
            print("Sen vei henkilö, joka tiesi tutkimuksesta")
            print("ja pääsi käsiksi työhuoneeseen.")
            print("Mutta kuka tiesi tarpeeksi?")
            # True kertoo kutsuvalle funktiolle, että PIN-koodi ratkaistiin onnistuneesti.
            return True

        else:
            # Väärä PIN-koodi päättää meneillään olevan pelikerran.
            print("\nVäärä PIN-koodi.")
            print("Et onnistunut ratkaisemaan mysteeriä.")
            print("Peli alkaa alusta.")
            # False kertoo main.py:lle, että peli pitää aloittaa alusta.
            return False

# --------------------------------------------------
# Esineet
# --------------------------------------------------

# Luodaan tutkimuspaperi
# Paperi antaa PIN-koodin ratkaisemiseen liittyvän vihjeen.
tutkimuspaperi = Esine("Tutkimuspaperi",
"""Paperissa on aurinkopaneeliin liittyviä laskelmia.
Paperin alareunassa lukee:
'400 W / paneeli - 25 paneelia.'""",
"400 W ja 25 paneelia liittyvät Edvardin uuden aurinkopaneelin kokonaistehoon.")


# Luodaan yrityksen avainkortti.
# Se antaa pelaajalle tärkeän vihjeen Sofian pääsystä työhuoneeseen.
avainkortti = Esine("Yrityksen avainkortti",
"""Kortti kuuluu yrityksen henkilökunnalle.
Kortissa lukee:
Sofia Niemi – sihteeri.
Kortilla pääsee myös Edvardin työhuoneeseen.""",
"Sofialla oli pääsy Edvardin työhuoneeseen.")

# Luodaan tyhjä USB-kotelo.
# Kotelo antaa vihjeen siitä, että USB-muisti on viety.
usb_kotelo = Esine("USB-kotelo",
"""Pieni musta kotelo löytyy työhuoneen laatikosta.
USB-muistitikkua ei kuitenkaan ole kotelon sisällä.""",
"Joku on vienyt USB-muistitikun kotelosta.")


# Luodaan teekuppi.
# Kuivasta kupista pelaaja saa vihjeen, joka herättää epäilyksiä Sofian kertomuksesta.
kuppi = Esine("Teekuppi",
"""Keittiöstä löytyy kuppi, jonka pitäisi kuulua Sofialle.
Kupissa ei kuitenkaan ole teetä ja kuppi on täysin kuiva.""",
"Sofian kertomus teen valmistamisesta vaikuttaa epäilyttävältä.")

# Luodaan muistilappu.
# Sen merkintä O-R-T-K kertoo PIN-koodin osien oikean järjestyksen.
muistilappu = Esine("Muistilappu", "Siinä lukee jotain", "= O-R-T-K")

# Luodaan Edvardin tietokone LukittuEsine-luokan avulla.
# Ei ole tavallinen kerättävä esine, vaan se avataan PIN-koodilla.
tietokone = LukittuEsine("Edvardin tietokone",
"""Tietokone on päällä, mutta näyttö on lukittu.
Näytöllä näkyy vain PIN-koodin syöttökenttä.""",
"Tietokoneessa saattaa olla jotain salaista",
"680024")