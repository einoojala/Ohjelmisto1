class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus} km/h")
print(f"Nykyinen nopeus: {auto.nykyinen_nopeus} km/h")
print(f"Kuljettu matka: {auto.kuljettu_matka} km")