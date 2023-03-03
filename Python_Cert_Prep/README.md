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

**Complication**

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
    Your first name is-John-Welcome!=
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