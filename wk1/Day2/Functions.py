# # Define f(x)=x+1

# def f(x):
#     ans=x+1
#     return ans

# my_sol=f(1)
# print(my_sol)


# def g(y):
#     eq1=y**4 + y**2 + 1
#     return eq1

# sol2=g(2)
# print(sol2)

# Functions with multiple returns
# def get_first_two_evens():
#     return 2, 4

# even1, even2 = get_first_two_evens()
# print(even1)
# print(even2)


# Function with no returns

# def print_even(N):
#     for num in range(1, N+1):
#         if num%2==0:
#             print(num)

# print_even(10) #2,4,6,8,10 should be the things printed out

# TODO: write a function that takes N as an input and print 
# all common multiples of 3 and 7, between 0 and N (inclusive)

# def multiples_of(N):
#     for num in range(3, N+1):
#         if num%3==0 and num%7==0:
#             print(num)

# multiples_of(100)

### Alternative method
# def multiples_of():
#     N=int(input("Enter the upper limit: "))
#     for num in range(3, N+1):
#         if num%3==0 and num%7==0:
#             print(num)

# multiples_of()


# TODO: define a function that takes 3 inputs: x, y, N
# the function will find all the common multiples of x and y
# between 0 and N

def awk_function():
    N=int(input("Yerr, what is the Limit? "))
    x=int(input("What is the lower value that you want to find the multiple of? "))
    y=int(input("what is the higher value of the multiple you want to find the multiple of? "))

    for num in range(0, N):
        if num % x == 0 and num % y == 0:
            print(num)

awk_function()