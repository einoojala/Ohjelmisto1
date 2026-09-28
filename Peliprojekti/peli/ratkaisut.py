from peli.esineet import tietokone
from peli.epaillyt import epaillyt

# --------------------------------------------------
# PIN-KOODIN RATKAISEMINEN
# --------------------------------------------------
# Käynnistää tietokoneen PIN-koodin ratkaisemisen.
def ratkaise_pin_koodi(pelaaja):
    print("\n--- RATKAISE MYSTEERI ---")
    # Jos PIN-koodi on jo ratkaistu, sitä ei tarvitse ratkaista uudelleen.
    if pelaaja.pin_ratkaistu:
        print("Olet jo avannut tietokoneen.")
        return
    print("Edvardin tietokone odottaa PIN-koodia.")

    # Kutsutaan tietokoneen avaamismetodia, joka tarkistaa PIN-koodin.
    tulos = tietokone.avaaminen(pelaaja)

    # False palautetaan main.py:lle, jotta peli voidaan aloittaa alusta.
    if tulos == False:
        return False
    
# --------------------------------------------------
# MURHAAJAN RATKAISEMINEN
# --------------------------------------------------
# Käynnistää murhaajan ratkaisemisen
def ratkaise_murhaaja():
    print("\n--- RATKAISE MURHAAJA ---")
    print("\nVAROITUS!")
    print("Kun valitset epäillyn, annat lopullisen syytöksen.")
    print("Jos arvaat väärin, peli alkaa alusta.")
    print("Varmista siis, että olet tutkinut vihjeet tarkasti.\n")

    print("Kuka murhasi Edvard Kiven?")

    # enumerate antaa jokaiselle epäillylle numeron, jotta pelaaja voi valita epäillyn numerolla.
    for numero, epailty in enumerate(epaillyt, 1):
        print(f"{numero}. {epailty.nimi}")

    print("5. Takaisin")

    while True:
        valinta = input("\nKetä syytät (numero)? ")

        if valinta == "1":
            print("\nSyytät Elisa Kiveä.")
            print("\nVäärä syytös!")
            print("Elisa oli olohuoneessa sähkökatkon aikana.")
            print("Hänen huivinsa löytyi olohuoneesta.")
            print("Todisteet eivät osoita, että Elisa olisi käynyt työhuoneessa.")
            print("Peli alkaa alusta.")

            # False kertoo main.py:lle, että peli pitää aloittaa alusta.
            return False

        elif valinta == "2":
            print("\nSyytät James Kiveä.")
            print("\nVäärä syytös!")
            print("James oli kirjastossa noin kello 22.10.")
            print("Hän ei käynyt Edvardin työhuoneessa.")
            print("Sinulla ei ole tarpeeksi todisteita yhdistää Jamesia murhaan.")
            print("Peli alkaa alusta.")
            return False

        elif valinta == "3":
            print("\nSyytät Viktor Salosta.")
            print("\nVäärä syytös!")
            print("Viktorilla oli motiivi ja hän kävi työhuoneessa.")
            print("Hän kuitenkin poistui työhuoneesta jo kello 22.19.")
            print("Sähkökatko alkoi vasta kello 22.21.")
            print("Viktor ei siis voinut olla työhuoneessa murhan aikana.")
            print("Peli alkaa alusta.")
            return False

        elif valinta == "4":
            print("\nSyytät Sofia Niemeä.")
            print("\nSofia Niemi oli murhaaja.")
            print("Hän käytti avainkorttia päästäkseen työhuoneeseen")
            print("sähkökatkon aikana ja varasti USB-muistitikun.")
            print("\nONNEKSI OLKOON!")
            print("Ratkaisit Edvard Kiven murhan.")

            # Oikean ratkaisun jälkeen pelaaja voi aloittaa uuden pelin tai lopettaa.
            while True:
                print("\nHaluatko pelata uudestaan?")
                print("1. Pelaa uudestaan")
                print("2. Lopeta peli")
                valinta = input("Valitse: ")

                if valinta == "1":
                    # False kertoo main.py:lle, että aloitetaan uusi peli.
                    return False

                elif valinta == "2":
                    # True kertoo main.py:lle, että peli voidaan lopettaa.
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