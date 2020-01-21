# import the random module
import random

winning_num=random.randint(0,10)
print(winning_num)

# guess=int(input("Enter your guess: "))

# if (guess==winning_num):
#     print("congrats! You Win!")
# else:
#     print("Loser")

num_guesses=5
user_won= False 

while num_guesses !=0 and user_won==False:
    user_guess=int(input("Enter Your guess: "))
    if user_guess==winning_num:
        print("Hey, you won!")
        user_won=True
    else:
        num_guesses -=1
        print("Nah blood, try again")
        if num_guesses==0:
            print("Nope you lost")
        else:
            print("Try again blood")