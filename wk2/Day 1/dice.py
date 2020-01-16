#rolling dice

import random

def roll_die():
    return random.randint(1,6)

# def roll_die(highest_num):
#     return random.randint(1,highest_num)

# NOTE: My Attempt at rolling a die
# def gamble(n):
#     One=0
#     Two=0
#     Three=0
#     Four=0
#     Five=0
#     Six=0
#     exp=0
#     dice_max=6

#     for exp in range(0,n):
#         if roll_die(dice_max)==1:
#             One+=1
#         elif roll_die(dice_max)==2:
#             Two+=1
#         elif roll_die(dice_max)==3:
#             Three+=1
#         elif roll_die(dice_max)==4:
#             Four+=1
#         elif roll_die(dice_max)==5:
#             Five+=1
#         else:
#             Six+=1

# print(f"probability of 1 = {(One/n)*100}%")
# print(f"probability of 2 = {(Two/n)*100}%")
# print(f"probability of 3 = {(Three/n)*100}%")
# print(f"probability of 4 = {(Four/n)*100}%")
# print(f"probability of 5 = {(Five/n)*100}%")
# print(f"probability of 6 = {(Six/n)*100}%")

def monte_carlo_with_lists(N,dice_max=6):
    results=[]

    for exp in range(0,N):
        results.append(roll_die(dice_max))
    
    print("{N} experiments were performed")
    for outcome in range(1,dice_max+1):
        results.count(outcome)
        msg=f"The probability of {outcome}={(count/N)*100}"
        print(msg)

monte_carlo_with_lists(10000)