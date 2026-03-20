
def fajlBeolvasas():
    fajl = open("szeleromu.txt","r",encoding ="utf-8")
    sorok = fajl.readlines()

    
    
    t = []
    for sor in sorok:
        st = sor.strip().split(';')
        t.append((st[0],(st[1]),(st[2]),int(st[3]),int(st[4]),int(st[5])))

    fajl.close()
    return t

def szeleromuvekSzama(adatok):
    db = 0
    ev = int(input("Adja meg melyik év szélerőműveire kíváncsi: "))
    for i in range(0,len(adatok),1):
        if(ev == adatok[i][5]):
            db += adatok[i][3]
    return db



def main():
    adatok = fajlBeolvasas()
    print(adatok)
    print(szeleromuvekSzama(adatok))


main()