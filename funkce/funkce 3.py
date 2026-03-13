from funkce.soucet_cisel import soucet


def funkce(a, b, c):
    return a+b+c

print(funkce(2,3,4))

def jina(a,b,c=10,d=10):
    return a+b+c+d

print(jina(1,2))
print(jina(1,2,3,))
print(jina(1,2,3,4))
print(jina(1,2,d=5))

def jin (*args):
    soucet = 0
    for i in range (len(args)):
        soucet +=args[i]
    return soucet

print(jin(1,2,3,4))
print(jin(1,2))
print(jin(1,2,3,4,5,6,7,8))