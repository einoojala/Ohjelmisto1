class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = 2000

    def kiihdyta(self, nopeuden_muutos):
        self.nykyinen_nopeus += nopeuden_muutos

        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus

        if self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nykyinen_nopeus

auto = Auto("ABC-123", 142, 0)

auto.kiihdyta(60)
auto.kulje(1.5)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nykyinen nopeus: {auto.nykyinen_nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")