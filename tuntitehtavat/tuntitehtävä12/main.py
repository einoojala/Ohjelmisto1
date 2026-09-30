from hahmoluokat import Pelaajahahmo, Hirvio

merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!")
luolahirvio = Hirvio("Luolahirviö", "Kuka uskaltaa tulla luolaani?")
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