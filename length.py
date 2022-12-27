def length(str1):
    print(len(str1))
    x=len(s)
    for i in range(0,len(str1)):
        if str1[i]==" ":
            x-=1
    return x
s=input()
print(length(s))