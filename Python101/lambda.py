
# Regular function to add two numbers
def add(x, y):
    return x + y

# Lambda function to add two numbers
add_lambda = lambda x, y: x + y

function_output = add(2, 2)
lambda_output = add_lambda(2, 2)

# print(function_output)
# print(lambda_output)


def test(x):
    return x[1]
test = lambda x: x[1]

# If a key function is given, apply it once to each list item and sort them,
# ascending or descending, according to their function values.


# help()

# points = [(1, 2), (3, 1), (5, -1), (0, 0)]
# points.sort(key=lambda x: x[1])
# print(points)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  

even_numbers = []
def get_even_number(x):
    for num in x:
        if num % 2 == 0:
            even_numbers.append(num)
get_even_number(numbers)

print(even_numbers)
# Output: [2, 4, 6]
