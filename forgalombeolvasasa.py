def fajlBeolvasas():
    fajl = open("forgalom.txt","r",encoding ="utf-8")
    elsoSor = fajl.readline()
    sorok = fajl.readlines()

    t = []
    for sor in sorok:
        st = sor.strip().split(' ')
        t.append((int(st[0]),int(st[1]),int(st[2]),int(st[3]),st[4]))
    
    fajl.close()
    return t, elsoSor



def main():
    adatok = fajlBeolvasas()
    print(adatok)
    t = adatok[0]
    elsoSor = adatok[1]


main()