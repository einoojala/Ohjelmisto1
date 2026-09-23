vuosi = int(input("Anna vuosi: "))

if vuosi == 1916:
    print("Olympialaisia ei järjestetty ensimmäisen maailmansodan vuoksi")
elif vuosi == 1940:
    print("Olympialaisia ei järjestetty toisen maailmansodan vuoksi")
elif vuosi == 1944:
    print("Olympialaisia ei järjestetty toisen maailmansodan vuoksi")
elif vuosi == 2020:
    print("Tokion olympialaiset siirrettiin vuoteen 2021")
elif vuosi == 2021:
    print("2021 oli olympiavuosi")
elif vuosi > 2026:
    print("Vuosi on tulevaisuudessa")
elif vuosi % 4 == 0:
    print("On olympiavuosi")
else:
    print("Ei ollut olympiavuosi")