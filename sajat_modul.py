def osszehas(a,b):
    if a < b:
        print("B nagybobb mint A")
    elif b < a:
        print("A nagybobb mint B")
    else:
        print("A két szám egyenlő")
        print("Mind a két szám ugyan akkora távolságra van")
    if (50-b) < (50-a):
        print("B közelebb van az 50-hez")
    elif (50-b) > (50-a):
        print("A közelebb van az 50-hez")

print("Kérek egy számot: ")
szam1 = int(input())
print("Kérek még egy számot: ")
szam2 = int(input())

oszsehas(szam1,szam2)