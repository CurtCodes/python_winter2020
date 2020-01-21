my_first_list = [2, 4, 6, 8]
print(my_first_list[3])

length =len(my_first_list)
print("The length of the list is ", length)

for index in range(0, len(my_first_list)):
    element=my_first_list[index]
    print(element)

### Error here
# my_first_list[4]
# issue here is that the index doesnt go up to 4 so it wont
# allow you to access

print("Original list: ", my_first_list)
my_first_list.append(10)
print("List after append: ", my_first_list)

#TODO: make a list of even numbers up to 12(inclusive)

evens_list=[]
# for num in range(1,13):
#     if num%2==0:
#         evens_list.append(num)

# print("List of even numbers up to 12 ", evens_list)
# evens_list.clear()
# print("List after using clear",evens_list)

### removing something from array
print("List before popping and element", evens_list)
for i in range(0,len(evens_list)-1):
    if evens_list[i]==8:
        index_of_ten=i
        ten = evens_list.pop(i)

print("list after popping an element",evens_list)
print("The value of ten: ", ten)

###Adding into an array
evens_list.insert(index_of_ten, ten)
print("Using insert, to put the 10 back: ",evens_list)

print(sorted(evens_list))