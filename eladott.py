def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(' ')
        lista.append((int(st[0]), int(st[1]), int(st[2])))
    return lista

def main():
    adatok = listaFeltoltes()
    print(adatok)
    

main()

