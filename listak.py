"""
lista - dinamikus
-tudunk bele új elemet raskni , ezzel nő az elemszáma
-tudunk belöle törölni ezzel csokken az elemszama
-lekerheto barmelyik eleme
-modosithato barmelyik eleme
deklarálás:
lista_neve = []
új elem h.adása
lista_neve.append(újelem)
beégetett lista:
lista_neve = [3,2,5,7,1]
len(lista_neve)
"""

szamok = [3,2,5,7,1]

print(szamok)
print("lista hossza: ",len(szamok))
print("elso elem: ",szamok[0])
print("utolso elem: ", szamok[len(szamok)-1])