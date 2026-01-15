"""
Függyvények
(scratch blokkok)

Előre definiált , megírt , megfogalmazott folyamatok , amik külső értéktől függően végrehajthatják,
a belső utasításokat!
def fuggvenyNev():
    #fuggveny tartalma

fuggvenyNev() # fuggveny meghivasa

"""
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

