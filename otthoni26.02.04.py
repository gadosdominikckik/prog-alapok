# HF 
# Szimuláljon egy matematika versenyt és az eredményeire készített statisztikát! Mind a 17 diák nagyon ügyes, így kevés rossz verseny dolgozat született. A döntőbe jutásésrt 70%-ot el kell érni.
# 1. Készítsen egy függvényt, amit feltölt egy listát úgy, hogy 50%-os eseéllyel szülessenek 120-200 közötti pontok, a maradék pedig 50-120 közötti pont legyen!
# 2. Írjon függvényt, ami visszaadja a versenydolgozatok átlagát!
# 3. Írjon függvényt, ami visszaadja a versenydolgozatok terjedelmét!
# 4. Írjon függvényt, ami visszaadja lett-e maximum pontos?
# 5. Írjon függvényt, ami visszaadja hány versenyző jutott a döntőbe?
# 6. Írjon függvényt, ami visszaadja, hogy volt-e 50 pontos, ha volt hányadik tanuló?
# 17 diak
# 70 szazalek az atjutashoz
import random
import math

def listafeltolt():
    lista = []
    db = 17
    for i in range(0,db,1):
        a = random.randint(0,100)
        if (a >= 50):
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))
    return lista

def pontAtlag(lista):
    atlag = 0
    for i in range(0,len(lista),1):
        atlag += lista[i]
    atlag = round(atlag / len(lista),1)
    return atlag

def terjedlista(lista):
    maxe = lista[0]
    mine = lista[0]
    for i in range(0,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
        if(lista[i]<mine):
            mine = lista[i]
    terj = maxe-mine
    return terj


def vanmax(lista):
    index = 0
    while(index<len(lista) and lista[index] != 200):
        index += 1
    vane = index < len(lista)
    return vane

def tovabbjutok(lista):
    db = 0
    for i in range (0,len(lista),1):
        # szazalek = lista[i]
        # if(lista[i]/200*100 >= 70):
        ponthatar = 200 / 100 *70
        if(lista[i] >= ponthatar):
            db += 1
    return db

def ertek50index(lista):
    i = 0
    while (i<len(lista) and lista[i] != 50):
        i += 1
        vane = i < len(lista)
    if(vane):
        return i
    else:
        return -1





def main():
    lista = listafeltolt()
    print(lista)
    atlag = pontAtlag(lista)
    print(atlag)
    terjedelem = terjedlista(lista)
    print(terjedelem)
    maxp = vanmax(lista)
    print(maxp)
    darab = tovabbjutok(lista)
    print(darab)
    index = ertek50index(lista)
    if ( index == -1):
        print("Nincs 50 pontos dolgozat a versenyen")
    else:
        print(f"A(z) {index}. van az 50 pontos dolgozat")




main()

# import random


# def listafeltol(db):
#     lista = []
#     for i in range(0,db,1):
#         a = random.randint(0,1)
#         if a == 0:
#             versenyzo = random.randint(120,200)
#         else:
#             versenyzo = random.randint(50,120)
#         lista.append(versenyzo)
#     return lista





# def dogaatlag(lista):
#     atlag = 0
#     for i in range(0,len(lista),1):
#         atlag += lista[i]
#     atlag = round(atlag /len(lista),2)
#     return atlag

# def terjedelem(lista):
#     min =lista[0]
#     max = lista[0]
#     for i in range(1,len(lista),1):
#         if lista[i] <min:
#             min= lista[i]
#         if lista[i] >max:
#             max = lista[i]
    
#     terj = max-min
#     return terj

# def vanmax(lista,maxp):
    
#     i = 0
#     while i <len(lista):
#         i +=1
#         if lista[i] ==maxp:
#             return True
#         else :  return False

# def tovabbjutok(lista,maxp):
#     tovabb = maxp * 0.7
#     i = 0
#     nyertesek= 0
#     while i < len(lista):
#         if tovabb <=lista[i]:
#             nyertesek += 1
#         i +=1

#     return nyertesek


        


# def main():
#     db = 17
#     lista =listafeltol(db)
#     print(lista)
#     atlag =dogaatlag(lista)
#     print(atlag)
#     terj = terjedelem(lista)
#     print(terj)
#     maxp = vanmax(lista,200)
#     print(maxp)
#     tov =tovabbjutok(lista,200)
#     print(tov)


# main()