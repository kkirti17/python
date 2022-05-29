#python program to get the same number on the dice
import random
dice=[1,2,3,4,5,6]
print("randomly selecting the number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))
