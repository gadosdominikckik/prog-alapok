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
# 1-10 ig szamok kiiratasa
for elem in range(1,11,1):
    print(elem,end=" ")

print( )
# Első 10 db páros szám

for paros in range(0,19,2):
    print(paros,end=" ")


# szöveg betűi közé vesszöt
szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter,sep="\nn")

# pdf 14.-16. feladat