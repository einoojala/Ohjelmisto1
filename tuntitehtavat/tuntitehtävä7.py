while True:
    laskutoimitus = input("Anna laskutoimitus (Plus, Miinus, Kerto, Jako, Modulo tai Lopeta): ").lower()

    if laskutoimitus == "lopeta":
        break

    luku1 = float(input("Anna luku 1: "))
    luku2 = float(input("Anna luku 2: "))

    if laskutoimitus == "plus":
        print(f"Tulos on: {luku1 + luku2}")
    elif laskutoimitus == "miinus":
        print(f"Tulos on: {luku1 - luku2}")
    elif laskutoimitus == "kerto":
        print(f"Tulos on: {luku1 * luku2}")
    elif laskutoimitus == "jako":
        print(f"Tulos on: {luku1 / luku2}")
    elif laskutoimitus == "modulo":
        print(f"Tulos on: {luku1 % luku2}")
    else:
        print("Tuntematon laskutoimitus.")