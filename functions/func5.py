#python program to reverse a string
def reverse(str):
    str1=''
    for i in str:
        str1=i+str1
    return str1
str=input("enter the string")
print(reverse(str))