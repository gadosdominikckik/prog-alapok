
def fajlBeolvasas():
    fajl = open("gyumolcsok.txt","r",encoding="utf-8")
    # osszesadat = fajl.read()
    # print(osszesadat)
    
    # sorok = fajl.readlines()
    # print(sorok)
    
    # sor = fajl.readline()
    # print(sor)

    db = int(fajl.readline())
    print(db)

    for i in range(db):
        sor = fajl.readline()
        sor2 = sor.strip().split(' ')
        t.append((sor2[0],int(sor2[1]),int(sor2[2])))


    fajl.close()
    return t


def main():
    fajlBeolvasas()

main()