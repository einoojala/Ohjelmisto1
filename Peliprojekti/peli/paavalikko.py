from peli.epaillyt import epaillyt
from peli.huoneet import huoneet
from peli.tallennus import tallenna_peli
from peli.mysteerit import ratkaise_murhaaja, ratkaise_pin_koodi

# ==================================================
# HUONEIDEN TUTKIMINEN
# ==================================================
# Funktio antaa pelaajalle mahdollisuuden valita tutkittavan huoneen.
# Otsikkoa voidaan vaihtaa, kun huoneeseen siirrytään esinevalikosta.
def tutki_huonetta(pelaaja, otsikko="TUTKI HUONEITA"):
    while True:
        print(f"\n--- {otsikko} ---")
        # enumerate antaa huoneille numerot 1 alkaen.
        for numero, huone in enumerate(huoneet, 1):
            print(f"{numero}. {huone.nimi}")
        print("x. Takaisin")

        valinta = input("Valitse huone: ")

        if valinta.lower() == "x":
            return

        if not valinta.isdigit():
            print("Anna numero.")
            continue
        
        numero = int(valinta)
        # Tarkistetaan, että valittu numero vastaa olemassa olevaa huonetta.
        if 1 <= numero <= len(huoneet):
            # Listan indeksit alkavat nollasta, joten käyttäjän numerosta vähennetään yksi.
            huone = huoneet[numero - 1]
            # Tallennetaan pelaajan nykyiseksi sijainniksi valittu huone.
            pelaaja.sijainti = huone
            print(huone)
            huone.tutki_tarkemmin(pelaaja)

        else:
            print("Anna luku väliltä 1-5.")


# ==================================================
# ESINEIDEN KERÄÄMINEN
# ==================================================
# Funktio antaa pelaajalle mahdollisuuden ottaa esineitä ja lisätä ne inventaarioon.
def lisaa_esine(pelaaja):
    # Pelaajan täytyy olla jossain huoneessa ennen kuin hän voi kerätä esineitä.
    if pelaaja.sijainti is None:
        print("\nEt ole vielä missään huoneessa.")
        print("Mene ensin huoneeseen.")
        return

    while True:
        print(f"\n--- ESINEET: {pelaaja.sijainti.nimi.upper()} ---")

        # Haetaan pelaajan nykyisen huoneen esinelista.
        esineet = pelaaja.sijainti.esineet

        if not esineet:
            print("\nTässä huoneessa ei ole kerättäviä esineitä.")

        else:
            # enumerate antaa esineille numerot 1 alkaen.
            for numero, esine in enumerate(esineet, 1):
                print(f"{numero}. {esine.nimi}")

        # Huoneen voi vaihtaa aina, vaikka siellä ei olisi enää esineitä.
        print("v. Vaihda huonetta")
        print("x. Takaisin")

        valinta = input("Valitse: ")

        # x-valinnalla palataan takaisin ilman esineen ottamista.
        if valinta.lower() == "x":
            return

        # v-valinnalla avataan huonevalikko.
        if valinta.lower() == "v":
            tutki_huonetta(pelaaja, "VAIHDA HUONETTA")
            continue

        # Jos huoneessa ei ole esineitä, muita valintoja ei voi tehdä.
        if not esineet:
            print("\nValitse v vaihtaaksesi huonetta tai x palataksesi.")
            continue

        if not valinta.isdigit():
            print("Anna numero.")
            continue

        numero = int(valinta)

        # Tarkistetaan, että valittu numero vastaa olemassa olevaa esinettä.
        if 1 <= numero <= len(esineet):
            # Listan indeksit alkavat nollasta, joten käyttäjän numerosta vähennetään yksi.
            esine = esineet[numero - 1]
            pelaaja.lisaa_esine(esine)
            # Poistetaan esine huoneesta, koska pelaaja otti sen mukaan.
            esineet.remove(esine)

        else:
            print("Tuntematon valinta.")

# ==================================================
# EPÄILTYJEN TUTKIMINEN
# ==================================================
# Funktio näyttää kaikki epäillyt ja antaa pelaajan tutkia heidän tietojaan.
def nayta_epaillyt(pelaaja):
    while True:
        print("\n--- EPÄILLYT ---")
        # enumerate antaa epäillyille numerot 1 alkaen.
        for numero, epailty in enumerate(epaillyt, 1):
            print(f"{numero}. {epailty.nimi}")
        print("x. Takaisin")

        valinta = input("Ketä haluat tutkia? ")
        # x-valinnalla palataan päävalikkoon.
        if valinta.lower() == "x":
            return

        # Tarkistetaan, että valinta on numero.
        if not valinta.isdigit():
            print("Anna numero.")
            continue

        numero = int(valinta)
        # Tarkistetaan, että valittu numero vastaa olemassa olevaa epäiltyä.
        if 1 <= numero <= len(epaillyt):
            # Listan indeksit alkavat nollasta, joten käyttäjän numerosta vähennetään yksi.
            epailty = epaillyt[numero - 1]

            if epailty not in pelaaja.tutkitut_epaillyt:
                pelaaja.tutkitut_epaillyt.append(epailty)
            print("\n--- EPÄILTY ---")
            print(epailty)
            
        else:
            print("Anna luku väliltä 1-4.")

# ==================================================
# OHJEET
# ==================================================
# Näyttää pelin tarinan ja ohjeet.
def nayta_ohjeet():
    # Avataan tiedosto lukemista varten.
    with open("data/tarina_ohjeet.txt", "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()

    # Jaetaan teksti kappaleisiin tyhjien rivien (\n\n) kohdalta.
    kappaleet = teksti.split("\n\n")

    # Pelaaja painaa Enteriä ennen ohjeiden alkamista.
    input("\nLue ohjeet painamalla enteriä: ")

    # Tulostetaan kappaleet yksi kerrallaan.
    for kappale in kappaleet:
        print(kappale)
        input()

# ==================================================
# TAPAHTUMA-AJAT
# ==================================================
def nayta_tapahtumat():
    print("\n--- TAPAHTUMAT ---")
    print("21:50 - Elisa ja Albert riitelivät kahdestaan.")
    print("21:55 - Viktor ja Albert keskustelivat kiivaasti työhuoneessa.")
    print("22:10 - James nähtiin kirjastossa.")
    print("22:18 - Sofia nähtiin keittiössä.")
    print("22:19 - James palasi ruokasaliin.")
    print("22:19 - Elisa palasi ruokasaliin.")
    print("22:20 - Viktor poistui työhuoneesta.")
    print("22:21-22:25 - Kartanossa oli täysin pimeää.")
    print("22:25 - Albert löydettiin kuolleena.")   

# ==================================================
# PÄÄVALIKKO
# ==================================================
def paavalikko(pelaaja):
    # Päävalikko pysyy auki, kunnes pelaaja lopettaa pelin tai peli päättyy.
    while True:
        print("\n================================")
        print("          PÄÄVALIKKO")
        print("================================")
        print("1. Tutki huoneita")
        print("2. Kerää esineitä")
        print("3. Katso inventaariota")
        print("4. Tutki epäiltyjä")
        print("5. Tutki vihjeitä")
        print("6. Tutki tapahtuma-aikoja")
        print("7. Ratkaise PIN-koodi")
        print("8. Ratkaise murhaaja")
        print("9. Tutkinnan tilanne")
        print("10. Ohjeet")
        print("11. Tallenna peli")
        print("12. Lopeta")
        print("================================")

        komento = input("Valitse toiminnon numero: ")

        if komento == "1":
            tutki_huonetta(pelaaja)
        elif komento == "2":
            lisaa_esine(pelaaja)
        elif komento == "3":
            pelaaja.nayta_inventaario()
        elif komento == "4":
            nayta_epaillyt(pelaaja)
        elif komento == "5":
            pelaaja.nayta_vihjeet()
        elif komento == "6":
            nayta_tapahtumat()
        elif komento == "7":
            # Jos PIN-koodin ratkaisu epäonnistuu, aloitetaan peli alusta.
            tulos = ratkaise_pin_koodi(pelaaja)

            if tulos is False:
                return False
            
        elif komento == "8":
            # Murhaajaa saa yrittää ratkaista vasta, kun PIN-koodi on ratkaistu.
            if pelaaja.pin_ratkaistu:
                tulos = ratkaise_murhaaja(pelaaja)

                if tulos is False:
                    # False palautetaan main.py:lle, jolloin peli aloitetaan alusta.
                    return False
                
                elif tulos is True:
                    # True palautetaan main.py:lle, jolloin peli voidaan lopettaa.
                    return True
            else:
                print("\nEt voi vielä ratkaista murhaajaa.")
                print("Avaa ensin Albertin tietokone.")

        elif komento == "9":
            pelaaja.nayta_tutkinnan_tilanne()
        elif komento == "10":
            nayta_ohjeet()
        elif komento == "11":
            tallenna_peli(pelaaja)
        elif komento == "12":
            print("\nPeli lopetetaan.")
            print(f"Kiitos pelaamisesta, {pelaaja.nimi}!")
            break
        else:
            print("\nTuntematon komento.")
            print("Valitse jokin valikon vaihtoehdoista.")