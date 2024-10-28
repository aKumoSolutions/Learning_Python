student_grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78
}



input = input("Please type in sentence, divided by 'space': ")
sum = len(input)
student_grades[input] = int(sum)
enter = input.split(" ")

print(sum, "Letter's in sentence")
print(student_grades)