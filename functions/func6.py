def count(word):
    d={"upper_case":0,"lower_case":0}
    for c in word:
        if c.isupper():
            d["upper_case"]+=1
        elif c.islower():
            d["lower_case"]+=1
    print("original string : ",word)
    print("no. of upper case characters : ",d["upper_case"])
    print("no. of lower case characters : ",d["lower_case"])
word=input("enter the string")
count(word)