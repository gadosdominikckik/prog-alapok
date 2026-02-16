import math
def prime(szam):
    a = 2
    b = math.sqrt(szam)
    while(a<b and szam % a != 0):
        a+=1
    return a>=math.sqrt(szam)




def LNKO(szam1,szam2):
    kisebb = szam1
    if(szam1>szam2):
        kisebb = szam2
    while(kisebb>=1 and not (szam1 % kisebb == 0 and szam2 % kisebb == 0)):
        kisebb-=1
    return kisebb
    


def main():

    a = 50
    b = 25
    # for i in range(2,100000,1):
    #     if prime(i):
    #         print(i)
    print(prime(a))
    print(LNKO(a,b))

main()