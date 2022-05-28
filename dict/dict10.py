
a={}
size=int(input("enter size"))
for i in range(0,size):
    x=input("enter key")
    y=int(input("enter value"))
    a[x]=y
print(a)
ans=1
for i in a:
    ans=ans*a[i]
print(ans)
