class Lentokone:
    def __init__(self, nimi, maksimi_bensa, nykyinen_bensa):
        self.nimi = nimi
        self.maksimi_bensa = maksimi_bensa
        self.nykyinen_bensa = nykyinen_bensa

    def tankkaa(self):
        mahtui = self.maksimi_bensa - self.nykyinen_bensa
        self.nykyinen_bensa = self.maksimi_bensa
        print(f"Tankkiin mahtui {mahtui} litraa bensaa.")

    def tulosta_tiedot(self):
        print(f"Lentokone: {self.nimi}")
        print(f"Tankin maksimi: {self.maksimi_bensa} litraa")
        print(f"Tankissa nyt: {self.nykyinen_bensa} litraa")

class Lentokenttä:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koneet = []

    def lisää_kone(self, kone):
        self.koneet.append(kone)

    def tulosta_koneet(self):
        print(f"Lentokenttä: {self.nimi}")
        print("\nKentällä olevat koneet:")

        for kone in self.koneet:
            kone.tulosta_tiedot()
            print()

kone1 = Lentokone("AY123", 5000, 2000)
kone2 = Lentokone("FIN456", 8000, 3500)
kone3 = Lentokone("HEL789", 6000, 6000)
kenttä = Lentokenttä("Helsinki-Vantaa")

kenttä.lisää_kone(kone1)
kenttä.lisää_kone(kone2)
kenttä.lisää_kone(kone3)

kenttä.tulosta_koneet()

print("Tankataan kone AY123:")
kone1.tankkaa()
print("\nTiedot tankkauksen jälkeen:")
kenttä.tulosta_koneet()