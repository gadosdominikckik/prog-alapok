"""
Ciklusok - ismétlés - loop

számlálás - for ciklus
végig megy a megadoot intervallumon!
for elem in range(mettol, meddig, hányasával):
    Ismétlődő folyamat


for karakter in szoveg:
    ismétlődő folyamat

Tesztelős - While

"""

import random as r

# 1-10 ig szamok kiiratasa
for elem in range(1,11,1):
    print(elem,end=" ")

print( )
# Első 10 db páros szám

for paros in range(0,19,2):
    print(paros,end=" ")
print()

# szöveg betűi közé vesszöt
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter,end=",")
print()


for index in range(0 , len(szoveg)-1,1):
    print(szoveg[index]+",",end="")
print(szoveg[-1])


#Visszafele
for index in range(len(szoveg)-1,-1,-1):
    print(szoveg[index],end="")
print()


# pdf 14.-16. feladat

for negy in range(32,51,4):
    print(negy)
print()

for csokk in range(10,0,-1):
    print(csokk,end=" ")





#irassa ki a kalapacs szot be kalapacs ki 1k 2a 3l 4a 5p 6a 7c 8s


n = len(szoveg)

szoveg = "kalapács"
index = "kalapács"

for index in range(0,n,1):
    print(str(index+1)+szoveg[index],end=" ")


for db in range(0,5,1):
    szam = r.randint(0,n-1)
    print(szoveg[szam],end=" ")
print()

#HF 17-21

#ujra felhasznalas

ujra += szoveg[index]
print()