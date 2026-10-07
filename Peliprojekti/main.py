import os
import sys
from peli import Pelaaja
from peli.paavalikko import paavalikko, nayta_ohjeet
from peli.tallennus import lataa_peli
from peli.huoneet import nollaa_huoneet

# ==================================================
# UUSI PELAAJA
# ==================================================
# Luo ja palauttaa uuden pelaajan.
def uusi_pelaaja():
    while True:
        nimi = input("Mikä sinun nimesi on? ")

        # Tarkistetaan, onko nimi tyhjä ylimääräisten välilyöntien poistamisen jälkeen.
        if not nimi.strip():
            print("Anna nimi.")
            continue
        if nimi.isdigit():
            print("Nimi ei voi olla pelkkää numeroa.")
            continue
        
        break

    while True:
        try:
            ika = int(input("Kuinka vanha olet? "))
            if ika >= 100:
                print("\nLuulen, että annoit väärän iän.")
                continue
            if ika < 12:
                print("\nOlet liian nuori pelaamaan tätä peliä.")
                sys.exit()

            break

        except ValueError:
            print("Anna ikä numerona.")

    # Luodaan uusi pelaaja ja palautetaan huoneet alkuperäiseen tilaansa.
    pelaaja = Pelaaja(nimi, ika)
    nollaa_huoneet()
    return pelaaja

# ==================================================
# PELIN VALINTA
# ==================================================
# Käsittelee tallennetun pelin valitsemisen tai uuden pelin aloittamisen.
def pelin_valinta():
    while True:
        print("\n================================")
        print("       TALLENNETTU PELI")
        print("================================")
        print("1. Jatka tallennettua peliä")
        print("2. Aloita uusi peli")
        print("================================")

        valinta = input("Valitse: ")

        if valinta == "1":
            try:
                pelaaja = lataa_peli()
                return pelaaja

            # Rikkinäinen tallennus poistetaan, jotta peli voidaan aloittaa uudelleen.
            except (KeyError, ValueError, IndexError):
                print("\nTallennustiedosto on virheellinen tai vahingoittunut.")
                print("Aloitetaan uusi peli.")
                os.remove("data/save.json")
                return uusi_pelaaja()

        elif valinta == "2":
            # Varmistetaan, että pelaaja haluaa aloittaa uuden pelin.
            varmistus = input("\nHaluatko varmasti aloittaa uuden pelin? Nykyinen tallennus poistetaan. (k/e): ").lower()

            if varmistus == "k":
                # Poistetaan vanha tallennus ennen uuden pelin aloittamista.
                os.remove("data/save.json")
                return uusi_pelaaja()
            elif varmistus == "e":
                # Palataan takaisin tallennetun pelin valintaan.
                continue
            else:
                print("Vastaa k tai e.")

# ==================================================
# TUTKINTA EPÄONNISTUI
# ==================================================
# Käsittelee tilanteen, jossa tutkinta epäonnistuu väärän PIN-koodin tai syytöksen jälkeen.
def tutkinta_epaonnistui():
    print("\n================================")
    print("      TUTKINTA EPÄONNISTUI")
    print("================================")
    print("1. Aloita uusi peli")
    print("2. Lopeta peli")

    while True:
        valinta = input("Valitse: ")

        if valinta == "1":
            # Vanha tallennus poistetaan ennen uuden pelin aloittamista.
            if os.path.exists("data/save.json"):
                os.remove("data/save.json")
            return "uusi"

        elif valinta == "2":
            print("\nPeli lopetetaan.")
            # Lopetetaan main()-funktio ja samalla koko peli.
            return None
        else:
            print("Tuntematon valinta. Valitse 1 tai 2.")

# ==================================================
# PELIN KÄYNNISTÄMINEN
# ==================================================
# Käynnistää pelin ja hallitsee pelin pääsilmukkaa.
def main():
    # Pelin pääsilmukka mahdollistaa pelin aloittamisen tarvittaessa uudelleen.
    while True:
        # Tarkistetaan, onko tallennettu peli olemassa.
        if os.path.exists("data/save.json"):
            pelaaja = pelin_valinta()
        else:
            # Luodaan uusi peli, jos tallennustiedostoa ei ole.
            pelaaja = uusi_pelaaja()
        print(f"\nTervetuloa, {pelaaja.nimi}!")
        nayta_ohjeet()

        # Käynnistetään päävalikko ja annetaan sille pelaajan tiedot.
        # Palautettu tulos tallennetaan muuttujaan.
        tulos = paavalikko(pelaaja)

        # Jos päävalikko palauttaa False-arvon, peli epäonnistui.
        # Tämä tapahtuu esimerkiksi väärän PIN-koodin tai syytöksen jälkeen.
        if tulos is False:
            tulos = tutkinta_epaonnistui()
            # Jos tutkinta_epaonnistui() palauttaa None, pelaaja halusi lopettaa pelin.
            # return lopettaa main()-funktion ja samalla koko pelin.
            if tulos is None:
                return
            # Jos pelaaja haluaa aloittaa uuden pelin, palataan main()-silmukan alkuun.
            elif tulos == "uusi":
                continue

        # Jos oikea murhaaja ratkaistiin ja pelaaja haluaa aloittaa uuden pelin,
        # vanha tallennus poistetaan ennen uuden pelin aloittamista.
        elif tulos == "uusi":
            if os.path.exists("data/save.json"):
                os.remove("data/save.json")

            continue
        else:
            # True tarkoittaa, että peli päättyi onnistuneeseen murhaajan ratkaisuun.
            # None tarkoittaa, että pelaaja lopetti pelin päävalikon kautta.
            # break lopettaa while True -silmukan, ja koska sen jälkeen ei ole enää koodia, main() funktio päättyy.    
            break

# Käynnistetään peli vain, kun main.py suoritetaan suoraan.
if __name__ == "__main__":
    main()