#python program to remove duplicates from dictionary
a={}
size=int(input("enter size"))
for i in range(0,size):
    x=input("enter key")
    y=input("enter value")
    a[x]=y
print("original dict:", a)
new={}
for i,j in a.items():
    if j not in new.values():
        new[i]=j
print("new dictionary : ",new)