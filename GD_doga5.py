import random
def listafeltoltes():
    lista1 = []
    db = 7
    for i in range(0,db,1):
        vszam = random.randint(1,18)
        lista1.append(vszam)
    return lista1

    lista2 = []
    db = 7
    for i in range(0,db,1):
        vszam1 = random.randint(1,18)
        lista2.append(vszam1)
    return lista2
    

# def listaosszeg():
#     osszeg = 0
#     for i in range(0,len(lista1),1):
#         osszeg = lista1[i]+lista1[i]
#     return osszeg


    

    





def main():
    szam = listafeltoltes()
    print(szam)
    #  osszeg = listaosszeg(lista1)
    #  print(osszeg)


main()