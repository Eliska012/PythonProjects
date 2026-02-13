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
    else:
        print ("Nemá řešení v množině reálných čísel")

dis = kvadraticka(1,2,1)
print (dis)
