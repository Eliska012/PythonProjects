vstup = input("zadej cislo:")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup =" + vstup)

if cislo > 5:
    print("vetsi")
    print(cislo)
    print("je")
    print("vetsi nez 5")
    if cislo > 10:
        print("neco")
else:
    print("neni vetsi nez 5")
if cislo < 7:
        print("cislo je mensi nez 7")
print("konec")

a = int(("zadej A"))
b = int(("zadej B"))
c = int ("zadej C")

reseni = b**2 -4*a*b
if reseni < 0:
    print("nula reseni")
elif reseni == 0:
    print("jedno reseni")
else:
    print("dve reseni")
