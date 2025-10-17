for i in range(0,11):
    print(i*2)# i je proměná číslo v závorce říká kolikrát dokola
    print("ahoj") # i je 0,1,2,3,4  range(n) dá mi čísla zas i<0;n)
    # 3 parametry <a,n,s) jde od a do n po s např s=2 skáče po dvou
for i in range(0,11,2):
    print(i)
for i in range(0,6):
    print(i*2)

for i in range(0,11):
    if i%2==0:
        print(i)

for i in range(5):
    for j in range(5):
        print(str(i) + "," + str(j)) #vnořeno nejdříve se vypíše max hodnot j a pak se i posune o jedno o znovu

a=0
while a == 0: #hrozí nekonečné smyčky vstup od uživatele pokud nedá číslo jde na nulu takže bude zadávat znova
    x = input("napis cislo: ") # while cykus neustále zjišťuje skutečnost
    try:
        a = int(x)
    except:
        a = 0
print(a)


for i in range(10):
    print(i)
    if i>5:
        continue # když se dostane sem ukončí se forcyklus a jde znovu pokud je podmínka splněná
    print("ahoj")

for i in range(10):
    print(i)
    if i>5:
        break # okamžitě ukončuje forcyklus a nebude se dodělávat zbytek
    print("ahoj")
#continue dělá to že se nepokračuje v prosece a jede znova break vše rovnou ukončí, fungují uvnitř whilecyklu i forcyklu


while True: #je to dobré ale nebezpečné jelikož běží do nekonečna
    x = input("napis cislo: ")
    try:
        a = int(x) #když se tohle povede vypadnu z cyklu dostanu se do break a mam a
        break
    except:
        pass #pass nedělá nic
print(a)