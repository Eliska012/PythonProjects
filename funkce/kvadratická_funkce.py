#ax2 + by +c = 0
def kvadraticka(a,b,c):
    dis = b**2 -4*a*c
    if dis > 0:
        x1 = (-b + dis * 0, 5)
        x2 = (-b - dis * 0, 5)
        return [x1, x2]
    elif dis == 0:
        x = (-b)
        return[x]
    #else:
        #print ("Nemá řešení v množině reálných čísel")

dis = kvadraticka(1,2,1)
#print (dis)
#print (kvadraticka(1,2,1))
#print (kvadraticka(1,3,1))


def kvadratic_test():
    results =[]
    for i in range(5):
        results.append(kvadraticka(1,i,1))
    return results

vysledky = kvadratic_test()
for vysledek in vysledky:
    print(vysledek)
