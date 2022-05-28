#to delete a key value pair by key
d={'name': 'kirti', 'branch': 'cs', 'sec': 'a'}
n=input("enter the key")
if n in d.keys():
    d.pop(n)
print(d)