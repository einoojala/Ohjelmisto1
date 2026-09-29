# Tuodaan os-moduuli tallennustiedoston tarkistamista varten.
import os
from peli import Pelaaja
from peli.paavalikko import paavalikko, nayta_ohjeet
from peli.tallennus import lataa_peli
from peli.huoneet import nollaa_huoneet

# Luo uuden pelaajan ja palauttaa Pelaaja-olion.
def uusi_pelaaja():
    nimi = input("Mikä sinun nimesi on? ")

    # Ikää kysytään, kunnes pelaaja antaa sen numerona.
    while True:
        try:
            ika = int(input("Kuinka vanha olet? "))
            break

        except ValueError:
            print("Anna ikä numerona.")

    # Alle 12-vuotias ei voi aloittaa peliä.
    if ika < 12:
        print("\nOlet liian nuori pelaamaan tätä peliä.")
        exit()

    # Luodaan uusi pelaaja ja palautetaan huoneet alkuperäiseen tilaansa.
    pelaaja = Pelaaja(nimi, ika)
    nollaa_huoneet()
    return pelaaja

# Käynnistää pelin
def main():
    # Pelin pääsilmukka mahdollistaa pelin aloittamisen uudelleen tarvittaessa.
    while True:
        # Tarkistetaan, onko tallennettu peli olemassa. os.path.exists() palauttaa True tai False.
        if os.path.exists("data/save.txt"):
            print("\n================================")
            print("       TALLENNETTU PELI")
            print("================================")
            print("1. Jatka tallennettua peliä")
            print("2. Aloita uusi peli")
            print("================================")
            while True:
                valinta = input("Valitse: ")

                if valinta == "1":
                    try:
                        pelaaja = lataa_peli()
                        break
                    # Rikkinäinen tallennus poistetaan, jotta peli voidaan aloittaa uudelleen.
                    except (KeyError, ValueError, IndexError):
                        print("\nTallennustiedosto on virheellinen tai vahingoittunut.")
                        print("Aloitetaan uusi peli.")
                        os.remove("data/save.txt")
                        pelaaja = uusi_pelaaja()
                        break

                # Luodaan uusi peli ja poistetaan vanha tallennus.
                elif valinta == "2":
                    if os.path.exists("data/save.txt"):
                        os.remove("data/save.txt")

                    pelaaja = uusi_pelaaja()
                    break
                else:
                    print("Tuntematon valinta. Valitse 1 tai 2.")
        else:
            # Jos tallennustiedostoa ei ole, luodaan uusi peli.
            pelaaja = uusi_pelaaja()

        print(f"\nTervetuloa, {pelaaja.nimi}!")

        # Näytetään pelin tarina ja ohjeet.
        nayta_ohjeet()

        # Käynnistetään päävalikko ja annetaan sille pelaajan tiedot.
        tulos = paavalikko(pelaaja)

        # Jos päävalikko palauttaa False-arvon, peli aloitetaan alusta.
        # Tämä tapahtuu esimerkiksi väärän PIN-koodin tai syytöksen jälkeen.
        if tulos is False:
            print("\n================================")
            print("       PELI ALKAA ALUSTA")
            print("================================")

            # Vanha tallennus poistetaan, koska peli aloitetaan kokonaan alusta.
            if os.path.exists("data/save.txt"):
                os.remove("data/save.txt")
            continue
        # Jos paavalikko ei palauttanut False-arvoa, peli päättyy ja while-silmukka lopetetaan.
        break
# Käynnistetään peli vain, kun main.py suoritetaan suoraan.
if __name__ == "__main__":
    main()