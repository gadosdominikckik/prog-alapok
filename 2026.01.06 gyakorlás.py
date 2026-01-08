#Generáljon egy listában 13 db olyan négyjegyű véletlen számot amelyek 3 ra 5 re és 7 re végződnek.
# Hány darab 3ra , 5 re , 7re , végződő szám van

import random


lista = []

for i in range(0,13,1):
    szam = random.randint(100,999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(szam*10+3)
    elif(veletlen == 2):
        lista.append(szam*10+5)
    else:
        lista.append(szam*10+7)
    lista.append(szam)
print(lista)

haromra = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 3):
        haromra += 1
print(haromra)

ötre = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 5):
        ötre += 1
print(ötre)

hétre = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 7):
        hétre += 1
print(hétre)
