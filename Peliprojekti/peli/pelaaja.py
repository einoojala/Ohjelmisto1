class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi.strip().title()
        self.ika = ika
        self.inventaario = []
        self.vihjeet = []
        self.tutkitut_huoneet = []
        self.tutkitut_epaillyt = []
        self.sijainti = None
        self.pin_ratkaistu = False

    # Lisää esineen pelaajan inventaarioon, jos sitä ei siellä vielä ole.
    def lisaa_esine(self, esine):
        if esine not in self.inventaario:
            self.inventaario.append(esine)
            print(f"{esine.nimi} lisättiin inventaarioon.")

    # Näyttää pelaajan inventaarion ja antaa mahdollisuuden tutkia esineitä.
    def nayta_inventaario(self):
        while True:
            print("\n--- INVENTAARIO ---")
            if not self.inventaario:
                print("Inventaario on tyhjä.")
                return

            for numero, esine in enumerate(self.inventaario, 1):
                print(f"{numero}. {esine.nimi}")
            print("x. Takaisin")

            valinta = input("Mitä esinettä haluat tutkia? ")

            if valinta.lower() == "x":
                return
            
            if not valinta.isdigit():
                print("Anna numero.")
                continue

            numero = int(valinta)

            # Tarkistetaan, että annettu numero vastaa jotain inventaarion esinettä.
            if 1 <= numero <= len(self.inventaario):
                # Listan indeksit alkavat nollasta, joten käyttäjän numerosta vähennetään yksi.
                esine = self.inventaario[numero - 1]
                esine.tutki()
                self.lisaa_vihje(esine.vihje)
            else:
                print("Tuntematon valinta.")

    # Lisää uuden vihjeen pelaajan vihjelistaan, jos sitä ei ole vielä löydetty.
    def lisaa_vihje(self, vihje):
        if vihje not in self.vihjeet:
            self.vihjeet.append(vihje)
            print("\nUusi vihje löydetty!")

    # Näyttää kaikki pelaajan löytämät vihjeet.
    def nayta_vihjeet(self):
        print("\n--- LÖYDETYT VIHJEET ---")
        
        if not self.vihjeet:
            print("Et ole vielä löytänyt vihjeitä.")
        else:
            for vihje in self.vihjeet:
                print(f"- {vihje}")

    # Näyttää tutkinnan tämänhetkisen tilanteen.
    def nayta_tutkinnan_tilanne(self):
        print("\n--- TUTKINNAN TILANNE ---")
        print(f"Vihjeet: {len(self.vihjeet)} / 12")
        print(f"Esineet: {len(self.inventaario)} / 6")
        print(f"Tarkemmin tutkitut huoneet: {len(self.tutkitut_huoneet)} / 5")
        print(f"Tutkitut epäillyt: {len(self.tutkitut_epaillyt)} / 4")

        if self.sijainti is not None:
            print(f"Sijainti: {self.sijainti.nimi}")
        else:
            print("Sijainti: Et ole vielä missään huoneessa.")
            
        if self.pin_ratkaistu:
            print("PIN-koodi: Ratkaistu")
        else:
            print("PIN-koodi: Ratkaisematta")