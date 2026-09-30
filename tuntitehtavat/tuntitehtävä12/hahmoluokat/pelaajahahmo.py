from .hahmo import Hahmo

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, tavaralista):
        super().__init__(nimi)
        self.tavaralista = tavaralista

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tavaralista: {self.tavaralista}")

    def taistelu(self, vastustaja):
        print(f"{self.nimi} taistelee hirviötä {vastustaja.nimi} vastaan.")
        print("Tulee suuri taistelu.")
        input()

        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            vastustaja.hp = 0
            self.tulosta_tiedot()
