#python program to get the maximum and minimum value in a dictionary
a={}
size=int(input("enter size"))
for i in range(0,size):
    x=input("enter key")
    y=input("enter value")
    a[x]=y
print(a)
min_key=min(a,key=a.get)
print(a[min_key])
max_key=max(a,key=a.get)
print(a[max_key])