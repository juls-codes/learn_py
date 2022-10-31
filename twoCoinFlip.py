#Date created: October 27, 2022
#Program for flipping two coins

import random
heads_tails = 0
two_heads = 0
two_tails = 0

number_of_flips = int(input("How many times should we flip?: "))

for x in range (1,number_of_flips+1):
    coinA_result = random.randint(0,1)
    coinB_result = random.randint(0,1)
    flip_result = (coinA_result, coinB_result)
    if (flip_result == (1,0) or flip_result == (0,1)):
        heads_tails += 1
    elif flip_result == (0,0):
        two_heads += 1
    else:
        two_tails += 1

comboDict = {"1H1T":heads_tails, "2H":two_heads, "2T":two_tails}

for combo in comboDict:
    print(combo, ":", comboDict[combo])
