def adatokBeolvasasa():
    lista=[]
    db = int(input)
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),int(st[4]),int(st[5])))
    return lista

def szeleromuvekDarab(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg
def main():
    adatok = adatokBeolvasasa()
    print(adatok)
    db = szeleromuvekDarab(t)

main()