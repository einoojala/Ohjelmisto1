# Tuodaan epäiltyjen lista, jotta pelaaja voi tutkia epäiltyjä.
from peli.epaillyt import epaillyt
# Tuodaan lukittu tietokone, jonka PIN-koodi täytyy ratkaista.
from peli.esineet import tietokone
# Tuodaan kaikki pelin huoneet, jotta niiden välillä voi liikkua niiden.
from peli.huoneet import tyohuone, kirjasto, keittio, olohuone, ruokasali
# Tuodaan pelin tallennusfunktio.
from peli.tallennus import tallenna_peli

# --------------------------------------------------
# HUONEIDEN TUTKIMINEN
# --------------------------------------------------
# Funktio antaa pelaajalle mahdollisuuden valita huoneen, jota hän haluaa tutkia.
def tutki_huonetta(pelaaja):
    # While True:lla valikkop pysyy auki niin kauan, että kun valitaan huone tai palaa takaisin.
    while True:
        print("\n--- HUONEET ---")
        print("1. Työhuone")
        print("2. Kirjasto")
        print("3. Keittiö")
        print("4. Olohuone")
        print("5. Ruokasali")
        print("6. Takaisin")
        
        valinta = input("Mihin huoneeseen haluat mennä? (numero) ")
        if valinta == "1":
            # Seurvaaissa kohdissa tallennetaan pelaajan nykyinen sijainti huoneen mukaan.
            # Tulostetaan huoneen nimi ja kuvaus ja kysytään halutaanko tutkia tarkemmin
            pelaaja.sijainti = tyohuone
            print(tyohuone)
            tyohuone.tutki_tarkemmin(pelaaja)

        elif valinta == "2":
            pelaaja.sijainti = kirjasto
            print(kirjasto)
            kirjasto.tutki_tarkemmin(pelaaja)

        elif valinta == "3":
            pelaaja.sijainti = keittio
            print(keittio)
            keittio.tutki_tarkemmin(pelaaja)

        elif valinta == "4":
            pelaaja.sijainti = olohuone
            print(olohuone)
            olohuone.tutki_tarkemmin(pelaaja)

        elif valinta == "5":
            pelaaja.sijainti = ruokasali
            print(ruokasali)
            ruokasali.tutki_tarkemmin(pelaaja)

        elif valinta == "6":
            # Poistutaan huonevalikosta ja palataan päävalikkoon.
            return

        else:
            # Jos pelaaja antaa muun kuin vaihtoehdon, kysytään valinta uudelleen.
            print("Tuntematon valinta. Valitse numero 1-6.")

# --------------------------------------------------
# ESINEIDEN KERÄÄMINEN
# --------------------------------------------------

# Funktio antaa pelaajalle mahdollisuuden ottaa esineitä ja lisätä ne omaan inventaarioonsa.
def lisaa_esine(pelaaja):
    # Pelaajan täytyy olla jossain huoneessa ennen kuin hän voi yrittää kerätä esineitä.
    if pelaaja.sijainti is None:
        print("\nEt ole vielä missään huoneessa.")
        print("Mene ensin huoneeseen.")
        return
    
    # Haetaan pelaajan nykyisen huoneen esinelista.
    esineet = pelaaja.sijainti.esineet
    # Jos huoneessa ei ole esineitä, ei ole mitään kerättävää.
    if len(esineet) == 0:
        print("\nTässä huoneessa ei ole kerättäviä esineitä.")
        return

    print("\n--- ESINEET ---")
    # Tulostetaan huoneen esineet numeroituna, enumerate aloittaa numeroinnin ykkösestä.
    for numero, esine in enumerate(esineet, 1):
        print(f"{numero}. {esine.nimi}")
    print("x. Takaisin")

    # While True:lla kysytään uudelleen, jos pelaaja antaa virheellisen arvon.
    while True:
        valinta = input("Minkä esineen haluat ottaa (esineen numero)? ")
        # x-valinnalla palataan takaisin ilman esineen ottamista.
        if valinta.lower() == "x":
            return

        # Tarkistetaan, että syöte on numero, continue aloittaa silmukan uudelleen.
        if not valinta.isdigit():
            print("Anna numero.")
            continue

        # Muutetaan merkkijono kokonaisluvuksi # Tarkistetaan, että annettu numero vastaa huoneen esinettä.
        numero = int(valinta)
        if 1 <= numero <= len(esineet):
            # Listan indeksi alkaa nollasta, joten käyttäjän antamasta numerosta vähennetään yksi.
            esine = esineet[numero - 1]
            # Lisätään valittu esine pelaajan inventaarioon.
            pelaaja.lisaa_esine(esine)
            # Poistetaan esine huoneesta, koska se otettiin mukaan.
            esineet.remove(esine)
            break
        else:
            print("Tuntematon valinta.")

# --------------------------------------------------
# EPÄILTYJEN TUTKIMINEN
# --------------------------------------------------
# Funktio näyttää kaikki epäillyt ja antaa pelaajan tutkia heidän tietojaan yksi kerrallaan.
def nayta_epaillyt(pelaaja):
    # While True:lla valikko pysyy auki, jotta pelaaja voi tutkia useampaa epäiltyä saman toiminnon aikana.
    while True:
        print("\n--- EPÄILLYT ---")
        # Tulostetaan kaikki epäillyt numeroituna, enumerate aloittaa numeroinnin ykkösestä.
        for numero, epailty in enumerate(epaillyt, 1):
            print(f"{numero}. {epailty.nimi}")
        print("x. Takaisin")

        # Kysytään pelaajalta, ketä hän haluaa tutkia.
        valinta = input("Ketä haluat tutkia? ")
        # x-valinnalla palataan päävalikkoon.
        if valinta.lower() == "x":
            return

        # Tarkistetaan, että valinta on numero.
        if not valinta.isdigit():
            print("Anna numero.")
            continue

        # Muutetaan merkkijono kokonaisluvuksi, ja tarkistetaan, että numero vastaa jotain epäiltyä.
        numero = int(valinta)
        if 1 <= numero <= len(epaillyt):
            # Haetaan valittu epäilty listasta.
            # Pelaajan numerointi alkaa ykkösestä, mutta listan indeksi nollasta.
            epailty = epaillyt[numero - 1]
            # Tulostetaan valitun epäillyn tiedot.
            print("\n--- EPÄILTY ---")
            print(epailty)
        else:
            print("Tuntematon valinta.")

# --------------------------------------------------
# VIHJEIDEN TUTKIMINEN
# --------------------------------------------------
# Funktio näyttää kaikki vihjeet, jotka pelaaja on tähän mennessä löytänyt.
def tutki_vihjeita(pelaaja):
    pelaaja.nayta_vihjeet()

# --------------------------------------------------
# PIN-KOODIN RATKAISEMINEN
# --------------------------------------------------
# Funktio käynnistää tietokoneen PIN-koodin ratkaisemisen.
def ratkaise_pin_koodi(pelaaja):
    print("\n--- RATKAISE MYSTEERI ---")

    # Jos pelaaja on jo ratkaissut PIN-koodin, samaa tehtävää ei tarvitse ratkaista uudelleen.
    if pelaaja.pin_ratkaistu:
        print("Olet jo avannut tietokoneen.")
        return
    print("Edvardin tietokone odottaa PIN-koodia.")
    # Kutsutaan tietokoneen avaamismetodia, joka tarkistaa pelaajan antaman PIN-koodin.
    tulos = tietokone.avaaminen(pelaaja)

    # False tarkoittaa, että pelaaja antoi väärän PIN-koodin.
    # False palautetaan main.py:lle, jotta peli voidaan aloittaa alusta.
    if tulos == False:
        return False
    
# --------------------------------------------------
# MURHAAJAN RATKAISEMINEN
# --------------------------------------------------
# Funktio antaa pelaajalle mahdollisuuden tehdä lopullisen arvauksen murhasta.
def ratkaise_murhaaja(pelaaja):
    print("\n--- RATKAISE MURHAAJA ---")
    print("\nVAROITUS!")
    print("Kun valitset epäillyn, annat lopullisen syytöksen.")
    print("Jos arvaat väärin, peli alkaa alusta.")
    print("Varmista siis, että olet tutkinut vihjeet tarkasti.\n")

    print("Kuka murhasi Edvard Kiven?")
    print("1. Elisa Kivi")
    print("2. James Kivi")
    print("3. Viktor Salonen")
    print("4. Sofia Niemi")
    print("5. Takaisin")

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

        # Oikean ratkaisun jälkeen pelaaja voi joko aloittaa uuden pelin tai lopettaa kokonaan.
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

    # Pelaaja haluaa palata päävalikkoon.
    elif valinta == "5":
        print("\nPalaat päävalikkoon.")
        return None

    # Jos pelaaja antaa muun kuin sallitun vaihtoehdon, palataan takaisin päävalikkoon.
    else:
        print("\nTuntematon valinta.")
        print("Murhaajaa ei ole vielä syytetty.")
        return None

# --------------------------------------------------
# OHJEET
# --------------------------------------------------
# Funktio lukee ohjetekstin erillisestä tekstitiedostosta ja näyttää sen pelaajalle.
def nayta_ohjeet(pelaaja):
    with open("data/tarina_ohjeet.txt", "r") as tiedosto:
        print(tiedosto.read())

# --------------------------------------------------
# PÄÄVALIKKO
# --------------------------------------------------
# Päävalikko toimii pelin keskeisenä ohjauspaikkana, ja sitä kautta. alitaan toiminnot.
def paavalikko(pelaaja):
    # Päävalikko pysyy näkyvissä koko pelin ajan while True:lla, kunnes Valitaan lopeta tai peli päättyy.
    while True:
        print("\n================================")
        print("          PÄÄVALIKKO")
        print("================================")
        print("1. Tutki huoneita")
        print("2. Kerää esineitä")
        print("3. Katso inventaariota")
        print("4. Tutki epäiltyjä")
        print("5. Tutki vihjeitä")
        print("6. Ratkaise PIN-koodi")
        print("7. Ratkaise murhaaja")
        print("8. Ohjeet")
        print("9. Tallenna peli")
        print("10. Lopeta")
        print("================================")

        # Kysytään pelaajalta, mitä toimintoa hän haluaa käyttää.
        komento = input("Valitse toiminnon numero: ")

        # Huoneiden tutkiminen.
        if komento == "1":
            tutki_huonetta(pelaaja)
        # Esineiden kerääminen.
        elif komento == "2":
            lisaa_esine(pelaaja)
        # Pelaajan inventaarion tarkasteleminen.
        elif komento == "3":
            pelaaja.nayta_inventaario()
        # Epäiltyjen tutkiminen.
        elif komento == "4":
            nayta_epaillyt(pelaaja)
        # Pelaajan löytämien vihjeiden tarkasteleminen.
        elif komento == "5":
            tutki_vihjeita(pelaaja)
        # PIN-koodin ratkaiseminen.
        elif komento == "6":
            tulos = ratkaise_pin_koodi(pelaaja)
            # Jos PIN-koodin ratkaisu epäonnistui, palautetaan False main.py:lle ja peli alkaa alusta.
            if tulos == False:
                return False

        # Murhaajan ratkaiseminen.
        elif komento == "7":
            # Murhaajaa saa yrittää ratkaista vasta, kun PIN-koodi on ratkaistu.
            if pelaaja.pin_ratkaistu:
                tulos = ratkaise_murhaaja(pelaaja)
                # False tarkoittaa, että peli aloitetaan uudelleen.
                if tulos == False:
                    return False
                # True tarkoittaa, että pelaaja voitti ja haluaa lopettaa pelin.
                elif tulos == True:
                    return True
            else:
                print("\nEt voi vielä ratkaista murhaajaa.")
                print("Avaa ensin Edvardin tietokone.")

        # Ohjeiden näyttäminen.
        elif komento == "8":
            nayta_ohjeet(pelaaja)
        # Pelin tallentaminen.
        elif komento == "9":
            tallenna_peli(pelaaja)
        # Pelin lopettaminen.
        elif komento == "10" or komento.lower() == "lopeta":
            print("\nPeli lopetetaan.")
            print(f"Kiitos pelaamisesta, {pelaaja.nimi}!")
            break
        # Kaikki muut syötteet ovat virheellisiä.
        else:
            print("\nTuntematon komento.")
            print("Valitse jokin valikon vaihtoehdoista.")