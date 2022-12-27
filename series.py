import math
def factorial(n,x):
    s=1
    for i in range(1,n+1):
        s=s+x**3/math.fatorial(i)
    print("{0:.2f}".format(s))
n=int(input("n: "))
x=int(input("x: "))
factorial(n,x)
