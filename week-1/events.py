#the goal of the script is to print out even nuumbers
#between 1 and n

N=int(input("enter an upper limit"))

#for number in range(1,N+1):
#    if (number%2==0):
#        print(number)
        
counter = 1
while counter <= N:
    if (counter%2==0):
        print(counter)
counter+=1