# egy szovegben hany darab szokoz van?

szoveg = "Géza kék az ég"

db = 0

for karakter in szoveg:
    if(karakter == " "):
        db += 1

print(db, "db szóköz van a szövegben")

sz = input("Adjon meg egy szöveget: ")
index = 0
while(index<len(sz)-1 and not (sz[index] == "c" and sz[index+1] =="s")):
    index += 1

print(index)
if(index <len(sz)-1):
    print("Van benne cs")
else:
    print("nincs benne cs")