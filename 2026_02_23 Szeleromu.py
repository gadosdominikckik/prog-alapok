# Hf - szeleromu.txt
    # telepules, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
    # Magyarországon hány szélerőmű van?
    # Írjuk ki, hogy melyik településen és melyik évben telepítették a legtöbb szélerőművet
    # Kérjünk be egy települést! Nézzük meg, hogy van-e ott szélerőmű (pl.: Cegléd: nincs)

def adatokBeolvasasa():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(';')
        lista.append((st[0],st[1],st[2],int(st[3]), int(st[4]), int(st[5])))
    return lista

def szeleromumvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i][3]
    return osszeg

def maximumIndexDb(lista):
    maxi = 0
    for i in range(0,len(lista),1):
        if(lista[i]>lista[maxi]):
            maxi = i
    return maxi

def vanszerelomuVarosban(lista,varos):
    i = 0
    while(i<len(lista) and lista[i][0] != varos):
        i += 1
    vane = i<len(lista)
    return vane


def main():
    t = adatokBeolvasasa()
    #print(t)

    db = szeleromumvekDarab(t)
    print(db)
    
    maxindex = maximumIndexDb(t)
    print(t[maxindex][0],"Városban",t[maxindex][5],"évben csinálták egyszerre a legtöbb erőművet")
    
    varos = input("Adjon meg egy várost: ")
    vane = vanszerelomuVarosban(t,varos)
    if(vane):
        print("Ebben a városban van szélerőmű")
    else:
        print("Ebben a városban nincs szélerőmű")

    # 2013 május digit kult emelt prog
    # szavazatok.txt
    # http://informatika.fazekas.hu/erettsegi/emelt-szintu-feladatok/
main()
