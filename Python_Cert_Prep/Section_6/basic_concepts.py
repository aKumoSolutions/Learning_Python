# Functions

# Functions always start with def

def greet():
    print('Hello World!')


greet()

input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]


def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)


get_average(input_numbers)


def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)


print_letter_count('Welcome', 'e')

print_letter_count(
    'People say nothing is impossible, but I do nothing everyday.', 'o')


# Shadowing in python
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)


mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)


def show_truth1():
    mysterious_var.append('New Surprise!')
    print(mysterious_var)


mysterious_var = ['Surprise!']
print(mysterious_var)
show_truth1()
print(mysterious_var)


# None value

def greet1():
    print('Hello World')


x = greet()
print(x)

# Return keyword


def get_average1(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average


average = get_average1([5.0, 3.5, 7.8, 9.9, 10.0])

print(average)

if average > 5.0:
    print('The average is too high!')


def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False


print(is_first_last_equal([10, 3.5, 7.8, 9.9, 10.0]))


for a in range(1, 3):
    for b in range(1, 3):
        if a > b:
            continue
        else:
            print(a * b)
