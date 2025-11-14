pole = [5,2,9,1,7,3,10,6,4]

# najdi maximum
maximalni_prvek = pole[0] # nastavim dosavadní nalezené maximum
pozice_max_prvku = 0 # nastaví pozici maximálního prvku na index 0

for i in range(1,len(pole)):#0. prvek je již nastaven - zacnu tedy
    if maximalni_prvek < pole[i]: #pokud je i-ty prvek vetsi nez dosavadní
        maximalni_prvek = pole[i] # nastavim maximum na i-ty prvek
        pozice_max_prvku = i # a pozici největšího prvku na i
print(maximalni_prvek)
print(pozice_max_prvku)

#najdi minimum
minimalni_prvek = pole[0] # nastavim dosavadní nalezené minimum
pozice_min_prvku = 0 # nastavím pozici minimálního prvke na index 0
for i in range(1,len(pole)):#0. prvek je již nastaven - zacnu tedy
    if minimalni_prvek > pole[i]: #pokud je i-ty prvek menší nez dosavadní
        minimalni_prvek = pole[i] # nastavim minimum na i-ty prvek
        pozice_min_prvku = i # a pozici nejmenšího prvku na i
print(minimalni_prvek)
print(pozice_min_prvku)

# spočítej průměr prvků v poli
soucet = 0
for i in range (len(pole)):
    soucet = soucet + pole[i] # soucet += pole[i]

print(soucet/len(pole))

# kolik prvků v poli je větší než 5
limit = 5
pocitani = 0
for i in range(len(pole)):
    if pole[i] > limit:
        pocitani += 1
print("Pocet prvku vetsich nez " +str(limit)+" je: " +str(pocitani))

# součet všech prvků
pocitani = 0
for i in range (len(pole)):
    pocitani = pocitani + pole[i]
print(pocitani)

# obrácení pole
pole = [5,2,9,1,7,3,10,6,4]
nove_pole[]
for i in range (len(pole)-1, -1, -1):
    nove_pole.append(pole[i])
print(nove_pole)