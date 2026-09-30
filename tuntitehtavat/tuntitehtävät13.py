# Tehtävä 1
"""
with open("ostoslista.txt", "w", encoding="utf-8") as tiedosto:
    tiedosto.write("maito\nleipä\nkananmunat\nomenat")
"""
# Tehtävä 2
"""
with open("ostoslista.txt", "a", encoding="utf-8") as tiedosto:
    tiedosto.write("\njuustoa\nhedelmiä")
"""

# Tehtävä 3
"""
with open("ostoslista.txt", "r", encoding="utf-8") as tiedosto:
    data = tiedosto.readlines()

for tuote in data:
    print(tuote.strip())

print(f"\nTuotteita listalla: {len(data)}")
"""

# Tehtävä 4
"""
import json

elokuva = {
    "Nimi": "Inception",
    "Vuosi": 2010,
    "Näyttelijät": ["Leonardo DiCaprio", "Elliot Page"]
}

with open("elokuva.json", "w", encoding="utf-8") as tiedosto:
    json.dump(elokuva, tiedosto, ensure_ascii=False, indent=1)

with open("elokuva.json", "r", encoding="utf-8") as tiedosto:
    data = json.load(tiedosto)

print(f"Nimi: {data['Nimi']}")
print(f"Vuosi: {data['Vuosi']}")
print(f"Näyttelijät: {', '.join(data['Näyttelijät'])}")
"""
# Tehtävä 5
"""
while True:
    tiedoston_nimi = input("Anna Tiedoston nimi: ")

    if not tiedoston_nimi:
        print("Annoit tyhjän merkkijonon")
        continue

    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as tiedosto:
            data = tiedosto.readlines()

        for rivi in data:
            print(rivi.strip())
        break

    except FileNotFoundError:
        print("Tiedostoa ei löydy, yritä uudelleen")
"""

# Tehtävä 6
"""
import os

while True:
    tiedoston_nimi = input("Anna Tiedoston nimi: ")

    if not tiedoston_nimi:
        print("Annoit tyhjän merkkijonon")
        continue

    try:
        os.remove(tiedoston_nimi)
        break

    except FileNotFoundError:
        print("Tiedostoa ei löydy, yritä uudelleen")
"""