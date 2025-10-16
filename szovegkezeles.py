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

