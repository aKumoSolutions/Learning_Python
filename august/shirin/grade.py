# Write a program that stores student names and their grades in a dictionary. 
# The program should allow the user to add, modify, and remove students from 
# the dictionary, and calculate the average grade.

actions = ['add', 'mod', 'remove', 'cal']
grades = {'tom': 87, 'bob': 56, 'lucy': 32, 'charlie': 78}
action = input("Please enter an action [add, mod, remove, cal]: ")

if action not in actions:
    print("Invalid input, please enter one of the following")
    print(actions)
    exit(1)
   
## add 
if action == 'add':
    u_input = input('Please enter name and score separated by ",": ')
    info = u_input.split(',')
    if not info[1].isdigit():
        print('score must be integer value')
        exit
    grades[info[0]] = int(info[1])
    print('student', info[0], 'added successfully')
## modify
elif action == 'mod':
    u_input = input('Please enter name and score separated by ",": ')
    info = u_input.split(',')
    if not info[1].isdigit():
        print('score must be integer value')
        exit
    if info[0] in grades.keys():
        grades[info[0]] = int(info[1])
    else:
        print(info[0], "does not exists in grades")
        exit
## remove
elif action == 'remove':
    student = input("Enter student name you want to remove: ")
    if student not in grades.keys():
        print(student, "does not exist in grades")
    else:
        del(grades[student]) 
        print(student, "successfully removed")
## calculate the avarage        
else:
    avarage = sum(grades.values()) / len(grades.values())   
    print("Avarage grade is:", avarage)
    
    