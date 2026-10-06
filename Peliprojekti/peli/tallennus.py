import json
from peli import Pelaaja
from peli.epaillyt import epaillyt
from peli.huoneet import huoneet
from peli.esineet import esineet

# =================================================
# PELIN TALLENNUS
# =================================================
def tallenna_peli(pelaaja):
    # Muodostetaan sanakirja pelaajan tallennettavista tiedoista.
    tiedot = {
        "nimi": pelaaja.nimi,
        "ika": pelaaja.ika,
        "sijainti": pelaaja.sijainti.nimi if pelaaja.sijainti else "",
        "inventaario": [esine.nimi for esine in pelaaja.inventaario],
        "vihjeet": pelaaja.vihjeet,
        "pin_ratkaistu": pelaaja.pin_ratkaistu,
        "tutkitut_huoneet": [huone.nimi for huone in pelaaja.tutkitut_huoneet],
        "tutkitut_epaillyt": [epailty.nimi for epailty in pelaaja.tutkitut_epaillyt]}

    # Avataan tai luodaan JSON-tiedosto kirjoittamista varten.
    # encoding="utf-8" mahdollistaa suomalaisten merkkien, kuten ä:n ja ö:n, tallentamisen oikein.
    # ensure_ascii=False pitää nämä merkit JSON-tiedostossa normaalisti näkyvissä.
    # indent=4 sisentää JSON-tiedoston rakenteen neljällä välilyönnillä, jotta se on helpompi lukea.
    with open("data/save.json", "w", encoding="utf-8") as tiedosto:
        json.dump(tiedot, tiedosto, ensure_ascii=False, indent=4)
    print("\nPeli tallennettu!")

# =================================================
# PELIN LATAAMINEN
# =================================================
def lataa_peli():
    with open("data/save.json", "r", encoding="utf-8") as tiedosto:
        tiedot = json.load(tiedosto)

    pelaaja = Pelaaja(tiedot["nimi"], tiedot["ika"])

    # Käytetään sanakirjakoostetta.
    # Tehdään huoneista sanakirja, jotta tallennuksessa oleva huoneen nimi voidaan yhdistää oikeaan huoneolioon.
    kaikki_huoneet = {huone.nimi: huone for huone in huoneet}
    # Tehdään esineistä sanakirja, jotta tallennuksessa oleva esineen nimi voidaan yhdistää oikeaan esineolioon.
    kaikki_esineet = {esine.nimi: esine for esine in esineet}
    # Tehdään epäillyistä sanakirja, jotta tallennuksessa oleva epäillyn nimi voidaan yhdistää oikeaan epäiltyolioon.
    kaikki_epaillyt = {epailty.nimi: epailty for epailty in epaillyt}

    # Palautetaan pelaajan sijainti tallennuksen perusteella.
    if tiedot["sijainti"] in kaikki_huoneet:
        pelaaja.sijainti = kaikki_huoneet[tiedot["sijainti"]]

    # Palautetaan pelaajan inventaario.
    for nimi in tiedot["inventaario"]:
        if nimi in kaikki_esineet:
            pelaaja.inventaario.append(kaikki_esineet[nimi])

    # Palautetaan pelaajan löytämät vihjeet.
    pelaaja.vihjeet = tiedot["vihjeet"]

    # Palautetaan PIN-koodin ratkaisemisen tila.
    pelaaja.pin_ratkaistu = tiedot["pin_ratkaistu"]

    # Palautetaan tutkitut huoneet.
    for nimi in tiedot["tutkitut_huoneet"]:
        if nimi in kaikki_huoneet:
            pelaaja.tutkitut_huoneet.append(kaikki_huoneet[nimi])

    # Palautetaan tutkitut epäillyt.
    for nimi in tiedot["tutkitut_epaillyt"]:
        if nimi in kaikki_epaillyt:
            pelaaja.tutkitut_epaillyt.append(kaikki_epaillyt[nimi])

    # Poistetaan inventaarioon kerätyt esineet niiden huoneista.
    for huone in huoneet:
        # Käydään listan kopio läpi, jotta esineitä voidaan poistaa alkuperäisestä listasta.
        for esine in huone.esineet[:]:
            if esine in pelaaja.inventaario:
                huone.esineet.remove(esine)

    print("\nTallennettu peli ladattu!")
    return pelaaja