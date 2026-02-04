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
        a = random.randint(0,1)
        if (a == 0):
            versenyzo = random.randint(120,200)
        else:
            versenyzo = random.randint(50,120)
        lista.append(versenyzo)
    return lista

def pontAtlag(lista):
    atlag = 0
    for i in range(0,len(lista),1):
        atlag += lista[i]
    atlag = round(atlag / len(lista),2)
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
    return maxe


def vanmax(lista,maxp):
    i = 0
    while i <len(lista):
        i +=1
        if lista[i] ==maxp:
            return True
        else :  return False

def tovabbjutok(lista,maxp):
    tovabb = maxp * 0.7
    for i in range (0,len(lista),1):
        tovabbjutoksz = 0
        if tovabb <= lista[i]:
            tovabbjutoksz += 1
    return tovabbjutoksz





    







def main():
    lista = listafeltolt()
    print(lista)
    atlag = pontAtlag(lista)
    print(atlag)
    terjedelem = terjedlista(lista)
    print(terjedelem)
    maxp = vanmax(lista,200)
    print(maxp)
    tovabbjut = tovabbjutok(lista,maxp)
    print(maxp)




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