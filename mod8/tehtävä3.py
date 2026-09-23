lentoasemat = {
    "EFHK": "Helsinki-Vantaa",
    "ESSA": "Stockholm Arlanda Airport",
    "KJFK": "John F. Kennedy International Airport",
    "ENGM": "Oslo Airport",
    "ZSPD": "Shanghai Pudong International Airport"
}

while True:
    syote = input("Valitse (Hae, Uusi tai Lopeta): ").lower()

    if syote == "lopeta":
        break

    elif syote == "hae":
        hae = input("Anna ICAO-koodi: ").upper()

        if hae in lentoasemat:
            print(f"Lentoasema on {lentoasemat[hae]}")
        else:
            print("ICAO-koodia ei löytynyt.")

    elif syote == "uusi":
        uusi_nimi = input("Anna uuden lentoaseman nimi: ").capitalize()
        uusi_icao = input("Anna uuden lentoaseman ICAO-koodi: ").upper()

        lentoasemat[uusi_icao] = uusi_nimi

        print("Lentoasema lisätty:")
        for key, value in lentoasemat.items():
            print(f"{key}: {value}")

        print()