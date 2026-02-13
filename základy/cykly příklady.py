# napiste cyklus, ktery vypise cisla od 5 do 8 (vcetne)
for i in range(5,9):
    print(i)

# napiste program, ktery vypise cisla od 10 do 5
for j in range(10,4,-1):
    print(j)

# napis program ktery vypise suda cisla od 5 do 11
for k in range(2,6):
    print(k*2)
for k in range(5,11,2):
    print(k)
for k in range(5,11):
    if k%2==0:
        print(k)

# napiste program ktery secte cisla od 5 do 11
for l in range(5,12):
    for m in range(5,12):
        print(m+l)
soucet = 0
for i in range(5,12):
    soucet = soucet + i # soucet = soucet + 1
print(soucet)

#