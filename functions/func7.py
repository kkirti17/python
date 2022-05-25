def perfect_number(n):
 sum = 0
 for i in range(1, n):
    if n % i == 0:
      sum=sum+i
 if sum == n:
    print("perfect_number")
 else:
    print("not a perfect number")
n=int(input("enter a number"))
perfect_number(n)
