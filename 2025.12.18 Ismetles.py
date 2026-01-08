"""

Utasítás (szekvencia)
- menj előre
- fordulj
- szívd be a levegőt
- fújd ki a levegőt...

- írasd ki(print)
-tárold el(változónév=érték)
-kérd be(input)
-számold ki - változónév = <képlet>

Elágazés - (szelekció)
- ha piros a lámpa akkor megállok
- ha zöld a lámpa elindulok
-ha fal van előttem elfordulok
- ha nem megy akkor gyakorlom
-....
- ha a bekért számom páros, akkor kiíratom hogy páros, különben kiiratom hogy páratlan
- ha a dobókocka értéke 5 akkor előrelépek 5-öt

ismétlés ciklus iteráció
- addig menju amíg a tábla van
-addig dobáld az aprot ameddig el nem éred a megfelelő összeget
-addig tegyel bele cukrot, amig eleg edes nem lesz
- addig gyakorlom amig meg nem ertem
- addig fog a tanar piszkalni amig nem latja hoogy ertem 
"""


db = 12
print("szám", db)


# a szam utolso szamjegye paros e?
utolso_szamjegy = db % 10
print("utolsó számjegy:", utolso_szamjegy)

# db nyi almát irasson ki

for kiskutya in range(0, db, 1):
    print(kiskutya+1,"Alma")


szoveg = "kalapács"
print(szoveg)
for karakter in szoveg:
    print(karakter)