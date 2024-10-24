# Write a program that stores student names 
# and their grades in a dictionary. The program 
# should allow the user to add, modify, and 
# remove students from the dictionary, and 
# calculate the average grade.

actions = ['add', 'mod', 'remove', 'cal']
grades = {'tom': 87, 'bob': 56, 'lucy': 32, 'charlie': 78}
action = input("Please enter an action [add, mod, remove, cal]: ")

if action not in actions:
    print("invalid input, please enter one of the following")
    print(actions)
    exit(1)


print(grades)
## add
if action == 'add':
    input = input('Please enter name and score seprated by ",": ')
    info = input.split(',') #['abdul', ' 54']
    if not info[1].isdigit():
        print('score must be integer value')
        exit
    grades[info[0]] = int(info[1])
    print('student', info[0], 'added successfully')

## modify
elif action == 'mod':
    student = input('Please enter name and score seprated by "," : ')
    info = student.split(',')
    if not info[1].isdigit():
        print('score must be integer value')
        exit
    if info[0] in grades.keys():
        grades[info[0]] = int(info[1])
        print(info[0], 'modified successfully')
    else:
        print(info[0], 'does not exist in grade system')
        exit

## remove
elif action == 'remove':
    student = input("enter student you want to remove: ")
    if student not in grades.keys():
        print(student, "does not exist in grade system")
    else:
        del(grades[student])
        print(student, 'successfully removed')

## calculate avr
else:
    average = sum(grades.values()) / len(grades.values())
    print("average grade is", average)