#to print words of a file in list format
file=open('kirtiiii.txt','w')
file.write("my name is kirti bhardwaj hello")
c=0
with open("kirtiiii.txt",'r') as file:
    line=file.readlines()
    for i in line:
        word=i.split()
    print(word)