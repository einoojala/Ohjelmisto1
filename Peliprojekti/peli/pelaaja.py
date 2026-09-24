# Luokka, joka sisältää pelaajan tiedot ja pelaajan toimintoja.
class Pelaaja:
    # Alustetaan uuden pelaajan tiedot.
    def __init__(self, nimi, ika):
        # Tallennetaan pelaajan nimi ja muutetaan ensimmäinen kirjain isoksi.
        self.nimi = nimi.capitalize()
        # Tallennetaan pelaajan ikä.
        self.ika = ika
        # Lista pelaajan mukana olevista esineistä, johon lisätään esineitä pelin aikana.
        self.inventaario = []
        # Lista pelaajan löytämistä vihjeistä.
        self.vihjeet = []
        # Pelaajan nykyinen sijainti. Aluksi pelaaja ei ole vielä missään huoneessa.
        self.sijainti = None
        # False tarkoittaa, että PIN-koodia ei vielä ratkaistu.
        # Arvoksi muuttuu True, kun pelaaja ratkaisee oikean PIN-koodin.
        self.pin_ratkaistu = False

    # Metodi, jolla pelaajan inventaarioon lisätään esine.
    def lisaa_esine(self, esine):
        # Tarkistetaan ensin, ettei sama esine ole jo inventaariossa.
        if esine not in self.inventaario:
            # Lisätään esine pelaajan inventaarioon.
            self.inventaario.append(esine)
            # Ilmoitetaan pelaajalle, että esine on lisätty.
            print(f"{esine.nimi} lisättiin inventaarioon.")

    # Metodi, jolla pelaaja voi tarkastella inventaariossa olevia esineitä.
    def nayta_inventaario(self):

        # Valikko pysyy auki, kunnes bvalitaan "x" tai inventaario on tyhjä.
        while True:
            print("\n--- INVENTAARIO ---")
            # Jos inventaariossa ei ole esineitä, ilmoitetaan siitä ja poistutaan metodista.
            if len(self.inventaario) == 0:
                print("Inventaario on tyhjä.")
                return

            # enumerate() antaa jokaiselle esineelle järjestysnumeron, alkaen rvosta 1
            for numero, esine in enumerate(self.inventaario, 1):
                print(f"{numero}. {esine.nimi}")
            print("x. Takaisin")

            # Kysytään pelaajalta, mitä esinettä hän haluaa tutkia.
            valinta = input("Mitä esinettä haluat tutkia? ")
            # Jos valinta "x", palataan takaisin päävalikkoon.
            if valinta.lower() == "x":
                return

            # Tarkistetaan, että valinta on numero. Jos se ei, palataan while-silmukan alkuun.
            if not valinta.isdigit():
                print("Anna numero.")
                continue

            # Muutetaan käyttäjän antama merkkijono kokonaisluvuksi, jotta voidaan käyttää listan indeksinä.
            numero = int(valinta)

            # Tarkistetaan, että annettu numero vastaa jotain inventaarion esinettä.
            if 1 <= numero <= len(self.inventaario):
                # Haetaan esine inventaariosta. Listan indeksit alkavat nollasta, joten käyttäjän
                # antamasta numerosta vähennetään yksi.
                esine = self.inventaario[numero - 1]

                # Kutsutaan esineen tutki()-metodia. self tarkoittaa tässä nykyistä Pelaaja-oliota,
                # jotta esine voi lisätä löytyvän vihjeen pelaajalle.
                esine.tutki(self)
            else:
                # Ilmoitetaan, jos käyttäjän antama numero ei vastaa mitään inventaarion esinettä.
                print("Tuntematon valinta.")

    # Metodi, jolla pelaajalle lisätään uusi vihje.
    def lisaa_vihje(self, vihje):
        # Tarkistetaan, ettei samaa vihjettä ole jo löydetty.
        if vihje not in self.vihjeet:
            # Lisätään uusi vihje pelaajan vihjelistaan.
            self.vihjeet.append(vihje)
            # Ilmoitetaan pelaajalle uuden vihjeen löytymisestä.
            print("\nUusi vihje löydetty!")

    # Metodi, jolla näytetään kaikki pelaajan löytämät vihjeet.
    def nayta_vihjeet(self):
        print("\n--- LÖYDETYT VIHJEET ---")
        # Jos pelaaja ei ole löytänyt vielä yhtään vihjettä, näytetään siitä ilmoitus.
        if len(self.vihjeet) == 0:
            print("Et ole vielä löytänyt vihjeitä.")
        else:
            # Käydään kaikki löydetyt vihjeet läpi ja tulostetaan ne yksi kerrallaan.
            for vihje in self.vihjeet:
                print(f"- {vihje}")