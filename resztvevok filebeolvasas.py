def filebeolvasas():
    fajl = open("resztvevok.txt","r",encoding="utf-8")
    elsoSor = fajl.readline()
    sorok = fajl.readlines()
    
    t = []
    for sor in sorok:
        st = sor.strip().split(';')
        t.append((st[0],st[1],st[2],int(st[3]),st[4]))

    fajl.close()
    return t, elsoSor

# def hanyMacska(t,allat):
    
#     for i in range():
#         osszeg = 0
#         if(t[i][4] == osszeg):
#             osszeg += 1
#     return osszeg




def main():
    adatok,elsoSor = filebeolvasas()
    print(adatok,elsoSor)
    # Macskak = hanyMacska(elsoSor)
    



main()