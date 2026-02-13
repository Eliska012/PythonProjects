promenna = [1, 2, 3, 4, 5]
print(promenna)

p2 = [1, "abc", 5.5, True, [1,2,"a"]]
print (type(p2))
print(p2) # vytiskne prvky pole
print(type(p2[2])) # vypíše 2 typ prvku, orientruje se podle čísla v závorce
print(p2)# typ prvku vypíše je to list jelikož pole
print(p2[3]) # vypíše 3 prvek z pole orientuje se podle čísla v závorce
print(p2[4][1])
print(type(p2[4][1]))
print(p2[1:3])# vypíše první tři znaky ne nultej
print (p2[1:4]) # ukrojení kousku pole vrátí pole
print(p2[2:3]) #vrací hodnotu
print(type(p2[2:3]))
print(p2[7]) # pokud větší než počet indexů v listech vyhodí eror

x = [1, 2, 8, 4, 6, 11, 7, 4]

for i in range(len(x)): # vypíše prvky pole
    print(x[i])

for i in range(len(x)): # vypíše jen sudé pozice
    if i%2 == 0:
        print(x[i])

for i in range(0, len(x), 2): #jde po dvou
    print(x[i])

for i in range(int(len(x)/2)): # vypíše jen sudé pozice
    print(x[i*2])

