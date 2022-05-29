#python code to create a file
file=open('python.txt','w')
file.write("hello world")
file.write("this is a python program")
with open("file.txt","r")as file:
    print(file)
file.close()