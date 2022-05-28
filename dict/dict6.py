#python program to replace a given key value pair in a dictionary
a={}
size=int(input("enter size"))
for i in range(0,size):
    x=input("enter key")
    y=input("enter value")
    a[x]=y
b=input("enter key to be replaced")
c=input("enter new key")
d=input("enter new value")
if b in a:
    a.pop(b)
    a[c]=d
else:
    print("key not found")
print(a)