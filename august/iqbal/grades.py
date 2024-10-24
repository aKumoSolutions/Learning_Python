# Write a program that stores student names 
# and their grades in a dictionary. The program 
# should allow the user to add, modify, and 
# remove students from the dictionary, and 
# calculate the average grade.
actions = ['add', 'change', 'remove', 'cal']
grades = {'tom': 87, 'bob': 56, 'lucy': 32, 'Charlie': 78}
action =input('please enter an action [add, change, remove, cal]: ')

if action not in actions:
    print('invalid input, please enter one of the following')
    print(actions)

if action == 'add':
    input = input('please enter name and score separated by ",": ')
    info = input.split(',')
    grades[info[0]] = int(info[1])

print(grades)