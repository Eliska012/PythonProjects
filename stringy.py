text = "ahoj"
text2 = 'ahoooj'
#uvozovky se mohou používat jednoduché i dvojité použití nemá vliv na kód používají se podle potřeby toho co chyci napsat
text3 = 'Sean 0\' Connery'
text4 = "cesta k souboru \\ hry\\ soubor"
text5 = "ahoj \n nazdar" #\n odřádkuje řádku
print(text3)
print(text4)
print(text5)

a = "abc"
b = "pane"
print(a+b)
print(a*3)

c = "a"
for i in range(5):
    c = c + "a"
print(c)

promenna = "Ahoj Karle, jak se máš?"
print(promenna[6])   #indexování od 0 !!!
print(len(promenna))
for i in range(len(promenna)):
    print(promenna[i])
    print(promenna[len(promenna)-1])

print(promenna[5:10]) #vybírání textu z promené od 5 do 10 znaku 10 znak není včetně
print(promenna[5:10:2])#poslední 3. číslo je po kolika to jde
print(promenna[10:5:-2])#zobrazování po zpátku

print(promenna[5:])#od pátého prvku až do konce
print(promenna[:5])# od začátku do pátého prvku který není zobrazen
print(promenna[:5:-1]) # automaticky dosadí největší možné číslo
print(promenna[::-1])# jde po zpátku
print(promenna.index(","))

