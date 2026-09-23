def parittomat_pois(lista: list):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

lista = [1,4,6,9,12,15,22]
print(lista)
tulos = parittomat_pois(lista)
print(tulos)