#program in python to raise an exception during the runtime of the program
l=int(input())
u=int(input())
for i in range(l,u+1):
    a = i
    for j in (2,a/2):
        if a%j!=0:
            raise Exception ('prime exception')