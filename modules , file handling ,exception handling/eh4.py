#python program to demonstrate finally
a=int(input("enter a no."))
b=int(input("enter another no."))
try:
    c=(a+b)/(a-b)
except ZeroDivisionError:
    print("a/b resulted in 0")
finally:
    print("this is always executed")