#Main goal is to add all numbers between N and M

N=int(input("lower limit"))
M=int(input("higher limit"))

sum=0
for num in range(N, M+1):
    sum+=num

print('The total sum is', sum)

#print("the type is", type(sum))


print("while loop")

sum=0
num=N
while num<=M:
    sum+=num
    num+=1

print("the total sum is: ", sum)