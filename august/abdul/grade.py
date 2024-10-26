# Write a program that stores student names 
# and their grades in a dictionary. The program 
# should allow the user to add, modify, and 
# remove students from the dictionary, and 
# calculate the average grade.

def verifyGrade(user_input):
    try:
        info = user_input.split(',')
        if not info[1].isdigit():
            print('score must be integer value')
            exit(1)
        return info[0], info[1]
    except IndexError:
        print("Please enter valid data: ex(abdul,55)")
        exit(1)


actions = ['add', 'mod', 'remove', 'cal']
grades = {}
action = input("Please enter an action [add, mod, remove, cal]: ")

if action not in actions:
    print("invalid input, please enter one of the following")
    print(actions)
    exit(1)


print(grades)
## add
if action == 'add':
    input = input('Please enter name and score seprated by ",": ')
    name, grade = verifyGrade(input)
    grades[name] = int(grade)
    print('student', name, 'added successfully')

## modify
elif action == 'mod':
    student = input('Please enter name and score seprated by "," : ')
    name, grade = verifyGrade(student)
    if name in grades.keys():
        grades[name] = int(grade)
        print(name, 'modified successfully')
    else:
        print(name, 'does not exist in grade system')
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
    try:
        average = sum(grades.values()) / len(grades.values())
        print("average grade is", average)
    except ZeroDivisionError:
        print("No students graded")