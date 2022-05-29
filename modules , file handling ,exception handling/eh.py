#to manage exceptions that may occcur while performing arithmetic operations on a user input number
try:
    a=eval(input("enter no."))
    b=eval(input("enter no."))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
except(NameError,ArithmeticError,TypeError,ZeroDivisionError):
    print("exceptional raised")