# define a function which counts the vowels and consoents in a word
def count(val):
    v=0
    c=0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u','A','E','I','O','U']:
            v=v+1
        else:
            c=c+1
    print("count of vowels is",v)
    print("count of consoments is",c)
val = input("enetr the word")
count(val)
