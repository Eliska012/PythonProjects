import numpy as np

for i in range(10):
    cislo = np.random.randint(10, 20)
    rnd = np.random.random()
    print(cislo)
    print(rnd)

cislo = np.random.randint(0, 21)
while True:
    x = int(input("Zadej tip: "))
    try:
        a = int(x)
    except:
        pass
        print("Zadej číslo")
    if x < cislo:
        print("moc malé")
    elif x > cislo:
        print("moc velké")
    else:
        print("správně")
        break