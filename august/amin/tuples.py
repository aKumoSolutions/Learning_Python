# list = [] -- ordered, chanegable
# tuple = () -- order, non changeable

# grades = [85, 65, 33, 67, 82]
# new_grade = int(input("Please enter a grade [1-100]"))
# grades.append(new_grade)
# grades.sort()
# avarage_grade = sum(grades) / len(grades)

# print("Grades: ", grades)
# print("Grade sum: ", sum(grades))
# print("Avarage: ", avarage_grade)


# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# print(months[3:1])


evens = [x**2 for x in range(1,21) if x % 2 == 0]
print(evens)
