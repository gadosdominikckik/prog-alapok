# [-950,950 kozott] x50 x00 tipusu sza,pl
# [-19,-19] *50
import random

def pozitivatlag()


def listaatlaga(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    atlag = osszeg / len(lista)
    return atlag

def veletlenLista(n):
    # n = 13
    lista = []
    for i in range(0,n,1):
        negative = random.randint(0,1)
        vszam = random.randint(2,19) *50
        if negative == 0:
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
    return(lista)

def main():
    lista1 = veletlenLista(13)
    print(lista1)
    lista2 = veletlenLista(67)
    print(lista2)

    lista1atlaga= listaatlaga(lista1)
    print("Az első lista átlaga: ", lista1atlaga)
    print("A második lista átlaga: ",listaatlaga(lista2))

main()
