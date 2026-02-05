import random

def karytagen():
    lista = []
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista

def keveres(pakli):
    for i in range(500):
        a = random.randint(0,len(pakli)-1)
        b = random.randint(0,51)
        sv = pakli[a]
        pakli[a] = pakli[b]
        pakli[b] = sv

def lapindex(lap, pakli):
    index = 0
    while( pakli[index] != lap):
        index+=1
    return index


def main():
    pakli = karytagen()
    # print(pakli)
    keveres(pakli)
    print(pakli)
    lap = input("Adjon meg egy lapot - t, p , s, k +[1,13] pl(p1): ")
    index = lapindex('P13', pakli)
    print(index)


main()