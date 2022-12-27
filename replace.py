def replace(str,chr,ind):
    if ind>=len(str):
        print("Index out of range")
    else:
        x=""
        x+=str[0:ind]
        x+=char
        x+=str[ind+1:]
        print(x)
a=input()
s=input()
b=int(input())
replace(a,s,b)