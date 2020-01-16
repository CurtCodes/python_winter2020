# Creating a Function that 
# outputs the odd integers between 0 and n(inclusively)

# N=int(input("What is your range?"))
# def odd_num():
#     for N in range(0,N+1):
#         if N%2==1:
#             print(N)
# odd_num()

# lst = []

# def odds():
#     N=int(input("What is your number?"))
#     for num in range(1, N+1):
#         # N=int(input("What is your number?"))
#         if num % 2==1:
#             lst.append(N)
#             print(lst)
# odds()  

lst=[]

# def odd_num():
#     i=0
#     N=int(input("What number are you choosing? "))
#     while i <=N:
#         lst.append(i%2==1)
#         i+=1
#     print(lst)
# odd_num()
# HAve yet to finish koraa.. I need to get numbers as outputs
# as of now I am getting boolean.. I remember being told what I got 
# to do but I forgot. smh.

# NOTE: once again Instructor to the rescue!

def find_odds(n):
    odds=[] # Empty List
    for num in range(0,n+1):
        if (num%2==1):
            odds.append(num)
        return odds

print(find_odds(n))