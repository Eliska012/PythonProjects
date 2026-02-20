def soucet(n):
    souc = 0
    for i in range(n+1):
        souc = souc +i

    return souc
print(soucet(6))

def soucet_rekuzre(n):
    if n <=1:
        return 1
    else:
        return n + soucet_rekuzre(n-1)
print(soucet_rekuzre(6))