#mějte dvě pole se stejným počtem prvků vytvořte třetí pole které bude obsahovat součty odpovídajících prvků
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
pole_vysledne = []
x = 0
for i in range(len(pole)):
    x = pole[i] + pole2[i]
    pole_vysledne.append(x)
print(pole_vysledne)

#napište to samé jen aby pole šli obráceně
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
pole_vysledne = []
x = 0
for i in range(len(pole)):
    x = pole[-i-1] + pole2[i]
    pole_vysledne.append(x)
print(pole_vysledne)

#najděte druhý největší prvek v poli
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
maximalni_prvek = float('-inf')
druhy = float('-inf')
for i in range (len(pole)):
    if pole[i] > maximalni_prvek:
        druhy = maximalni_prvek
        maximalni_prvek = pole[i]
    elif pole[i] > druhy:
        druhy = pole[i]
print(druhy)

#zjistěte zda je pole seřazené vzestupně nebo není
pole = [5, 2, 9 ,1 ,7 ,3, 10, 6, 4]
je = True
for i in range (len(pole)-1):
    if pole[i] > pole[i+1]:
        je = False
        break
if je:
    print("je")
else:
    print("není")


# počet sudých a počet lichých čísel
pole = [5, 2, 9 ,1 ,7 ,3, 10, 6, 4]
sude = 0
liche = 0
for i in range (len(pole)):
    if pole[i] %2 == 0:
        sude +=1
    else:
        liche += 1
print(sude)
print(liche)