'''
1. Lue koodi läpi, suorita se, varmista että ymmärrät, miten se toimii nyt.
2. Luo luokat Hirvio ja Pelaajahahmo. Ne molemmat perivät luokan Hahmo.
3. Muokkaa koodia niin, että lisäät Pelaajahahmo-luokalle ominaisuuden tavaralista. 
Kun pelaajahahmo-olio luodaan, se saa parametrinä listan tavaroita, jotka tallennetaan olion listaan.
4. Ylikirjoita Hahmo-luokan tulosta-metodi Pelaajahahmolle niin, että se tulostaa mukaan myös tavaralistan.
5. Muokkaa niin, että vain hirviöillä on repliikki, ei kaikilla Hahmo-olioilla.
6. Ylikirjoita Hirvio-luokan tulosta-metodi niin, että se tulostaa myös repliikin.
7. Jos ehdit: Luo peliin useampi hirviö, ja laita pelaajahahmo taistelemaan myös niiden kanssa. 
Taistelu-metodia ei tarvita sekä hahmolle että hirviölle. 
Siirrä se sille luokalle, jossa se on sinusta looginen. 
Testaa, että peli toimii järkevästi.
'''

class Hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = 100

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki):
        super().__init__(nimi)
        self.repliikki = repliikki

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Repliikki: {self.repliikki}")

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

merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!")
luolahirvio = Hirvio( "Luolahirviö", "Kuka uskaltaa tulla luolaani?")
pelaajahahmo = Pelaajahahmo(input("Anna hahmon nimi: "), ["Miekka", "Kilpi", "Parantava juoma"])

print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()

print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön.")
print(f"Hirviö huutaa: {merihirvio.repliikki}")
merihirvio.tulosta_tiedot()

input()
pelaajahahmo.taistelu(merihirvio)

if pelaajahahmo.hp > 0:
    input()

    print(f"{pelaajahahmo.nimi} kohtaa viimeisen hirviön.")
    print(f"Hirviö huutaa: {luolahirvio.repliikki}")
    luolahirvio.tulosta_tiedot()

    input()
    pelaajahahmo.taistelu(luolahirvio)

if pelaajahahmo.hp > 0:
    print("Kaikki hirviöt on voitettu!")
    print("Peli ohi.")
else:
    print("Pelaajahahmo hävisi.")
    print("Peli ohi.")