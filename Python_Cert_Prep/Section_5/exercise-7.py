# Helping with the Budget
# John has a hard time keeping his budget. Write a program to help him analyse his spendings. You are given a list with John's spendings for each month. Go through the list, and count the number of times...

# a. the spendings were low ( < 1000.0)
# b. the spendings were normal(between 1000.0 and 2500.0 inclusive)
# c. the spendings were high ( > 2500.0)

# Then, print the following to the output:

# Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.


spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0,
             2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low = 0
normal = 0
high = 0

for i in spendings:
    if i < 1000.0:
        low += 1
    elif i >= 1000.0 and i <= 2500.0:
        normal += 1
    else:
        high += 1

print(
    f'Numbers of months with low spendings: {low}, normal spendings: {normal}, high spendings: {high}.')
