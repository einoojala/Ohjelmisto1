while True:
    menu_list = "select option:\n1. add\n2. subtract\n3. multiply\n0. exit"
    selection = input(menu_list)

    if selection == "0":
         break

    luku1 = float(input("Anna luku 1: "))
    luku2 = float(input("Anna luku 2: "))
    
    if selection == "1":
        print(f"Tulos on: {luku1 + luku2}")
    elif selection == "2":
        print(f"Tulos on: {luku1 - luku2}")
    elif selection == "3":
        print(f"Tulos on: {luku1 * luku2}")
    else:
        print("Tuntematon laskutoimitus.")