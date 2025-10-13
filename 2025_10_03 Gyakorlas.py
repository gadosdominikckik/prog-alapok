# Generálj ki egy páros véletlen számot [-10, 10] között!
# Írasd ki az adott számot!

import random 
import math
a = random.randint(-5,5)*2
print("szám: "+ str(a))

# vegyük a szám abszolut értékét!
# ha a szám negatív akkor szám*(-1) különben önmaga
if a<0 :
    print("abs: "+str(a*(-1)))
else:
    print("abs: "+str(a))


if(a >= 0 ):
    print("gyök(a): "+str(math.sqrt(a)))
else:
    print("A negatív számnak nincs gyöke.")

# döntse el a számról, hogy pozitív, negatív vagy nulla

if(a>0):
    print("pozitív")
else:
    if(a==0):
        print("nulla")
    else:
        print("negatív")


if(a>0):
    print("pozitív")
elif(a==0):
    print("nulla")
else:
    print("negatív")



szoveg = input("Adjon meg egy számot: ")
print(szoveg)

sec = 3923

ora = sec // 3600
perc = (sec - ora *3600) // 60
mp = (sec-ora *3600)-(perc *60)
print(ora,"óra")
print(perc,"perc")
print(mp,"másodperc")