# wap in python to find the si on agiven principle & time, where the rate is defined by the user.
def si(rate):
    si=(1000*5*rate)/100
    print(si)
rate=float(input("enter rate"))
si(rate)