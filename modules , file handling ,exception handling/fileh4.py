#python program to count the number of words
file=open('kirtiiii.txt','w')
file.write("my name is kirti bhardwaj hello")
c=0
with open("kirtiiii.txt",'r') as file:
    line=file.readlines()
    for i in line:
        word=i.split()
    print(word)
    for j in word:
        c=c+1
    print("total no. of words are ",c)
