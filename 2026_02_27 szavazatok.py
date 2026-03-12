#https://github.com/szabodanielckik
def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(" ")
        lista.append((int(st[0]),int(st[1]),st[2],st[3],st[4]))
    return lista

def feladat4(adatok):
    szavazatokSzama = osszesSzavazat(adatok)
    mindenki = 12345
def osszegzes(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i]
    return osszeg
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

def feladat4(adatok):

    szavazatokSzama = osszesSzavazat(adatok)
    mindenki = 12345
    szazalek = szavazatokSzama / mindenki *100
    print(f"A választáson {szavazatokSzama} állampolgár, a jogosultak{round(szazalek),2} %-a vett részt.")

def partDarab(part):
    db = 0
    for i in range(len(adatok)):
        if(adatok[i][4] == part):
            db += 1
    return db

def feladat5(adatok):
    gyep = partDarab("GYEP")
    hep = partDarab("HEP")
    tisz = partDarab("TISZ")
    zep = partDarab("ZEP")
    fugg = partDarab("-")
    print("Gyümölcsevők pártja =",gyep)
    print("Húsevők pártja =",hep)
    print("Tejivók szövetsége =",tisz)
    print("Zöldségevők pártja =",zep)
    print("Független párt =",fugg)


def feladat6(adatok):
    maxe = maximumSzavazatok(adatok)
    for i in range(len(adatok)):
        if(adatok[i][1] == maxe):
            print(f"{adatok[i][2]} {adatok[i][3]} {adatok[i][4]}")
    

def main():
    adatok = listaFeltoltes()
    print(adatok)

    print("A helyhatósági választáson" ,len(adatok),"képviselőjelölt indult.")

    feladat3(adatok)

    feladat4(adatok)

    feladat5(adatok)

    feladat6(adatok)


main()