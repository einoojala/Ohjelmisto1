import random

class Auto:
    def __init__(self, rekisteritunnus, nykyinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nykyinen_nopeus += nopeuden_muutos

        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus

        if self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nykyinen_nopeus

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)

        for auto in self.autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<18}"
              f"{'Nykyinen nopeus':<20}{'Kuljettu matka':<18}")

        print("-" * 74)

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<18}"
                  f"{auto.huippunopeus:<18}"
                  f"{auto.nykyinen_nopeus:<20}"
                  f"{auto.kuljettu_matka:<18.1f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True

        return False

autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", 0)
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()