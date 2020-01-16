import random

def organize_game():
    door_contents=[1,0,0]
    random.shuffle(door_contents)

    for i in range(0,len(door_contents)):
        if door_contents[i]==1:
            winning_door=i
    
    return door_contents, winning_door

def game_time():
    door_nums=[0,1,2]

    door_contents, winning_door=organize_game()

    # We need the contestant to make a choice
    door_chosen = random.choice(door_nums)

    #now we need game show host to open another door
    # Game show host opens the door that doesnt have 10 mil, cash
    #  but the door opened cannot be the one the contestant chose
    unavailable_doors=[door_chosen,winning_door]
    door_to_open=set(door_nums).difference(unavailable_doors)

    # We can use pop() function to remove the opened door
    # Make it an integer value
    door_to_open=door_to_open.pop()

    # open the door
    opened_door=door_nums[door_to_open]

    # See if contestant won or lost
    switched_win=False
    stayed_win=False

    # declare the variables that tells us whether the win would come from
    # from switching os staying
    unavailable_doors=[door_chosen, door_to_open]
    switched_choice =set(door_nums).difference(unavailable_doors)

    # switched_choice is currently a set so we need to use pop function to 
    # pop out the number out of the set.
    # switched_choice should be a set of 1

    switched_choice=switched_choice.pop()

    # Use the index value we establised from the switche_choice variable
    #  to find out the contents of the door behind it.
    if door_contents[switched_choice]==1:
        # this means the user won by switching
        switched_win=True

    if door_contents[door_chosen]==1:
        stayed_win=True

    return int(switched_win), int(stayed_win)    

def monte_carlo(N):
    # We need to keep track of number of wins
    # from switching and the number of wins from staying.

    total_switched_wins=0
    total_stayed_wins=0

    switched_win=0
    stayed_win=0

    for game_num in range(0,N):
        switched_win,stayed_win=game_time()

        # if we won by switching increment total switched wins
        if switched_win==1:
            total_switched_wins+=1
        
        # if qw qon by staying, the increment total stayed winss
        if stayed_win==1:
            total_stayed_wins+=1
    
    print(f"Out of {N} plays")
    print(f"switched win percentage = {(total_switched_wins/N)*100}%")
    print(f"Stayed win percentage = {(total_stayed_wins/N)*100}%")


monte_carlo(100000)




# NOTE Intro to sets
# list1=[1,1,1,1,1,3,5,5,3]
# print(set(list1))
# list2=[1,6,7]
# list3=[]
# list3=set(list1).difference(list2)

