class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.nykyinen_nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nykyinen_nopeus

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nykyinen_nopeus = 100
polttomoottoriauto.nykyinen_nopeus = 120

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(sahkoauto.kuljettu_matka)
print(polttomoottoriauto.kuljettu_matka)