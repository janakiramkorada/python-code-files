import math
def armstrong(num):
    sum = 0
    while(num>0):
        sum = sum+math.factorial(num%10)
        num = num//10
    return sum
n=eval(input())
for i in range(1,n+1):
    if i==armstrong(i):
        print(i-1, end=" ")