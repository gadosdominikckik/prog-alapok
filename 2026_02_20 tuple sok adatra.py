# 5
# alma 12 500
# körte 10 600
# szilva 13 300
# cseresznye 8 1200
# meggy 6 1150

def listaFeltoltes():
    db = int(input(""))
    t = []
    for i in range(db):
        sor = input()
        st = sor.split(' ')
        tuple = (st[0],int(st[1]),int(st[2]))
        t.append(tuple)
    return t
    input()

def mazsaosszegzese(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i][1]
    return osszeg

def hanyArNagyobb(adatok,ar):
    if(adatok[i][2]>ar):
        db += 1
    return db


def main():
    adatok = listaFeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    osszesen = mazsaosszegzese(adatok)
    print(osszesen)

    ar = 1000
    db = hanyArNagyobb(adatok,ar)
    print(db)

    #irjon fuggvenyt ami visszaadja az osszesitett ertekbol 
    #hogy hany mazsa gyumolcs van

main()

#HF: irj fuggvenyt ami megadja a legdragabb gyumolcsot ,irjon fuggvenyt ami beker a felhasznalotol egy gyumolcsot es ha vanilyen gyumolcs kiirja az adatait 
# BE : szilva KI : 100ft / kg