import random

gondolt_szam = random.randint(10,99)

print("Melyik kétjegyű számra gondoltam?")
szam = int(input("Szám: "))
probalkozasok = 1

probalkozasok += 1
while(szam != gondolt_szam):
    if(szam > 9 and gondolt_szam < 100):
        if (szam > gondolt szam):
            print("A szám nagyobb mint a gondolt szám.")
    elif(szam < gondolt_szam):
        print("A szám kisebb mint a gondolt szám.")
    else:
        print("Eltaláltad")
    szam = int(input("Próbálkozz még egyszer: "))


print

# Írassa ki hány darab próbálkozás volt!
# Figyeljen arra, hogyha nem kétjegyű számot adott meg, az ne legyen új próbálkozás, és figyelmeztesse a felhasználót!
# Minden szám bekérésénél írja, ki az aktuális próbálkozások számát!