#the goal is print odd numbers between 0 and N
#incorporate users input
#using a for loop

N=int(input("Yerr, enter a number"))

for number in range(1, N+1):
    if (number%2==1):
        print(number)
    
    
    
#Now do it using a while loop

counter = 1
while counter <= N:
    if (counter%2==1):
        print(number)
    number +=1