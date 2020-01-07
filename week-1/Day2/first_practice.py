# Practicing with lists and functions

# Example: define a function

# Between A and B(inclusive)

# def find_evens(A,B):
#     evens=[]
#     for nums in range(A,B+1):
#         if (nums%2==0):
#             evens.append(nums)
#     return evens
# print(find_evens(2,100))

# TODO: find a function that returnes a list of numbers between A
# and B (inclusive) that are even multiples of 3

def find_of_three(A,B):
    of_threes=[]
    for nums in range(A,B+1):
        if (nums%3==0 and nums%2==0):
            of_threes.append(nums)
        return of_threes
print(find_of_three(1,30))

# def even_mults(A,B):
#     mults=[]
#     for nums in range(A,B+1):
#         if nums%6==0:
#             mults.append(nums)
#     return mults

# print(even_mults(0,20))