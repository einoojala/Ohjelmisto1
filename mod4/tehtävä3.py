sukupuoli = input("Anna sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiini arvo: "))

if sukupuoli == "mies" and 134 <= hemoglobiini <= 195:
    print("Hemoglobiini on normaali")
elif sukupuoli == "mies" and hemoglobiini < 134:
    print("Hemoglobiini on alhainen")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("Hemoglobiini on korkea")
elif sukupuoli == "nainen" and 117 <= hemoglobiini <= 175:
    print("Hemoglobiini on normaali")
elif sukupuoli == "nainen" and hemoglobiini < 117:
    print("Hemoglobiini on alhainen")
elif sukupuoli == "nainen" and hemoglobiini > 175:
    print("Hemoglobiini on korkea")