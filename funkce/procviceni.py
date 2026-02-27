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

# ověřte zda je číslo jako prvočíslo vstup: cislo vystup: logicka promena true/false

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