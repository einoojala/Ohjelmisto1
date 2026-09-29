from peli import Pelaaja
from peli.huoneet import tyohuone, kirjasto, keittio, olohuone, ruokasali
from peli.esineet import tutkimuspaperi, avainkortti, usb_kotelo, kuppi, paivakirja, muistilappu
from peli.epaillyt import epaillyt

# --------------------------------------------------
# PELIN TALLENNUS
# --------------------------------------------------
# Tallennetaan pelaajan tämänhetkinen pelitilanne save.txt-tiedostoon.
def tallenna_peli(pelaaja):
    # Avataan tai luodaan tallennustiedosto kirjoittamista varten. 
    # encoding="utf-8" varmistaa, että suomalaiset merkit tallentuvat oikein.
    with open("data/save.txt", "w", encoding="utf-8") as tiedosto:
        # Tallennetaan pelaajan nimi ja ikä.
        tiedosto.write(f"nimi:{pelaaja.nimi}\n")
        tiedosto.write(f"ika:{pelaaja.ika}\n")

        # Tarkistetaan pelaajan sijainti ja tallennetaan se.
        if pelaaja.sijainti is not None:
            tiedosto.write(f"sijainti:{pelaaja.sijainti.nimi}\n")
        else:
            # Jos pelaaja ei ole vielä ollut missään huoneessa, tallennetaan tyhjä arvo.
            tiedosto.write("sijainti:\n")

        # Tallennetaan inventaarion esineiden nimet.
        esineet = []

        # Käydään pelaajan inventaarion esineet läpi.
        for esine in pelaaja.inventaario:
            esineet.append(esine.nimi)

        # Yhdistetään esineiden nimet yhdeksi merkkijonoksi.
        tiedosto.write(f"inventaario:{','.join(esineet)}\n")

        # Tallennetaan pelaajan löytämät vihjeet.
        tiedosto.write("vihjeet:\n")

        # Jokainen vihje tallennetaan omalle riville ranskalaisella viivalla.
        for vihje in pelaaja.vihjeet:
            tiedosto.write(f"- {vihje}\n")

        # Tallennetaan tieto siitä, onko PIN-koodi ratkaistu.
        tiedosto.write(f"pin_ratkaistu:{pelaaja.pin_ratkaistu}\n")

        # Tallennetaan tieto tutkituista huoneista
        tiedosto.write(f"tutkitut_huoneet:{','.join(huone.nimi for huone in pelaaja.tutkitut_huoneet)}\n")

        # Tallennetaan tieto tutkituista epäillyistä
        tiedosto.write(f"tutkitut_epaillyt:{','.join(epailty.nimi for epailty in pelaaja.tutkitut_epaillyt)}\n")

    # Ilmoitetaan pelaajalle, että tallennus onnistui.
    print("\nPeli tallennettu!")

# --------------------------------------------------
# PELIN LATAAMINEN
# --------------------------------------------------
# Ladataan aikaisemmin tallennettu peli.
def lataa_peli():
    # Avataan tallennustiedosto lukemista varten.
    # encoding="utf-8" varmistaa, että suomalaiset merkit luetaan oikein.
    with open("data/save.txt", "r", encoding="utf-8") as tiedosto:
        # Luetaan tallennustiedoston rivit listaksi.
        rivit = tiedosto.readlines()

    # Luodaan sanakirja tallennustiedoston tietoja varten.
    tiedot = {}
    # Aloitetaan tallennustiedoston rivien käsittely ensimmäisestä rivistä.
    i = 0

    while i < len(rivit):
        rivi = rivit[i].strip()
        # Ohitetaan tyhjät rivit.
        if not rivi:
            i += 1
            continue

        # Tarkistetaan, alkaako tässä kohtaa tallennustiedoston vihjelista.
        if rivi == "vihjeet:":
            vihjeet = []
            i += 1

            # Luetaan vihjelistan kaikki rivit, jotka alkavat "- "-merkeillä.
            while i < len(rivit):
                vihjerivi = rivit[i].strip()

                # Poistetaan rivin alusta "- " ennen vihjeen tallentamista.
                if vihjerivi.startswith("- "):
                    vihje = vihjerivi[2:]
                    vihjeet.append(vihje)
                    i += 1
                else:
                    # Vihjelista päättyy, kun seuraava rivi ei ala "- "-merkeillä.
                    break

            # Tallennetaan vihjelista tiedot-sanakirjaan.
            tiedot["vihjeet"] = vihjeet
            # Jatketaan seuraavan tiedon käsittelyyn.
            continue

        # Muut tallennustiedot käsitellään normaalisti.
        avain, arvo = rivi.split(":", 1)
        tiedot[avain] = arvo
        i += 1

    # Luodaan uusi Pelaaja-olio tallennettujen tietojen perusteella.
    pelaaja = Pelaaja(tiedot["nimi"], int(tiedot["ika"]))

    # Yhdistetään tallennettu huoneen nimi oikeaan Huone-olioon.
    huoneet = {
        "Työhuone": tyohuone,
        "Kirjasto": kirjasto,
        "Keittiö": keittio,
        "Olohuone": olohuone,
        "Ruokasali": ruokasali}

    # Tarkistetaan, löytyykö tallennettu sijainti huoneiden sanakirjasta.
    if tiedot["sijainti"] in huoneet:
        pelaaja.sijainti = huoneet[tiedot["sijainti"]]

    # Yhdistetään tallennetut esineiden nimet oikeisiin Esine-olioihin.
    kaikki_esineet = {
        "Tutkimuspaperi": tutkimuspaperi,
        "Yrityksen avainkortti": avainkortti,
        "USB-kotelo": usb_kotelo,
        "Teekuppi": kuppi,
        "Päiväkirja": paivakirja,
        "Muistilappu": muistilappu}

    # Jos inventaariossa on tallennettuja esineitä, palautetaan ne inventaarioon.
    if tiedot["inventaario"]:
        # Jaetaan tallennetut esineiden nimet listaksi.
        esineiden_nimet = tiedot["inventaario"].split(",")

        # Käydään kaikki tallennetut esineet läpi.
        for nimi in esineiden_nimet:
            # Tarkistetaan, löytyykö nimi kaikki_esineet-sanakirjasta.
            if nimi in kaikki_esineet:
                # Lisätään oikea Esine-olio pelaajan inventaarioon.
                pelaaja.inventaario.append(kaikki_esineet[nimi])

    # Palautetaan pelaajan löytämät vihjeet.
    if tiedot["vihjeet"]:
        pelaaja.vihjeet = tiedot["vihjeet"]
    
    # Vertailulla muutetaan "True" oikeaksi boolean-arvoksi True.
    # Jos arvo on jotain muuta, tulokseksi tulee False.
    pelaaja.pin_ratkaistu = tiedot["pin_ratkaistu"] == "True"

    # Palautetaan pelaajan tutkimat huoneet.
    if tiedot["tutkitut_huoneet"]:
        huoneiden_nimet = tiedot["tutkitut_huoneet"].split(",")

        for nimi in huoneiden_nimet:
            if nimi in huoneet:
                pelaaja.tutkitut_huoneet.append(huoneet[nimi])

    # Luodaan sanakirja epäiltyjen nimistä epäilty-olioihin.
    kaikki_epaillyt = {epailty.nimi: epailty for epailty in epaillyt}

    # Palautetaan pelaajan tutkimat epäillyt.
    if tiedot["tutkitut_epaillyt"]:
        epailtyjen_nimet = tiedot["tutkitut_epaillyt"].split(",")

        for nimi in epailtyjen_nimet:
            if nimi in kaikki_epaillyt:
                pelaaja.tutkitut_epaillyt.append(kaikki_epaillyt[nimi])

    # Poistetaan pelaajan inventaariossa olevat esineet huoneista.
    for huone in huoneet.values():

        # Kopioidaan lista, jotta alkuperäistä listaa voidaan muuttaa.
        for esine in huone.esineet[:]:
            # Jos esine on pelaajan inventaariossa, poistetaan se huoneesta.
            if esine in pelaaja.inventaario:
                huone.esineet.remove(esine)

    print("\nTallennettu peli ladattu!")
    # Palautetaan valmis Pelaaja-olio main.py:lle.
    return pelaaja