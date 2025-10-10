print("ahoj")

odpoved = input("Tohle se napíše do řádky:")

print(odpoved)
print(type(odpoved))

try:
    odpoved_jako_cislo = int(odpoved) #odpoved_jako_cislo = float(odpoved)
except:
    print("zadej cisla, nastavuju na 0")
    odpoved_jako_cislo = 0

print("ahoj" + "vole")
print(22 + odpoved_jako_cislo)
