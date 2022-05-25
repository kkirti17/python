# define a funtion that returns factorial of a number
def fact(num):
    f=1
    while num>0:
        f=f*num
        num=num-1
    print(f)
num=int(input("enter a no."))
fact(num)