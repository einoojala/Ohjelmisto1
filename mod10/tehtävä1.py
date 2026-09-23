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

h = Hissi(1, 10, 1)
kerros = int(input("Anna kerros: "))
h.siirry_kerrokseen(kerros)
print("Palataan alimpaan kerrokseen.")
h.siirry_kerrokseen(h.alin)