massa = float(input("Kuinka monta grammaa: "))

kilot = int(massa // 1000)
grammat = int(massa % 1000)

print(f"Määrä kiloina ja grammoina: {kilot} kg {grammat} g")