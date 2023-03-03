# Intro to List
city1 = 'New York'
city2 = 'Los Angeles'
city3 = 'Chicago'
city4 = 'Huston'
city5 = 'Phoenix'


top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']

print(top_cities)

print(top_cities[0])
print(top_cities[1])
print(top_cities[-1])

print(top_cities[0:3])


# deleting elements in list

top_cities = ['New York', 'Los Angeles',
              'Singapore', 'Chicago', 'Huston', 'Phoenix']
del top_cities[2]
print(top_cities)


book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

book_ratings.insert(1, 10)
print(book_ratings)

# Iterating lists

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for city in top_cities:
    print("Current city: ", city)


top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for index in range(len(top_cities)):
    print("Current index: ", index, '| Current city: ', top_cities[index])


spendigs = [32.45, 18.65, 23.45, 78.32, 5.23]

sum = 0.0
for spending in spendigs:
    sum += spending
print('Money spent:', sum)


# Changing the element position in the list

first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)

temp = first
first = second
second = temp

print('After swapping: ', first, second)


top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
top_cities.sort()
print(top_cities)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)

# List checking Presence

invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guest:
    print('Welcome!')
else:
    print('You are not invited!')


# Copying List
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew', list_new)


# List comprehension

numbers = [i for i in range(1, 101)]
print(numbers)


numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)

# Nested List

nums = [1, 2, 3, 4]
countries = ['UK', 'US', 'Germany']
countries = [1, 'UK', 2, 'US']
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

print(cells[0])
print(cells[0][0])
print(cells[0][1])
print(cells[1][2])


for row in cells:
    for cell in row:
        print(cell, '', end=' ')
    print()


table = [[i for i in range(1, 6)] for j in range(4)]
print(table)


# Add / Multiply List

list_us = ['New York', 'Chicago']
list_uk = ['London', 'Bristol']

list_all = list_us + list_uk
print(list_all)

list_numbers = [0, 1] * 10
print(list_numbers)


# String Features
fav_band = 'Green Day'
print(fav_band[6])

print(fav_band[:6])


text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)


# Tuples

three_el_tuple = 1, 2, 3
print(three_el_tuple)

user_data = ('John', 'American', 1964)

# Tuples in list

city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0, 4)
city_3 = ('Algiers', 'Algeria', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra',
                                     'Australia', 0, 4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ', Country:',
          capital[1], ', Population:', capital[2])

# List in tuples
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.3)

print(user_data)
