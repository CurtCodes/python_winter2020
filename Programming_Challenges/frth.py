# prgramming challenge 4
#  finding the differences between lists without using sets

def find_diffs(a,b):
    differences=[]
    for element in a:
        if element not in b:
            differences.append(element)
    
    for element in b:
        if element not in a:
            differences.append(element)
            
    return differences

test1=[1,2,3]
test2=[1,2,3]

print(find_diffs(test1,test2))