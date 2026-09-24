# Tuodaan os-moduuli, jota käytetään tarkistamaan, onko tallennustiedosto olemassa.
import os
# Tuodaan Pelaaja-luokka uuden pelaajan luomista varten.
from peli import Pelaaja
# Tuodaan päävalikko, jossa varsinainen peli tapahtuu.
from peli.paavalikko import paavalikko
# Tuodaan funktio, jolla tallennettu peli voidaan ladata.
from peli.tallennus import lataa_peli
# Tuodaan funktio, jolla huoneiden esineet palautetaan uuteen tilanteeseen.
from peli.huoneet import nollaa_huoneet

# Funktio, jolla luodaan uusi pelaaja.
def uusi_pelaaja():
    nimi = input("Mikä sinun nimesi on? ")

    # Toistetaan kysymystä while True:lla, kunnes pelaaja antaa iän numerona.
    while True:
        try:
            ika = int(input("Kuinka vanha olet? "))
            # Jos onnistui, poistutaan while-silmukasta.
            break

        # Jos käyttäjä kirjoittaa esimerkiksi "kaksitoista", int() aiheuttaa ValueError-virheen.
        except ValueError:
            print("Anna ikä numerona.")

    # Alle 12-vuotias ei voi aloittaa peliä.
    if ika < 12:
        print("\nOlet liian nuori pelaamaan tätä peliä.")
        # Lopetetaan koko ohjelman suoritus.
        exit()

    # Luodaan uusi Pelaaja-olio annetun nimen ja iän perusteella.
    pelaaja = Pelaaja(nimi, ika)

    # Palautetaan kaikki huoneiden esineet alkuperäiseen tilaansa.
    nollaa_huoneet()
    # Palautetaan valmis pelaaja pääohjelmalle.
    return pelaaja

# Pelin pääsilmukka. Sen avulla peli voidaan aloittaa peli uudelleen
while True:
    # Tarkistetaan, onko tallennettu peli olemassa. os.path.exists() palauttaa True tai False.
    if os.path.exists("data/save.txt"):
        # Jos tallennus löytyy, pelaajalle näytetään kaksi vaihtoehtoa.
        print("\n================================")
        print("       TALLENNETTU PELI")
        print("================================")
        print("1. Jatka tallennettua peliä")
        print("2. Aloita uusi peli")
        print("================================")
        # Kysytään valintaa, kunnes käyttäjä antaa 1 tai 2.
        while True:
            valinta = input("Valitse: ")
            if valinta == "1":
                # Ladataan tallennettu peli. lataa_peli() palauttaa valmiin Pelaaja-olion.
                pelaaja = lataa_peli()
                break
            elif valinta == "2":
                # Luodaan kokonaan uusi pelaaja ja uusi pelitilanne.
                pelaaja = uusi_pelaaja()
                break
            else:
                # Jos käyttäjä antaa virheellisen syötteen, kysytään valintaa uudelleen.
                print("Tuntematon valinta. Valitse 1 tai 2.")
    else:
        # Jos tallennustiedostoa ei ole, luodaan uusi peli.
        pelaaja = uusi_pelaaja()
    # Tervehditään pelaajaa nimellä.
    print(f"\nTervetuloa, {pelaaja.nimi}!")

    # Käynnistetään pelin päävalikko. Pelaaja-olio annetaan parametrina, jotta päävalikko
    # voi käyttää pelaajan tietoja, kuten inventaariota ja vihjeitä.
    tulos = paavalikko(pelaaja)
    # Jos päävalikko palauttaa False-arvon, peli aloitetaan alusta.
    # False palautuu esimerkiksi silloin, kun:
    # - pelaaja antaa väärän PIN-koodin
    # - pelaaja syyttää väärää murhaajaa
    # - pelaaja voittaa ja valitsee "Pelaa uudestaan"
    if tulos == False:
        print("\n================================")
        print("       PELI ALKAA ALUSTA")
        print("================================")
        # continue aloittaa while-silmukan uuden kierroksen. Tällöin voidaan luoda uusi peli.
        continue
    # Jos paavalikko ei palauttanut False-arvoa, peli päättyy ja while-silmukka lopetetaan.
    break