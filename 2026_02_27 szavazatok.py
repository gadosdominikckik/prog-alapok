
def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),st[2],st[3],st[4]))
    return lista

def kereses(lista,vn,kn):
    i = 0
    while(i<len(lista) and not (lista[i][2] == vn and lista[i][3] == kn)):
        i += 1
    if(i<len(lista)):
        return i
    else:
        return -1
    

def feladat3(adatok):
    vezeteknev = input("Adja meg a vezeteknevet: ")
    keresztnev = input("Adja meg a keresztnevet: ")

    index = kereses(adatok,vezeteknev,keresztnev)
    if (index >= 0):
        print(adatok[index][1])
    else:
        print("Ilyen nevű képviselőjelölt nincs a listában")

def osszesSzavazat(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i][1]
    return osszeg 

# def feladat4(adatok):

    

def main():
    adatok = listaFeltoltes()
    print(adatok)

    print("A helyhatósági választáson" ,len(adatok),"képviselőjelölt indult.")

    feladat3(adatok)



main()