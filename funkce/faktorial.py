def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))

def odpocet(n):
    if n <= 0:
        print("Konec")
        return
    print(n)
    odpocet(n-1)
odpocet(5)

def start(n):
    if n<=0:
        print("bum")
        return
    else:
        print("odpocet T - " + str(n))
        start(n-1)
start(7)
