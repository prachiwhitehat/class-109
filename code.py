import random
import statistics

dice_result=[]

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    result=dice1+dice2
    dice_result.append(result)

mean= sum(dice_result) / len(dice_result)

print("The mean is ", mean)

median= statistics.median(dice_result)
print(median)

mode = statistics.mode(dice_result)
print(mode)