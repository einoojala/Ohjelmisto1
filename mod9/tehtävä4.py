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

autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", 0)
    autot.append(auto)

while True:

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

    for auto in autot:
        auto.kulje(1)

    kilpailu_loppui = False

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppui = True
            break

    if kilpailu_loppui:
        break

print(f"{'Rekisteritunnus':<18}{'Huippunopeus':<18}"
      f"{'Nykyinen nopeus':<20}{'Kuljettu matka':<18}")

print("-" * 74)

for auto in autot:
    print(f"{auto.rekisteritunnus:<18}"
          f"{auto.huippunopeus:<18}"
          f"{auto.nykyinen_nopeus:<20}"
          f"{auto.kuljettu_matka:<18.1f}")