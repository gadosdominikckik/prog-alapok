
def listaFeltoltes():
    db = int(input())
    t = []
    for i in range(db):
        sor = input() #alma 12 500
        st = sor.split(" ")#seged lista: ['alma', '12', '500']
        tuple = (st[0],int(st[1]),int(st[2]))
        t.append(tuple)
    return t

def mazsaOsszegzese(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i][1]
    return osszeg

def hanyArNagyobb(adatok, ar):
    db = 0
    for i in range(len(adatok)):
        if(adatok[i][2] > ar):
            db += 1
    return db

def maxindexSuly(adatok):
    maxi = 0
    for i in range(len(adatok)):
        if(adatok[i][2]>adatok[maxi][2]):
            maxi = i
    return maxi

def gyumolcsKereses(adatok,gyumNev):
    i = 0
    while(i<len(adatok) and adatok[i][0] != gyumNev):
        i += 1



def main():
    adatok = listaFeltoltes()
    print(adatok)
    # print = adatok[2]
    print(adatok[2][0])

    # irjon fuggvenyt ami visszaadja az osszetett szerkezetbol hogy osszesen hany mazsa gyumolcs van
    osszesen = mazsaOsszegzese(adatok)
    print(osszesen)

    #irjon egy fuggvenyt ami visszaadja a parameterben megadott ertektol nagyobb osszeggel rendelkezo gyomulcsok darabszamat
    ar = 1000
    db = hanyArNagyobb(adatok,1000)
    print(db,"Ennyi db gyümölcs nagyobb mint: ",ar)
    
    gyumNev = input("")
    keresesindex = gyumolcsKereses(adatok,gyumNev)
    if(keresesindex)

    #HF 
    #irjon fuggvenyt ami megadja a legdragabb gyumolcs nevet
    #irjon fuggvenyt ami beker a felhasznalotol egy gyomulcsot es ha van ilyen gyumolcs kiirja az adatait be: szilva  ki: 13q, 300 Ft/kg
    #ha nincs ilyen adat akkor irja ki hogy nincs ilyen adat

    index = maxindexSuly(adatok)
    print("Legdrágább gyümölcs: ",adatok[index][0])
main()