# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki.
#  Mivel minden autó végsebessége 3 jegyű, ezért megnézik a középső számot. 
# Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
import random
import math

lista = []
for i in range(0,30,1):

    elso = random.randint(3,4)
    masodik = -1
    if ( i % 2 == 1):
        masodik = random.randint(0,4)*2
    else:
        masodik = random.randint(0,4)*2+1
    harmadik = random.randint(0,9)
    vseb = random.randint(300,499)
    szam = int(str(elso)+str(masodik)+str(harmadik))
    lista.append(szam)
print(lista)

osszeg = 0
for i in range(1,len(lista),2):
    print(lista[i])
    osszeg += lista[i]


db = len(lista)/2
atlag = osszeg / db
print("Jancsi autóinak vésebességének átlaga: ", round(atlag,2))

# vseb = 380
# for vseb in range(0,len(lista),1):
#     if(len(lista) > vseb):
#         vseb += 1
#         print(vseb)

db_juliska = 0
for i in range(0,len(lista),2):
    if(lista[i] > 380):
        db_juliska += 1
print("Juliskának ennyi autója gyorsabb 380-nál: ")
        


# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [300, 499] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!


