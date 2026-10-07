from peli.esineet import tietokone
from peli.epaillyt import epaillyt

# ==================================================
# PIN-KOODIN RATKAISEMINEN
# ==================================================
# Käytetään paavalikko() funktiossa, kun pelaaja valitsee PIN-koodin ratkaisemisen.
def ratkaise_pin_koodi(pelaaja):
    print("\n--- RATKAISE MYSTEERI ---")

    # Jos PIN-koodi on jo ratkaistu, ei tarvitse ratkaista uudelleen.
    if pelaaja.pin_ratkaistu:
        print("Olet jo avannut tietokoneen.")
        return

    print("Albertin tietokone odottaa PIN-koodia.")
    print(tietokone.kuvaus)

    # Pelaajalla on kaksi yritystä.
    yritykset = 2
    while yritykset > 0:
        koodi = input(f"\nSyötä 6-numeroinen PIN-koodi (yrityksiä jäljellä: {yritykset}, x = poistu): ")

        if koodi.lower() == "x":
            return

        if not koodi.isdigit() or len(koodi) != 6:
            print("PIN-koodin täytyy olla kuusi numeroa.")
            continue

        if koodi == tietokone.pin:
            print("\nOikea PIN-koodi!")
            print("Tietokone avautuu.")
            # Merkitään pelaajan tietoihin, että PIN-koodi on ratkaistu.
            pelaaja.pin_ratkaistu = True

            print("\n--- SALAINEN VIESTI ---")
            print("Albertin tietokoneelta löytyy viimeinen merkintä:")
            print("Joku on osoittanut erityistä kiinnostusta tutkimukseeni.")
            print("Hän on päässyt tutustumaan tutkimukseen")
            print("ja hänellä on ollut pääsy työhuoneeseeni.")
            print("Jos minulle tapahtuu jotain, näitä tietoja kannattaa tutkia tarkemmin.")
            pelaaja.lisaa_vihje("Epäillyllä oli tietoa tutkimuksesta ja pääsy työhuoneeseen.")
            return

        # Väärä PIN-koodi kuluttaa yhden yrityksen.
        yritykset -= 1

        if yritykset > 0:
            print("\nVäärä PIN-koodi.")
            print(f"Sinulla on vielä {yritykset} yritys.")

        else:
            print("\nVäärä PIN-koodi.")
            print("Molemmat yritykset käytettiin.")
            print("Et onnistunut ratkaisemaan PIN-koodia.")
            print("Tutkinta epäonnistui.")
            # False kertoo paavalikko.py:lle, että tutkinta epäonnistui.
            # paavalikko.py välittää tiedon main.py:lle.
            return False
# ==================================================
# MURHAAJAN RATKAISEMINEN
# ==================================================
# Käytetään paavalikko() funktiossa, kun pelaaja valitsee murhaajan ratkaisemisen.
def ratkaise_murhaaja(pelaaja):
    print("\n--- RATKAISE MURHAAJA ---")
    print("\nVAROITUS!")
    print("Valitsemalla epäillyn syytät häntä murhasta.")
    print("Jos valitset väärän henkilön, tutkinta epäonnistuu.")
    print("Tutki siis kaikki vihjeet tarkasti ennen kuin teet päätöksen.")

    print("\nKuka murhasi Albert Kiven?")

    # enumerate antaa epäillyille numerot 1 alkaen.
    for numero, epailty in enumerate(epaillyt, 1):
        print(f"{numero}. {epailty.nimi}")
    print("5. Takaisin")

    while True:
        valinta = input("\nKetä syytät (numero)? ")

        if valinta == "1":
            print("\nSyytät Elisa Kiveä.")
            print("\nVäärä syytös!")
            print("Elisa oli sähkökatkon aikana olohuoneessa.")
            print("Hänen huivinsa löytyi olohuoneesta.")
            print("Mikään todiste ei osoita, että Elisa olisi ollut työhuoneessa.")
            print("Tutkinta epäonnistui.")
            # False kertoo paavalikko.py:lle, että tutkinta epäonnistui.
            # paavalikko.py välittää tiedon main.py:lle.
            return False

        elif valinta == "2":
            print("\nSyytät James Kiveä.")
            print("\nVäärä syytös!")
            print("James oli kirjastossa noin kello 22.10.")
            print("Hän ei käynyt Albertin työhuoneessa.")
            print("Sinulla ei ole tarpeeksi todisteita yhdistämään Jamesia murhaan.")
            print("Tutkinta epäonnistui.")
            return False

        elif valinta == "3":
            print("\nSyytät Viktor Salosta.")
            print("\nVäärä syytös!")
            print("Viktorilla oli motiivi ja hän kävi työhuoneessa.")
            print("Hän kuitenkin poistui työhuoneesta jo kello 22.20.")
            print("Sähkökatko alkoi vasta kello 22.21.")
            print("Viktor ei siis voinut olla työhuoneessa murhan aikaan.")
            print("Tutkinta epäonnistui.")
            return False

        elif valinta == "4":
            print("Sofia Niemi oli murhaaja.")
            print("\nSofialla oli pääsy työhuoneeseen avainkortillaan.")
            print("\nHänen kertomuksensa teestä ei pitänyt paikkaansa.")
            print("Sähkökatkon aikana hän pääsi työhuoneeseen")
            print("ja varasti sieltä USB-muistitikun.")
            print("\nONNEKSI OLKOON!")
            print("Ratkaisit Albert Kiven murhan.")

            # Oikean ratkaisun jälkeen pelaaja voi aloittaa uuden pelin tai lopettaa.
            while True:
                print("\nHaluatko pelata uudestaan?")
                print("1. Pelaa uudestaan")
                print("2. Lopeta peli")
                valinta = input("Valitse: ")

                if valinta == "1":
                    # Ilmoittaa paavalikko.py:lle, että pelaaja haluaa aloittaa uuden pelin.
                    return "uusi"
                elif valinta == "2":
                    print("\nPeli lopetetaan.")
                    print(f"Kiitos pelaamisesta, {pelaaja.nimi}!")
                    # True kertoo paavalikko.py:lle, että peli voidaan lopettaa.
                    return True
                else:
                    print("Valitse 1 tai 2.")

        elif valinta == "5":
            print("\nPalaat päävalikkoon.")
            # None kertoo paavalikko.py:lle, että pelaaja haluaa palata päävalikkoon.
            return None
        else:
            print("\nTuntematon valinta.")
            print("Valitse numero 1-5.")