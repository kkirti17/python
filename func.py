# define a function that accepts roll number and returns whether the student is present or not
def detail(roll):
    x=[1,23,33,43,44]
    if roll in x:
        print(f"roll number {roll} is present")
    else:
        print(f"roll number {roll} is absent")
roll = int(input("enter roll number"))
detail(roll)