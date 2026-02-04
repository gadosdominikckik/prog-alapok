# [-950,950 kozott] x50 x00 tipusu sza,pl
# [-19,-19] *50
import random    
"""
 == : Egyenlő
 != : Nem egyenlő
"""
#Írjon fv-t ami visszaadja a listank terjedelmet

# def listaTerjed(lista):
#     maxe = lista[0]
#     mine = lista[0]
#     for i in range(1,len(lista),1):
#         if(lista[i]>maxe):
#             maxe = lista[i]
#         if(lista[i]<mine):
#             mine = lista[i]
#     terjedelem = maxe - mine
#     return terjedelem

def maximumErtek(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
    return maxe

def minimumErtek(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mine):
            mine = lista[i]
    return mine



def terjedelem(lista):
    maxe = maximumErtek(lista)
    mine = minimumErtek(lista)
    return maxe - mine



def maximumindex(lista):
    maxi = 0
    for i in range(1,len(lista),1):
        if(lista[i]>lista[maxi]):
            maxi = i
    return maxi


def pozitivatlag(lista):
    db = 0
    osszeg = 0
    for elem in lista:   # végigmegyünk a lista összes elemén
        if(elem>0):
            db+=1
            osszeg += elem
    atlag = osszeg / db 
    return atlag




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
    lista1 = veletlenLista(8)
    print(lista1)
    lista2 = veletlenLista(7)
    print(lista2)

    lista1atlaga= listaatlaga(lista1)
    print("Az első lista átlaga: ", lista1atlaga)
    print("A második lista átlaga: ",listaatlaga(lista2))

    print("Az első lista pozitív számainak átlaga: " ,
    pozitivatlag(lista2))

    maxlista1 = maximumindex(lista1)
    print("Első lista legnagyobb elem helye : ", maxlista1+1)

    print(maximumErtek(lista1))
    print(minimumErtek(lista1))
    print(" Az első lista terjedelme:",terjedelem(lista1))


main()
