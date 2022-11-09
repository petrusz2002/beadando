import random
a = random.randint(1,100)
def osszehas (a):
    if a ==100:
        print("Legenerálta a legnagyobb lehetséges számot! A szám: ",a)
    elif a <100  and a >=50:
        print("A legenerált szám 50 és 100 között van! A szám: ",a)
    else:
        print("A legenerált szám kisebb mint 50! A szám: ",a)
osszehas(a)
