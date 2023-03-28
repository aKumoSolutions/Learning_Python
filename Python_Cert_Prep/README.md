### Octal Numbers

its part of the exam but not widely used. When number starts with 0O or 0o then thats octal value and only can use 0 to 7

```
print(0o123)
```

## hexadecimal numbers

```
print(0x123)
```

### Operators

Can't divide by 0

```python
division = 5 / 7
plus = 4 + 4
subtraction = 5 - 2
multiplication = 5 \* 5
```

<br>

## integer division

```python
int_num = 7 // 2
print(int_num)
```

<br>

## modulus division

```python
left_over_num = 7 % 4
print(left_over_num)
```

<br>

## power operator

```python
power_sum = 2 \*\* 3
print(power_sum)
```

<br>

## Float

```python
float_sum = 2 + 3.0
print(float_sum)
```

<br>

Extra: How does modulo division % work?
I’ve noticed that some students have problems understanding how modulo division works. Here is an easy-to-follow example that I once provided to a student in a private message. If you have a problem with modulo, have a look at it.

---

Let’s say that you work in a car company, and you produce wheels for cars. Your boss comes and says: “We need to quickly assembly as many cars as we can. We need the wheels that you produce in sets of 4. How many cars can we produce with the wheels that you have at the moment?”
You know that 1 car needs 4 wheels. Now, if you have 5 wheels in total in your factory, you will be able to create only 1 set of 4 wheels for 1 car, and you will then have 1 wheel left (5 = 4 _ 1 + 1). This “1 wheel left” is the remainder. And it’s also the result of modulo division. 5 % 4 = 1.
If you have 7 wheels, you can still only create 1 set of 4 wheels, and you will be left with 3 wheels (7 = 4 _ 1 + 3). The “3 wheels left” is the remainder. 7 % 4 = 3.
If you have 10 wheels, you can create 2 sets of 4 wheels, and you will be left with 2 wheels (10 = 4 \* 2 + 2). The “2 wheels left” is the remainder. 10 % 4 = 2.
If you only have 3 wheels in total, how many cars can you assemble? Zero. 3 wheels is not enough even for a single car, so you can produce 0 sets, and you will be left with 3 wheels. 3 % 4 = 3.
In general, if you have x % y, and the second number y is greater than the first number x, the result will always be x:
7 % 16 = 7
7 % 20 = 7
5 % 10 = 5
20 % 30 = 20

## Exercise - 2

Variables and Operators
In a fictional country named Lowtaxland, the income tax is 5%. In another fictional country, Ripoffland, the income tax is 43%. You are given a sample variable named income with the value of 250,000.

1. Create two additional variables: lowtaxland_rate with the value of 0.05 (which is the same as 5%) and ripoffland_rate with the value of 0.43 (which is the same as 43%).
2. Print to the output the following:
   Your income is {income} and you would pay {tax amount in Lowtaxland} income tax in Lowtaxland or {tax amount in Ripoffland} income tax in Ripoffland. You would save {difference between the tax amounts} by paying taxes in Lowtaxland!
   Your solution must replace the curly brackets (e.g. {income}) with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as {income _ lowtaxland_rate} for Lowtaxland, and {income _ ripoffland_rate} for Ripoffland, respectively.

# Reassigning Values

```python
age = 22
print(age)
age = age + 5
print(age)
```

    ### shortcut ^

```python
age = 22
age += 5 ## also works with "-, \*, /, +"
print(age)
```

## string things

```python
string = "hokus" + "pokus"
print(string)

string = "hokus"
print(string \* 5)
```

## string concatenation

```python
print('23' + '3')
```

## input function

```python
print("What is your name?")
user_name = input() #input function always returns str
print('Hello there ' + user_name)

user_name = input("What is your name?: ")
print('Hello there ' + user_name)
```

## Exercise - 3

Practising input()
Ask the user to provide their login and native language. Use the following prompts:
Enter your login: << remember to add a space at the end of this prompt!
Enter your native language: << remember to add a space at the end of this prompt!
Then, show the user the following message:
Your login is {login provided} and you speak {language provided}
For example, if the user provides the login h_potter and language British English, show:
Your login is h_potter and you speak British English
Watch out for typos: you must show the output in this particular format!

# A bit of technical theory

**Computer program** = a collection of instructions executed by a computer.

**Instruction list** = the set of instructions the given computer can execute; written in the form of machine code

**Compilation**

- Compiles source code only once
- anyone can run the executable file

**Interpretation**

- interpret source code everytime you run programs
- everyone needs the interpreter to run

**Python interpreter behaviour**

- lexis - pre-defined keywords that cannot be used as variables
- syntax - the arrangement of keywords and phrases that make up python lanugage
- semantics - reference of what is True, if a function takes 1 arg, you can only give 1 arg

# Module 2: Data Types, Evaluation, Basic I/O

## **Type Casting**

Type Casting is the method to convert the variable data type into a certain data type in order to the operation required to be performed by users.

```python
    height_cm = float(input("Height converter: enter your height in cm: "))
    print("Your height in feet is: ", height_cm / 30.48)
```

## Exercise 4

Salary calculator
Ask the user for the number of hours they worked last month and their hourly rate (both numbers should be floats). Use the following prompts:
How many hours did you work last month? << add a space at the end of this prompt
What is your hourly rate? << add a space at the end of this prompt
Then, show the following message with the calculated salary:
Last month, you earned {hours \* hourly_rate} dollars
The salary should be shown as a float number. For example, for input 30 hours and hourly rate 10.5, show:
Last month, you earned 315.0 dollars
Watch out for typos: you must show the output in this particular format!

## **print() and strings. Keyword Arguments and Named Arguments**
``` python
    print('Hello, World', end='.')
    print('Python speaking')
```

**keyword arguments** - optional arguments which you can use at the end of the function after all the other arguments. 


```python
    first_name = 'John'
    print("Your name is", first_name, "Welcome!", sep='-', end='=')
```

This will print

```
Your name is-John-Welcome!=
```

## Bit operators

```python
& - logical AND
| - logical OR
~ - logical NOT
^ - logical XOR
<< - original value multiplied 
>> - original value divided


Example:
    12 << 1 = 24
    12 << 2 = 48
    12 << 3 = 96

    12 >> 1 = 6
    12 >> 2 = 3
```

# Module 3: Control Flow - Conditional Blocks and Loops

```python
    if condition_a_met:
        do_scenario_a()
    elif condition_b_met():
        do_scenario_b()
    elif condition_c_met():
        do_scenario_c()
    else:
        do_scenario_d()
```

## **Available logical operators**

```python
    <  less than
    >  greater than
    <= less than or equal
    >= greater than or equal
    == equals
    != not equals
```

## **Joining multiple conditions**

```python
    1. not
    2. and
    3. or


user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((user_age < 25 and not user_country == 'Germany') or (user_age < 25 and user_country == 'Germany')):
    print('You qualify')
else:
    print('You don\'t qualify!')
```

## Exercise 5

Refund Policy Helper
Let's help an online store with their new refund policy. In this store, you can return an item and get a refund in 2 cases:

1. Within 10 days from the day of purchase, given that you have not used the item, or
2. No matter when you bought it, when the item broke down through no fault of your own.

Write a program that first asks the user three questions and then informs them whether they can get a refund. Ask the following questions:

How many days ago have you purchased the item? << add a space at the end of this prompt

Have you used the item at all [y/n]?  << add a space at the end of this prompt

Has the item broken down on its own [y/n]?  << add a space at the end of this prompt

Based on the answers and the refund policy explained above, print either:
You can get a refund.
or:
You cannot get a refund.

### Here's a sample solution to Coding Exercise 5:
``` python
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
 
if(is_broken == 'y' or (purchase_days_ago <= 10 and is_used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')
```


## for loop and while loop

 - A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

 - With the while loop we can execute a set of statements as long as a condition is true.

```python 
for letter in 'hello!':
    print("Current letter: ", letter)

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print('Finished')


for counter in range(1, 11, 2):
    print(counter)
print('Finished')

```


## break and continue

**Break statement** - The break statement is used to terminate the loop or statement in which it is present. After that, the control will pass to the statements that are present after the break statement, if available. If the break statement is present in the nested loop, then it terminates only those loops which contains break statement


**Continue statement** Continue is also a loop control statement just like the break statement. continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop. As the name suggests the continue statement forces the loop to continue or execute the next iteration. When the continue statement is executed in the loop, the code inside the loop following the continue statement will be skipped and the next iteration of the loop will begin.

**break**
```python
while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
```

**continue**
```python
for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i)
```


# Module 4: Data Collections, Tuples, Lists, Dictionaries

### **Collection Data Types** - are the data types that can store more than 1 value in a single variable


## **Lists**

```python
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']

print(top_cities)

print(top_cities[0])
print(top_cities[1])
print(top_cities[-1])

print(top_cities[0:3])

```

### **Deleting element in the list**

```python
top_cities = ['New York', 'Los Angeles',
              'Singapore', 'Chicago', 'Huston', 'Phoenix']
del top_cities[2]
print(top_cities)

```

### **Adding new elements to lists**

```python
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

book_ratings.insert(1, 10)
print(book_ratings)

```

### **Iterating lists**

**Example 1**
```python
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for city in top_cities:
    print("Current city: ", city)
```

**Example 2**
```python
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for index in range(len(top_cities)):
    print("Current index: ", index, '| Current city: ', top_cities[index])
```

**Example 3**
```python
spendigs = [32.45, 18.65, 23.45, 78.32, 5.23]

sum = 0.0
for spending in spendigs:
    sum += spending
print('Money spent:', sum)
```


## **Changing the element position in list**

**Swapping elements in list**
```python
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

Answer: ['Phoenix', 'Los Angeles', 'Chicago', 'Huston', 'New York']
```

<br>

**Sorting the list**

```python
top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
top_cities.sort()
print(top_cities)

Answer: ['Chicago', 'Huston', 'Los Angeles', 'New York', 'Phoenix']
```

<br>

**Sorting using reverse**

```python
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

Answer: [5, 4, 2, 0, -3]
```

<br>


**Element check inside of the list**

```python
invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in invited_guest:
    print('Welcome!')
else:
    print('You are not invited!')
```

<br>

**Copying list**

```python
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew', list_new)

Answer: Original: [-5, 2, 3] 
        New [1, 2]
```

<br>


**List Comprehension**

```python
numbers = [i for i in range(1, 101)]
print(numbers)

Answer: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)

Answer: [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100]
```


**Nested List**

```python
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

print(cells[0]) = ['A1', 'A2', 'A3']
print(cells[0][0]) = A1
print(cells[0][1]) = A2
print(cells[1][2]) = B3


for row in cells:
    for cell in row:
        print(cell, '', end=' ')
    print()

Answer: A1  A2  A3  
        B1  B2  B3 


table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

Answer: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
```


**Add / Multiply List**

```python
list_us = ['New York', 'Chicago']
list_uk = ['London', 'Bristol']

list_all = list_us + list_uk
print(list_all)

Answer = ['New York', 'Chicago', 'London', 'Bristol']


list_numbers = [0, 1] * 10
print(list_numbers)

Answer: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

```

### **String Features**

```python
fav_band = 'Green Day'
print(fav_band[6])

Answer: D

print(fav_band[:6])

Answer: Green

fav_band[6] = 'M'

Answer: 

fav_band[6] = 'M'
TypeError: 'str' object does not support item assignment

```

**Text Capitalization**

```python

text = 'please capitalize me'
text_cap = text.upper()
print(text_cap)

Answer: PLEASE CAPITALIZE ME 
```


## **Tuples**

**Tuples are immutable**

```python
three_el_tuple = 1, 2, 3
print(three_el_tuple)

Answer = (1, 2, 3)

user_data = ('John', 'American', 1964)


user_data.append('teacher')
This will throw an error:
AttributeError: 'tuple' object has no attribute 'append'


del user_data[0]
This will throw an error:
TypeError: 'tuple' object doesn't support item deletion
```

## Tuples in list

```python
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0, 4)
city_3 = ('Algiers', 'Algeria', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra',
                                     'Australia', 0, 4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name:', capital[0], ', Country:',
          capital[1], ', Population:', capital[2])


Answer:
Name: London , Country: UK , Population: 8.98
Name: Canberra , Country: Australia , Population: 0
Name: Algiers , Country: Algeria , Population: 3.9
```

## List in tuples
```python
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.3)
print(user_data)


Answer: ('John', 'American', 1964, [77.0, 78.2, 77.5, 79.3])
```


## Exercise 8

All Roads Lead to Rome
You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:

(city_from, city_to, time)

For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:

('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). Among the routes to Rome, you should also calculate the average flight time. Print the following the output:

{} connections lead to Rome with an average flight time of {} minutes

Replace {} with the number of connections and the average flight time.


### Here's a sample solution to Coding Exercise 8:
``` python
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
num_con = 0
num_minutes = 0
for i in connections:
    if i[1] == 'Rome':
        num_con += 1
        num_minutes += i[2]
            
print(f"{num_con} connections lead to Rome with an average flight time of {num_minutes / num_con} minutes")
```

## **Dictinaries**


```python
emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel@com'
}

print(emails['Mark Steel'])

Answer = mark@steel@com
```


# Dictionary operations

```python 
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

print(grades)

Answer: {'John': 'A-', 'Anne': 'B'}

```

```python
grades['John'] = 'A-'
grades['Anne'] = 'A'

print(grades)

Answer: {'John': 'A-', 'Anne': 'A'}
```

```python

grades.update({'John': 'A'})

print(grades)

Answer: {'John': 'A', 'Anne': 'A'}

```

```python
del grades['John']
print(grades)

Answer: {'Anne': 'A'}
```

```python
grades['Anne'] = 'A'
grades['John'] = 'A'

for el in grades:
    print(el)

Answer:
Anne
John


for el in grades.keys():
    print(el)

Answer:
Anne
John


for el in grades.values():
    print(el)

Answer:
A
A


for person, grade in grades.items():
    print(person, 'got', grade)

Answer:
Anne got A
John got A
```

## Exercise 9

Write a program that implements a simple interactive dictionary. Start by prompting the user with the following:

Enter a word in English or EXIT: << put a space at the end of this message

When the user enters EXIT in capital letters, terminate the program with the following:

Bye!

Otherwise, try to find the German equivalent in the dictionary provided in the exercise.

a. if the word is in the dictionary, print: Translation: {} << replace {} with the word from the dictionary
b. if the word is not in the dictionary, print: No match!

You should keep asking the user for new words with the same prompt ('Enter a word in English or EXIT: ') until the user provides EXIT.


### Here's a sample solution to Coding Exercise 9:
``` python
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    word = input('Enter a word in English or EXIT: ')

    if word == 'EXIT':
        break

    if word in sample_dict:
        print(f'Translation: {sample_dict[word]}')

    else:
        print('No match!')


print('Bye!')
```