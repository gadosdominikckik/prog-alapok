# a szovegben van sz betu?
# szoveg = "osztaly"
# dube = "cs"
# print(szoveg)
# if "sz" in szoveg:
#     print("van benne sz betu")
# else:
#     print("nincs benne sz betu")

szoveg = "gezakekazeg"
dube = "ny"
print(szoveg)

index = 0
while(index < len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index += 1
if(index<len(szoveg)-1):
    print("benne van az",dube,"betu")
else:
    print("nincs benne",dube,"betu")


#palindrom-e
ujszoveg = ""

for index in range(len(szoveg)-1,-1,-1):
    ujszoveg += szoveg[index]
if(ujszoveg == szoveg):
    print("A szoveg, palindrom")
else:
    print("A szoveg nem palindrom")


j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-j-1]):
    j+=1
if(j<len(szoveg)/2):
    print("A szoveg  nem palindrom")
else:
    print("A szoveg palindrom")