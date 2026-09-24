# Tuodaan Pelaaja-luokka, jotta tallennuksesta voidaan luoda uusi pelaaja.
from peli import Pelaaja
# Tuodaan kaikki huoneet, jotta tallennettu sijainti voidaan yhdistää oikeaan Huone-olioon.
from peli.huoneet import tyohuone, kirjasto, keittio, olohuone, ruokasali
# Tuodaan kaikki esineet, jotta tallennettu esineen nimi voidaan yhdistää oikeaan Esine-olioon.
from peli.esineet import tutkimuspaperi, avainkortti, usb_kotelo, kuppi, muistilappu

# Tallennetaan pelaajan tämänhetkinen pelitilanne save.txt-tiedostoon.
def tallenna_peli(pelaaja):
    # Avataan/ luodaan tallennustiedosto kirjoittamista varten.
    with open("data/save.txt", "w") as tiedosto:
        # Tallennetaan pelaajan nimi ja ikä omille riveilleen.
        tiedosto.write(f"nimi:{pelaaja.nimi}\n")
        tiedosto.write(f"ika:{pelaaja.ika}\n")

        # Tarkistetaan, että pelaajalla on jokin sijainti ja tallennetaan se
        if pelaaja.sijainti is not None:
            tiedosto.write(f"sijainti:{pelaaja.sijainti.nimi}\n")
        else:
            # Jos pelaaja ei ole vielä ollut missään huoneessa, tallennetaan tyhjä arvo.
            tiedosto.write("sijainti:\n")

        # Inventaario sisältää Esine-olioita, mutta tiedostoon tallennetaan vain esineiden nimet.
        esineet = []
        # Käydään pelaajan inventaarion kaikki esineet läpi.
        for esine in pelaaja.inventaario:
            # Lisätään esineen nimi väliaikaiseen listaan.
            esineet.append(esine.nimi)

        # join() yhdistää listan nimet yhdeksi merkkijonoksi.
        # Esimerkiksi: ["Tutkimuspaperi", "Teekuppi"] muuttuu muotoon: "Tutkimuspaperi,Teekuppi"
        tiedosto.write(f"inventaario:{','.join(esineet)}\n")

        # Tallennetaan kaikki pelaajan löytämät vihjeet. Vihjeet erotetaan toisistaan |-merkillä.
        tiedosto.write(f"vihjeet:{'|'.join(pelaaja.vihjeet)}\n")

        # Tallennetaan tieto siitä, onko PIN-koodi ratkaistu. Arvo tallentuu tekstinä True tai False.
        tiedosto.write(f"pin_ratkaistu:{pelaaja.pin_ratkaistu}\n")
    # Ilmoitetaan pelaajalle, että tallennus onnistui.
    print("\nPeli tallennettu!")

# Ladataan aikaisemmin tallennettu peli.
def lataa_peli():
    # Avataan tallennustiedosto lukemista varten.
    with open("data/save.txt", "r") as tiedosto:
        # Luetaan kaikki tallennustiedoston rivit listaksi.
        rivit = tiedosto.readlines()

    # Luodaan tyhjä sanakirja, johon tallennustiedoston avaimet ja arvot voidaan sijoittaa.
    tiedot = {}
    # Käydään kaikki tallennustiedoston rivit läpi.
    for rivi in rivit:
        # Poistetaan rivin alussa ja lopussa olevat tyhjät merkit.
        # split(":", 1) jakaa rivin kahteen osaan: avaimeen ja arvoon.
        # Esimerkiksi: "nimi: Sofia" muuttuu muotoon: avain = "nimi" ja arvo = "Sofia"
        avain, arvo = rivi.strip().split(":", 1)
        # Tallennetaan avain ja arvo sanakirjaan.
        tiedot[avain] = arvo

    # Luodaan uusi Pelaaja-olio int() muuttaa tiedoston iän merkkijonosta kokonaisluvuksi.
    pelaaja = Pelaaja(tiedot["nimi"], int(tiedot["ika"]))

    # Sanakirjan avulla tallennettu huoneen nimi yhdistetään oikeaan Huone-olioon.
    huoneet = {
        "Työhuone": tyohuone,
        "Kirjasto": kirjasto,
        "Keittiö": keittio,
        "Olohuone": olohuone,
        "Ruokasali": ruokasali}

    # Tarkistetaan, löytyykö tallennettu sijainti huoneiden sanakirjasta.
    # Jos löytyy, pelaajan sijainniksi asetetaan tämä Huone-olio.
    if tiedot["sijainti"] in huoneet:
        pelaaja.sijainti = huoneet[tiedot["sijainti"]]

    # Sanakirja, jonka avulla tallennettu esineen nimi voidaan yhdistää oikeaan Esine-olioon.
    kaikki_esineet = {
        "Tutkimuspaperi": tutkimuspaperi,
        "Yrityksen avainkortti": avainkortti,
        "USB-kotelo": usb_kotelo,
        "Teekuppi": kuppi,
        "Muistilappu": muistilappu}

    # Jos inventaariossa on tallennettuja esineitä, palautetaan ne pelaajan inventaarioon.
    if tiedot["inventaario"]:

        # split(",") jakaa tallennetun merkkijonon takaisin yksittäisiksi esineiden nimiksi.
        # Esimerkiksi: "Tutkimuspaperi,Teekuppi" muuttuu listaksi: ["Tutkimuspaperi", "Teekuppi"]
        esineiden_nimet = tiedot["inventaario"].split(",")
        # Käydään kaikki tallennetut esineet läpi.
        for nimi in esineiden_nimet:
            # Tarkistetaan, löytyykö nimi kaikki_esineet-sanakirjasta.
            if nimi in kaikki_esineet:
                # Lisätään oikea Esine-olio pelaajan inventaarioon.
                pelaaja.inventaario.append(kaikki_esineet[nimi])

    # Jos pelaajalla on tallennettuja vihjeitä, palautetaan ne vihjelistaan.
    if tiedot["vihjeet"]:
        # split("|") jakaa tallennetun tekstin takaisin yksittäisiksi vihjeiksi.
        pelaaja.vihjeet = tiedot["vihjeet"].split("|")

    # Tallennuksessa True ja False ovat tekstiä.
    # Vertailulla muutetaan "True" oikeaksi boolean-arvoksi True.
    # Jos arvo on jotain muuta, tulokseksi tulee False.
    pelaaja.pin_ratkaistu = tiedot["pin_ratkaistu"] == "True"

    # Pelaajan mukana olevat esineet täytyy poistaa huoneista, muuten voisi löytyä sama esine.
    for huone in huoneet.values():
        # [:] tekee huoneen esineistä kopion, jota voidaan käydä läpi
        # samalla kun alkuperäisestä poistetaan esineitä.
        for esine in huone.esineet[:]:
            # Jos esine on pelaajan inventaariossa, poistetaan se huoneesta.
            if esine in pelaaja.inventaario:
                huone.esineet.remove(esine)
    # Ilmoitetaan pelaajalle, että tallennus ladattiin onnistuneesti.
    print("\nTallennettu peli ladattu!")
    # Palautetaan valmis Pelaaja-olio main.py:lle.
    return pelaaja