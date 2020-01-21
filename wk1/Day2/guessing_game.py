# So we gotta do some work..
# We need to have an array of numbers from 0 to 100 and have to let 
# the user guess. need to have some memory system to it.

import random
winning_num=random.randint(0,100)
print(winning_num)
print("Winning number+10= ",winning_num+10)
print("Winning Number-10= ",winning_num-10)
num_guesses=5
user_won= False 
guesses=[]
while num_guesses !=0 and user_won==False:
    user_guess=int(input("Enter Your guess: "))
    guesses.append(user_guess)

    if user_guess==winning_num:
        print("Hey, you won!")
        user_won=True
    else:
        num_guesses-=1
        print("Try Again!")
    if user_guess>winning_num and user_guess<=winning_num+10 or user_guess>=winning_num-10 and user_guess<winning_num:
        print("Thats Really Hot!")
    if user_guess>=winning_num+10 and user_guess<=winning_num+20 or user_guess>=winning_num-20 and user_guess<=winning_num-10:
        print("Thats Warm!")

print(guesses)



