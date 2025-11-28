# Kerjen be egy szöveget es egy betut
#adja meg hany darab betu van a szovegben

szoveg = input("Adjon meg egy szöveget : ")
print()
betu = input(" Adjon meg egy betűt : ")
print()

index = 0
while(index < len(szoveg) and szoveg[index] != betu):
    index += 1
print(index)


db = 0
for karakter in szoveg:
    if(karakter == betu):
        db+=1
print(db)

