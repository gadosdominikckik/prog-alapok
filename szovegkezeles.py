import random

# lebegőpopntos - float - tört
a = 1.25
b = float(input("adjon meg egy tizedes törtet: "))
print(b*4)

#Generáljon ki {1,10} közötti tört számot 2 tizedesjegyre
# pl:1.10, 2.30

#c = random.randint(100,999)/100
c = random.random() #[0,1[
print(round(c,2))
#hf befejezni

#szovegkezeles
szoveg = input("adjon meg egy szoveget: ")
print(szoveg)
print("szoveg hossza: ",len(szoveg)),
print("első karakger" ,szoveg[0])
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

a = chr(random.randint(97,122))
b = chr(random.randint(97,122))
c = chr(random.randint(97,122))

print(a,b,c)

#Kérje be a felhasználó keresztnevét, generáljon egy jelszót az első 3 karakterének ascii kodjanak szorzatat, ha nincs a nev 3 jegyu akkor ketto eseten legyen a hossz ertek a szorzat, egy eseten pedig a szam kobe legyen
#Alma - 65 * 108 * 109
#Co - 67 * 111 * 2
#G - 71*71 *71
