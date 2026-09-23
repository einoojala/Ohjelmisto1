# Luokka tavallisille pelissä oleville esineille.
# Jokaisella esineellä on nimi, kuvaus ja siihen liittyvä vihje.
class Esine:

    # Alustetaan uuden esineen tiedot.
    def __init__(self, nimi, kuvaus, vihje):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.vihje = vihje

    # Metodia käytetään, kun pelaaja tutkii inventaariossa olevaa esinettä.
    # Esineen kuvaus ja siihen liittyvä vihje näytetään pelaajalle.
    def tutki(self, pelaaja):
        print(f"\n--- {self.nimi.upper()} ---")
        print(self.kuvaus)

        # Jos esineeseen liittyy vihje, se näytetään pelaajalle
        # ja tallennetaan pelaajan löytämien vihjeiden listaan.
        if self.vihje:
            print(f"\nVihje: {self.vihje}")
            pelaaja.lisaa_vihje(self.vihje)


# LukittuEsine perii Esine-luokan ominaisuudet.
# Tätä luokkaa käytetään esineisiin, joiden avaamiseen tarvitaan PIN-koodi.
class LukittuEsine(Esine):

    # Alustetaan lukitun esineen tiedot sekä PIN-koodi.
    def __init__(self, nimi, kuvaus, vihje, pin):

        # super() kutsuu perityn Esine-luokan __init__-metodia.
        # Näin nimi, kuvaus ja vihje voidaan alustaa samalla tavalla
        # kuin tavallisessa esineessä.
        super().__init__(nimi, kuvaus, vihje)

        # Tallennetaan lukitun esineen PIN-koodi.
        self.pin = pin

    # Metodia käytetään lukitun esineen avaamiseen.
    # Tässä tapauksessa kyseessä on Edvardin tietokone.
    def avaaminen(self, pelaaja):
        print("\n---- EDVARDIN TIETOKONE ----")
        print(self.kuvaus)

        # Pelaaja yrittää ratkaista tietokoneen PIN-koodin.
        # x-valinnalla pelaaja voi poistua PIN-koodin syöttämisestä.
        koodi = input("Syötä 6-numeroinen PIN-koodi (x = poistu): ")

        if koodi.lower() == "x":
            return

        # Tarkistetaan, onko pelaajan antama koodi sama
        # kuin lukitulle esineelle tallennettu PIN-koodi.
        if koodi == self.pin:
            print("\nOikea PIN-koodi!")
            print("Tietokone avautuu.")

            # Tallennetaan pelaajan tietoihin, että PIN-koodi on ratkaistu.
            # Tämän jälkeen pelaaja voi siirtyä ratkaisemaan murhaajan.
            pelaaja.pin_ratkaistu = True

            # Tietokoneesta paljastuva salainen viesti antaa
            # pelaajalle uuden tärkeän vihjeen murhatutkintaan.
            print("\n--- SALAINEN VIESTI ---")
            print("USB-muisti ei kadonnut itsestään.")
            print("Sen vei henkilö, joka tiesi tutkimuksesta")
            print("ja pääsi käsiksi työhuoneeseen.")
            print("Mutta kuka tiesi tarpeeksi?")

            # True kertoo kutsuvalle funktiolle,
            # että PIN-koodi ratkaistiin onnistuneesti.
            return True

        else:
            # Väärä PIN-koodi päättää kyseisen pelikerran.
            print("\nVäärä PIN-koodi.")
            print("Et onnistunut ratkaisemaan mysteeriä.")
            print("Peli alkaa alusta.")

            # False kertoo main.py:lle, että peli pitää aloittaa alusta.
            return False


# --------------------------------------------------
# PELIN TAVALLISET ESINEET
# --------------------------------------------------

# Luodaan tutkimuspaperi Esine-luokan avulla.
# Paperi antaa pelaajalle PIN-koodin ratkaisemiseen liittyvän vihjeen.
tutkimuspaperi = Esine(
    "Tutkimuspaperi",
"""Paperissa on aurinkopaneeliin liittyviä laskelmia.
Paperin alareunassa lukee:
'400 W / paneeli - 25 paneelia.'""",
"400 W ja 25 paneelia liittyvät Edvardin uuden aurinkopaneelin kokonaistehoon.")


# Luodaan yrityksen avainkortti.
# Se antaa pelaajalle tärkeän vihjeen Sofian pääsystä työhuoneeseen.
avainkortti = Esine(
    "Yrityksen avainkortti",
"""Kortti kuuluu yrityksen henkilökunnalle.
Kortissa lukee:
Sofia Niemi – sihteeri.
Kortilla pääsee myös Edvardin työhuoneeseen.""",
"Sofialla oli pääsy Edvardin työhuoneeseen.")


# Luodaan tyhjä USB-kotelo.
# Kotelo antaa vihjeen siitä, että USB-muisti on viety.
usb_kotelo = Esine(
    "USB-kotelo",
"""Pieni musta kotelo löytyy työhuoneen laatikosta.
USB-muistitikkua ei kuitenkaan ole kotelon sisällä.""",
"Joku on vienyt USB-muistitikun kotelosta.")


# Luodaan teekuppi.
# Kuivasta kupista pelaaja saa vihjeen, joka herättää epäilyksiä Sofian kertomuksesta.
kuppi = Esine(
    "Teekuppi",
"""Keittiöstä löytyy kuppi, jonka pitäisi kuulua Sofialle.
Kupissa ei kuitenkaan ole teetä ja kuppi on täysin kuiva.""",
"Sofian kertomus teen valmistamisesta vaikuttaa epäilyttävältä.")


# Luodaan muistilappu.
# Sen merkintä O-R-T-K kertoo pelaajalle PIN-koodin osien oikean järjestyksen.
muistilappu = Esine(
    "Muistilappu",
    "Siinä lukee jotain",
    "= O-R-T-K"
)


# --------------------------------------------------
# LUKITTU ESINE
# --------------------------------------------------

# Luodaan Edvardin tietokone LukittuEsine-luokan avulla.
# Tietokone ei ole tavallinen kerättävä esine, vaan se avataan PIN-koodilla.
tietokone = LukittuEsine(
    "Edvardin tietokone",
"""Tietokone on päällä, mutta näyttö on lukittu.
Näytöllä näkyy vain PIN-koodin syöttökenttä.""",
"Tietokoneessa saattaa olla jotain salaista",
"680024")