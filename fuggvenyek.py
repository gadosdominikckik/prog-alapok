"""
Függyvények
(scratch blokkok)

Előre definiált , megírt , megfogalmazott folyamatok , amik külső értéktől függően végrehajthatják,
a belső utasításokat!
def fuggvenyNev():
    #fuggveny tartalma

fuggvenyNev() # fuggveny meghivasa

"""
import random
# VISSZATÉRÉSI ÉRTÉK NÉLKÜLI FÜGGVÉNYEK - ELJÁRÁS
# Általában kiiratásnál használjuk
#összeadas fuggveny definialasa
def osszeadas():
    a = 12
    b = 17
    print(a+b)

# összeadás külső értéken paraméteren keresztül
def osszeadasparam(a,b):
    c = a + b
    print(c)

# fuggveny meghivasa 
osszeadas()
valami = osszeadasparam(18,13)
print(valami)
# Visszatéréssel nem rendelkező függvény - Csak futtathato , nem hasznalhato vegeredmeny - Eljárás

# Visszatéréssel rendelkező függvényekű - Hasznalhato vegtermek 
def kettoatizediken():
    # a = math.pow(2,10)
    a = 2**10
    return a

valtozo = kettoatizediken()
print(valtozo)

def osszeadasvisszateressel(a,b):
    c = a + b
    return c

print(osszeadasvisszateressel(13,17))
print(osszeadasvisszateressel(1,2012))

#feladat pdf 38

def veletlenszamkiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999),end = " ")
    print()
veletlenszamkiiratas(5)


def szovegvisszafele(szoveg):
    visszaSzoveg = ""
    for i in range(len(szoveg)-1,-1,-1):
        visszaSzoveg += szoveg[1]
        return visszaSzoveg
    print()


print(szovegvisszafele("kalapács"))

# Írjon egy fv-t ami egy szóról eldönti h palindrom - e és visszaadja vélaszul.

def palindrome(szo):
    if(szo == szovegvisszafele(szo)):
        return True
    else:
        return False

print("palindrom-e a szó: " , palindrome("abadba"))


    # int(input(" Gépeljen be egy szót "))
    # for i in range(0,len(sz),1):
    #     if(sz == sz):
    #         print(" A szó palindrom")
    #     else:
    #         print(" A szó nem palindrom")

