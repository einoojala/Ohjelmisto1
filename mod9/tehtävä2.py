class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykyinen_nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nykyinen_nopeus += nopeuden_muutos

        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus

        if self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0

auto = Auto("ABC-123", 142, 0)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nykyinen nopeus: {auto.nykyinen_nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")

auto.kiihdyta(-200)
print(f"Nykyinen nopeus hätäjarrutuksen jälkeen: {auto.nykyinen_nopeus} km/h")