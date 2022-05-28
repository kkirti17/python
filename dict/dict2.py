#to delete an item by value
d={'name': 'kirti', 'branch': 'cs', 'sec': 'a'}
b={}
n=input("enter the value")
for i,j in d.items():
    if(n!=j):
        b[i]=j
print(b)