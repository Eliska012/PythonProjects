#vypište jednotlivéznaky pod sebe pomocí forcyklu
promenna = "Ahoj Karle, jak se máš?"
for i in range(len(promenna)):
    print(promenna[i])

# totež pozpátku
for i in range(len(promenna)):
    print(promenna[-i-1])

for i in range(len(promenna)-1,-1,-1):
    print(promenna[i])

#vypsat postupně po  rádcích +1 písmeno pyramidu
for i in range(len(promenna)):
    print(promenna[:i+1])

#odsazení po dvou písmenech na řádek
for i in range(len(promenna)-1):
    print(promenna[i:i+2])

# upravte předchozí aby psal 3 písmenka
for i in range(len(promenna)-2):
    print(promenna[i:i+3])

# vypište vedle sebe první a poslední písmenka vždy pak, druhy a předposlední,... koncime v polovině textu
for i in range(int(len(promenna)/2+1)):
    print(promenna[i],promenna[-i-1])

#zahození desetiných
print(int(5.9))