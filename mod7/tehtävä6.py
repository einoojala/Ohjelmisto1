import math

def pizza_hinta(halkaisija: float, hinta: float):
    halkaisija_m = halkaisija / 100
    pinta_ala = math.pi * (halkaisija_m / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

pizza1_halkaisija = float(input("Anna pizzan 1 halkaisija (cm): "))
pizza1_hinta = float(input("Anna pizzan 1 hinta (€): "))

pizza2_halkaisija = float(input("Anna pizzan 2 halkaisija (cm): "))
pizza2_hinta = float(input("Anna pizzan 2 hinta (€): "))

tulos1 = pizza_hinta(pizza1_halkaisija, pizza1_hinta)
tulos2 = pizza_hinta(pizza2_halkaisija, pizza2_hinta)

if tulos1 < tulos2:
    print("Pizza 1 antaa paremman vastineen rahalle")
elif tulos2 < tulos1:
    print("Pizza 2 antaa paremman vastineen rahalle")
else:
    print("Pizzoilla on sama yksikköhinta")