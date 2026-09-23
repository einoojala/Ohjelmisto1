nimi = input("Anna nimi: ")
adjektiivi = input("Anna adjektiivi: ")

print(f"{nimi} oli {adjektiivi} ritari, joka joutui kaksintaisteluun.")
aseet = input(f"Ensin piti valita aseet. Ottaako {nimi} miekan vai tikarin? ")

if aseet == "tikari":
    print(f"{nimi} lähti urheasti kaksintaisteluun tikari kädessään, mutta vastustajalla oli miekka, ja {nimi} hävisi.")
else:
    print(f"{nimi} lähti urheasti kaksintaisteluun miekka kädessään ja voitti taistelun, koska vastustajalla oli tikari.")