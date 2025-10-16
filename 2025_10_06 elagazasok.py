import random
import math


szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

szam1 = int(input("Adjon meg egy számot:"))
if(szam1 % 10 ==0):
    print("tízzel osztható")
else:
    print("tízzel nem osztható")
    print("az utolso szamjegy:" + str(szam1 % 10))

# Kérjen be egy másik számot es irassa ki a ket szam reciprokanak osszeget

szam2 = int(input("Adjon meg egy másik számot:"))
if(szam != 0):
    if(szam2 != 0):
        rec = 1/szam1
        rec2 = 1/szam2
        print(rec+rec2)
    else:
        print("A második számnak nincs reciproka")

else:
    print("Az első számnak nincs reciproka")


# Adja meg a ket szam osszegenek gyoket


szamossz = szam1 + szam2
if(szamossz >= 0):
    print(math.sqrt(szamossz))
else:
    print("A két szám összege negatív")


# Logikai Operátorok
# and, or, xor, not

if(szam != 0 and szam2 != 0):
    rec = 1/szam1
    rec2 = 1/szam2
    print(rec+rec2)
else:
    print("A két szám valamelyike nulla!")


#HF: bool algebra
#HF: Kérjen be a felhasználótól 3db számot, ez a 3 szam egy haromszog oldala.
#1.Derékszögű-e
#2.egyenlőszárú-e?
#3.Szabályos-e?

a = int(input("Add meg az első oldalt: "))
b = int(input("Add meg a második oldalt: "))
c = int(input("Add meg a harmadik oldalt: "))

if a + b > c and a + c > b and b + c > a:
    print("Ez egy érvényes háromszög.")

    oldal = sorted([a, b, c]) 
    if abs(oldal[0]**2 + oldal[1]**2 - oldal[2]**2) < 1e-6:
        print("Derékszögű háromszög.")
    else:
        print("Nem derékszögű háromszög.")

    if a == b or b == c or a == c:
        print("Egyenlő szárú háromszög.")
    else:
        print("Nem egyenlő szárú háromszög.")


    if a == b == c:
        print("Szabályos háromszög.")
    else:
        print("Nem szabályos háromszög.")
else:
    print("Ez nem háromszög (nem teljesül a háromszög-egyenlőtlenség).")


#HF: Ciklusok-Loops-Íterációk nezz utana

#Generaljon 3 veletlen 3 jegyu szamot amelyek 13 al oszhatok
# Allitsa ezeket sorrendbe
# adja meg az atlaguk
# Van-e kozottunk 4 el vegzodo
 
import math
import random 

szam3 = random.randint(100,999)
szam4 = random.randint(100,999)
szam5 = random.randint(100,999)

#Otthon másold le 
#Házifeladat elkészítése
#add, commit , push

import math
import random

a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("Adjon meg egy számjegyet:"))

print(a,b,c)

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy ):
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("nincs közte "+str(szamjegy)+"-re végződő")




