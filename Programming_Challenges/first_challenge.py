# create a Function that takes in floats and integers and adds them up
# if no numbers are added the output should be 0

# First attempt

num=[]
print(num)   # doing this just to check what is inside

# 2nd attempt
# def adding_floats(N):
#     num.append(float(input("Add some numbers")))

N=int(input("How many numbers do you want to add to the list?"))

# 3rd attempt
# for i in range(N):
#     num.append(float(input("What do you want to add to the list?")))
#     print("The sum of the list is, ",sum(num))

# final attempt, incorporated into a function
def adding_num():
    for i in range(N):   # I didnt know what to use for 'i' ... 
        num.append(float(input("What do you want to add to the list?")))
        print("The sum of the list is, ",sum(num))

adding_num()

# NOTE: Instructors way of doing this!

# def sum_up(list):
#     sum=0
#     for i in range(0,len(list)):
#         sum+=list[i]
#     return sum

# def sum_up(list):
#     return sum(list)



