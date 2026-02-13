cislo_jako_text = input("Zadej cislo: ")

try:
    cislo = int(cislo_jako_text)
except:
    cislo = 0
print("zadane cislo + 10 = " + str(cislo + 10))

#aby zadával dokud nezadá číslo pořád dokola mu bude vyhazovat ať zadá

a = 0
while a == 0:
    x = input("napis cislo: ")
    try:
        a = int(x)
    except:
        a = 0
print(a)

while True:
    x = input("napis cislo: ")
    try:
        a = int(x)
        break
    except:
        pass
print(a)