# Készítsen egy függvényt ami egy darab számtól függ, és visszaad egy feltöltött listát [-10,50] közötti számokkal.

import random

def listafeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(-10,50)
        lista.append(szam)
    return lista

def pozitivdb(szlista):
    darab = 0
    for i in range(0,len(szlista),1):
        if(szlista[i]>0):
            darab += 1
    return darab        



def main():
    lista = listafeltolt(13)
    print(lista)
    print(pozitivdb(lista))

main()
