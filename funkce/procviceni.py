seznam = [1, 2, 8, 4, 6, 11, 9, 4]
def druhe_nejvetsi(seznam):
    nejvetsi = seznam[0]
    druhe = seznam[0]

    for cislo in seznam:
        if cislo > nejvetsi:
            druhe = nejvetsi
            nejvetsi = cislo
        elif cislo  > druhe and cislo != nejvetsi:
            druhe = cislo
    return druhe

print(druhe_nejvetsi([1, 2, 8, 4, 6, 11, 9, 4, 12, 12]))

# ověřte zda je číslo jako prvočíslo vstup: cislo, vystup: logicka promena true/false

def prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2,cislo):
        if cislo % i == 0:
            return False
    return True
print(prvocislo(15))
print(prvocislo(51))
print(prvocislo(49))
print(prvocislo(17))
print(prvocislo(31))
print(prvocislo(109))
print(prvocislo(int(input("zadej cislo:"))))

# funkce ktera spocita prvocisla v seznamu vstup: list(seznam celych cisel), vystup: cislo(pocet prvocisel)
vstup = [2, 5, 13, 17, 20, 21]

def pocečet_prvocisel(seznam):
    pocet = 0
    for i in seznam:
        if prvocislo((i)):
            pocet += 1
    return pocet
print(pocečet_prvocisel(vstup))

def scitani(a, b):
    return a + b
def odcitani(a, b):
    return a - b
def pocitej(funkce, a, b):
    return funkce(a, b)
print("************")
print(pocitej(scitani,2, 3))
print(pocitej(odcitani, 3, 2))

zadani1 = int(input("zadej cislo:"))
zadani2 = int(input("zadej druhe cislo:"))
funkce = input("zadej funkci (+/-):")

if funkce == "+":
    print(pocitej(scitani,zadani1, zadani2))
elif funkce =="-":
    print(pocitej(odcitani, 3, 2))
else:
    print("neznama funkce")