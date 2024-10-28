
# list = [] -- ordered, changed
# tuple = () -- ordered, non-changable

# tl = (3,) # to declare a single element tuple, we need to have coma at the end
# print(tl)

## Write a Python program that:
## Creates a list of student grades (e.g., [85, 90, 78, 92, 88]).
## Adds a new grade to the list.
## Sorts the list of grades.
## Calculates and prints the average grade.

# grades = [85, 90, 78, 92, 88]
# new_grade = int(input("Please provide a grade [1-100]: "))
# grades.append(new_grade)
# grades.sort()
# avarage_grade = sum(grades) / len(grades)

# print("Grades: ", grades)
# print("Grade sum:", sum(grades))
# print("Avarage grade is:", avarage_grade)



## Create a tuple containing the names of the months.
## Slice the tuple to display the first quarter of the year (January to March).

# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
#           'August', 'September', 'October', 'November', 'December')
# print("First quarter:", months[:3])
# print("Last quarter:", months[-3:])

## Write a Python program using list comprehension that creates a list of squares of all 
## even numbers between 1 and 20.
evens = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(evens)