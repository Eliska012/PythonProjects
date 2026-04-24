import random

x = random.randint(10,20)
print(x)

y = random.randint(1,6)
print(y)

def hod_k6():
    z = random.randint(1, 6)
    return z

print(hod_k6())

def pokus():
    pokus = 1
    hod = hod_k6()
    while hod !=6:
        pokus += 1
        hod = hod_k6()
    return pokus
print(pokus())

def nez_padne(n):
    vysledky = [0]*20

    for i in range(n):
        pokusy = pokus()
        if pokusy <= 20:
            vysledky[pokusy-1]+=1
    return vysledky
print(nez_padne(100))
print(nez_padne(50))