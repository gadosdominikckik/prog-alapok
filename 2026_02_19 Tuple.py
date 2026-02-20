# a = 23
# b = "alma"
# c = True

# t = [a,b,c]
# t = [0]

def maxi1(lista):
    maxi = 0
    for i in range(0,len(lista),1):
        if(lista[0]>lista[maxi]):
            maxi = i
    return maxi

def maxi2(szamok , honapok):
    maxi = 0
    honap = honapok[0]
    for i in range(0,len(szamok),1):
        if(szamok[i]>szamok[maxi]):
            maxi = i
            honap = honapok[i]
    return (honap,maxi,szamok[maxi])



def main():
    honapok =["Január","Február","Március","Április","Május","Június","Július",
    "Augusztus","Szeptember","Október","November","December"]
    Jani = [4.0 , 3.8 , 4.2 , 4.1 , 3.8 , 4.2 , 3.0 , 3.6 ,4.2 , 4.1 , 4.7, 4.2]
    maxi = maxi1(Jani)
    print(honapok[maxi])
    #tordeles
    szoveg = "Jani 2000 10 03"
    print(szoveg)
    tordelt = szoveg.split(" ")
    print(tordelt)
    print(2026 -int(tordelt[1]))
    
    
    adat = (tordelt[0] , int(tordelt[1]), int(tordelt[2]) , int(tordelt[3]))
    print(adat)
    
    szoveg2 = "2026.02.19 3 Programozás"
    tordeles = szoveg2.split(" ")
    print(tordeles)
    adat1 = (tordeles[0].split("."))
    print(adat1[1])

    szoveg3 = "IOV-878,Gados Peter,vz5551616v,2003.03.20"
    leon = szoveg3.split(",")
    print(leon)
    datum = leon[3].split(".")
    print(datum[0])
    vezeteknev = leon[1].split(" ")
    print(vezeteknev[0])
    # 5
    # alma 12 500
    # körte 10 600
    # szilva 13 300
    # cseresznye 8 1200
    # meggy 6 1150
    

main()

