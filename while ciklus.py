import random

"""""

Elöl tesztelős ciklus
while ciklus

- Nem tudjuk hanyszor fog lefutni
- Feltételhez kötött
- Akkor ismétel ha feltétel igaz

while(feltétel):
    utasítások
"""""
# Generáljon véletlen számokat [0,10] között, amíg 0 nem mutat.

vszam = random.randint(0,10)
print(vszam)
while(vszam != 0):
    vszam = random.randint(0,10)
    print(vszam,end=" ")


osszeg = 0
db = 0
szam = int(input("Adjon meg egy számot:"))

while(szam != 0):
    osszeg +=szam
    db += 1
    szam = int(input("Adjon meg egy számot:"))
print(round(osszeg/db,2))


szoveg =  lkjméáűxysxdecgvhjnklőpéolihkugfd5dtucgjbm 

while(szoveg != x):
    print(szoveg)


