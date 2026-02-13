vstup = input("zadej cislo:")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup =" + vstup)

if cislo > 10:
    print("cislo vetsi nez 10")
elif cislo < 20:
        print("a zaroven mensi nez 20")
else:
    print ("mensi nez 20")

if cislo >10:
    print("cislo vetsi nez 10")
if cislo%2 == 0: #zjistuje delitelnost dvema tedy sudost
    print("cislo sude")
else: # kdyz nespadne do podmínky předtím
    print("cislo je liche")
if cislo >10 and cislo < 20:
    print("cislo je vetsi nez 10 ale mensi nez 20")
