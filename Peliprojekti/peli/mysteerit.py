from peli.esineet import tietokone
from peli.epaillyt import epaillyt

# ==================================================
# PIN-KOODIN RATKAISEMINEN
# ==================================================
# Käynnistää tietokoneen PIN-koodin ratkaisemisen.
def ratkaise_pin_koodi(pelaaja):
    print("\n--- RATKAISE MYSTEERI ---")

    # Jos PIN-koodi on jo ratkaistu, sitä ei tarvitse ratkaista uudelleen.
    if pelaaja.pin_ratkaistu:
        print("Olet jo avannut tietokoneen.")
        return

    print("Albertin tietokone odottaa PIN-koodia.")
    print(tietokone.kuvaus)
    koodi = input("Syötä 6-numeroinen PIN-koodi (x = poistu): ")

    if koodi.lower() == "x":
        return
    if koodi == tietokone.pin:
        print("\nOikea PIN-koodi!")
        print("Tietokone avautuu.")

        # Merkitään pelaajan tietoihin, että PIN-koodi on ratkaistu.
        pelaaja.pin_ratkaistu = True

        print("\n--- SALAINEN VIESTI ---")
        print("Albertin tietokoneelta löytyy viimeinen merkintä:")
        print("Joku on osoittanut huomattavaa kiinnostusta tutkimukseeni.")
        print("Hänellä on ollut mahdollisuus nähdä työni")
        print("ja päästä käsiksi työhuoneeseen.")
        print("Jos minulle tapahtuu jotain, näitä tietoja kannattaa tutkia tarkemmin.")

        pelaaja.lisaa_vihje("Epäillyllä oli tietoa tutkimuksesta ja pääsy työhuoneeseen.")

    else:
        print("\nVäärä PIN-koodi.")
        print("Et onnistunut ratkaisemaan mysteeriä.")
        print("Peli alkaa alusta.")
        # False kertoo paavalikko.py:lle, että peli pitää aloittaa alusta.
        return False
    
# ==================================================
# MURHAAJAN RATKAISEMINEN
# ==================================================
# Käynnistää murhaajan ratkaisemisen.
def ratkaise_murhaaja(pelaaja):
    print("\n--- RATKAISE MURHAAJA ---")
    print("\nVAROITUS!")
    print("Kun valitset epäillyn, annat lopullisen syytöksen.")
    print("Jos arvaat väärin, peli alkaa alusta.")
    print("Varmista siis, että olet tutkinut vihjeet tarkasti.\n")

    print("Kuka murhasi Albert Kiven?")

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
            # False kertoo paavalikko.py:lle, että peli pitää aloittaa alusta.
            return False

        elif valinta == "2":
            print("\nSyytät James Kiveä.")
            print("\nVäärä syytös!")
            print("James oli kirjastossa noin kello 22.10.")
            print("Hän ei käynyt Albertin työhuoneessa.")
            print("Sinulla ei ole tarpeeksi todisteita yhdistää Jamesia murhaan.")
            print("Peli alkaa alusta.")
            return False

        elif valinta == "3":
            print("\nSyytät Viktor Salosta.")
            print("\nVäärä syytös!")
            print("Viktorilla oli motiivi ja hän kävi työhuoneessa.")
            print("Hän kuitenkin poistui työhuoneesta jo kello 22.20.")
            print("Sähkökatko alkoi vasta kello 22.21.")
            print("Viktor ei siis voinut olla työhuoneessa murhan aikana.")
            print("Peli alkaa alusta.")
            return False

        elif valinta == "4":
            print("Sofia Niemi oli murhaaja.")
            print("\nSofialla oli pääsy työhuoneeseen avainkortillaan.")
            print("\nHänen kertomuksensa teestä ei pitänyt paikkaansa.")
            print("Sähkökatkon aikana hänellä oli mahdollisuus päästä työhuoneeseen")
            print("ja varastaa USB-muistitikku.")
            print("\nONNEKSI OLKOON!")
            print("Ratkaisit Albert Kiven murhan.")

            # Oikean ratkaisun jälkeen pelaaja voi aloittaa uuden pelin tai lopettaa.
            while True:
                print("\nHaluatko pelata uudestaan?")
                print("1. Pelaa uudestaan")
                print("2. Lopeta peli")
                valinta = input("Valitse: ")

                if valinta == "1":
                    # False kertoo paavalikko.py:lle, että peli pitää aloittaa alusta.
                    return False

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