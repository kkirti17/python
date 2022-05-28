#program to create a user defined dictionary
a={}
size=int(input("enter size"))
for i in range(0,size):
    x=input("enter key")
    y=input("enter value")
    a[x]=y
print(a)
