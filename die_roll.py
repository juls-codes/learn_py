#Date created: October 11, 2022
#Program for rolling a die

import random

roll1 = 0
roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
roll6 = 0

numberOfRolls = int(input("How many times should we roll?: "))
for x in range(1,numberOfRolls+1):
    numberRolled = random.randint(1,6)
    if (numberRolled == 1):
        roll1 += 1
    elif (numberRolled == 2):
        roll2 += 1
    elif (numberRolled == 3):
        roll3 += 1
    elif (numberRolled == 4):
        roll4 += 1
    elif (numberRolled == 5):
        roll5 += 1
    else:
        roll6 += 1
    
print(f"Number of times 1 is rolled: {roll1}")
print(f"Number of times 2 is rolled: {roll2}")
print(f"Number of times 3 is rolled: {roll3}")
print(f"Number of times 4 is rolled: {roll4}")
print(f"Number of times 5 is rolled: {roll5}")
print(f"Number of times 6 is rolled: {roll6}")
