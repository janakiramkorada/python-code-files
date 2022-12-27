def place_value(str1,n):
    for i in range(0,len(str1)):
        if(n<=len(str1)):
            print(str1[n])
            break
        else:
            print("Index out of range")
            break
s=input()
n=int(input())
place_value(s,n)