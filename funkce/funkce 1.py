def scitani(a, b):
    return a+b

def secteni(a, b):
    reseni = a+b
    return reseni

def napis_ahoj():
    print ("Ahoj")

def secti_a_vypis(a,b):
    print(a+b)
x = 5
y = 10
vysledek = scitani(x,y)
print(vysledek)
napis_ahoj()
neco = napis_ahoj()
print(neco)

print("**********")
pejsek = secti_a_vypis(4,5)  #tyto proměné jen ve fumkci nelze vidět jinde
print(pejsek)