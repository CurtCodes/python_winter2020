number=int(input('Enter a number: '))
min_num=3
max_num=15
if number>min_num and number<max_num:
    print('nooice')
elif number>min_num - 2 and number < max_num + 2:
    print('ehh, you pass')
else:
    print('not nooice')