class Hissi:
    def __init__(self, alin, ylin, numero):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
        self.numero = numero

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi {self.numero} on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi {self.numero} on nyt kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissien_lkm = hissien_lkm
        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(alin, ylin, i + 1)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)

talo = Talo(1, 10, 3)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 3)
talo.palohalytys()