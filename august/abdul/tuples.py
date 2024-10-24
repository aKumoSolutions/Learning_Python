# list = [] -- ordered, changed
# tuple = () -- ordered, non-changable 

# tl = (3,)
# print(type(tl))

#  Write a Python program that:
#  Creates a list of student grades (e.g., [85, 90, 78, 92, 88]).
#  Adds a new grade to the list.
#  Sorts the list of grades.
#  Calculates and prints the average grade.


# grades = [85, 90, 78, 92, 88]
# new_grade = int(input("Please enter a grade [1-100]: "))
# grades.append(new_grade)
# grades.sort()
# avrage_grade = sum(grades) / len(grades)

# print("Grades:", grades)
# print("Grade Sum:", sum(grades))
# print("Avrage grade is", avrage_grade)


# Create a tuple containing the names of the months.
# Slice the tuple to display the first quarter of the
# year (January to March).
# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# print(months[:3])

# Write a Python program using list comprehension that 
# creates a list of squares of all even numbers between 1 and 20.


evens = [x**2 for x in range(1,21) if x % 2 == 0]
print(evens)