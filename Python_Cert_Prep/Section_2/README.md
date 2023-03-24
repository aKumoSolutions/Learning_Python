# **Python User Input**

**PLEASE NOTE THAT INPUT WILL RETURN** `String` **Output**
```python
x = input('Enter your name:')
print('Hello, ' + x)
```

<br>
<br>
<br>

# **Python Data Types**

<br>

## **Getting the Data Type**
You can get the data type of any object by using the `type()` function:

```python
x = 5
print(type(x))
```

<br>

***

<br>

## **Python Numeric Data Type**

`int` - holds signed integers of non-limited length.  
`long`- holds long integers(exists in Python 2.x, deprecated in Python 3.x).  
`float`- holds floating precision numbers and it’s accurate up to 15 decimal places.  
`complex`- holds complex numbers.   

<br>

**Example**
```python
#create a variable with integer value.
a=100
print("The type of variable having value", a, " is ", type(a))

#create a variable with float value.
b=10.2345
print("The type of variable having value", b, " is ", type(b))

#create a variable with complex value.
c=100+3j
print("The type of variable having value", c, " is ", type(c))
```


<br>

***

<br>

## **Python String Data Type**

The `string` is a sequence of characters. Python supports Unicode characters. Generally, strings are represented by either **single** or **double-quotes**.

**Example**
```python
a = "string in a double quote"
b = 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)
```


### **Python String Functions**

<br>

**Here is the all methods that are available for the String Data Type**  
https://www.programiz.com/python-programming/methods/string/

<br>

***

<br>

## **Python List Data Type**

`Lists` are used to store multiple items in a single variable.

`Lists` are one of 4 built-in data types in Python used to store collections of data, the other 3 are `Tuple`, `Set`, and `Dictionary`, all with different qualities and usage.

`Lists` are created using square brackets: 

**Example**
```python
#list of having only integers
a= [1,2,3,4,5,6]
print(a)

#list of having only strings
b=["hello","john","reese"]
print(b)

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)

#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c
```

<br>

***

<br>

## **Python Tuple**

<br>

The `tuple` is another data type which is a sequence of data similar to a `list`. But it is **immutable**. That means data in a **tuple is write-protected**. Data in a tuple is written using parenthesis and commas.

**Example**
```python
#tuple having only integer type of data.
a=(1,2,3,4)
print(a) #prints the whole tuple

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"
```

<br>

***

<br>

## **Python Dictionaries**

<br>

`Dictionaries` are used to store data values in `key:value` pairs.

A `dictionary` is a collection which is ordered*, changeable and do not allow duplicates.


**Example 1**
```python
#a sample dictionary variable

a = {1:"first name",2:"last name", "age":33}

#print value having key=1
print(a[1])

#print value having key=2
print(a[2])

#print value having key="age"
print(a["age"])
```

**Example 2**


```python
MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

>>> print(MLB_team['Minnesota'])
'Twins'     ---> Answer
>>> print(MLB_team['Colorado'])
'Rockies'   ---> Answer
```

<br>

***

<br>

## **Python Boolean**

Booleans represent one of two values: `True` or `False`.

In programming you often need to know if an expression is `True` or `False`.

You can evaluate any expression in Python, and get one of two answers, `True` or `False`.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

**Example**
 
```python
print(10 > 9)   --->  True
print(10 == 9)  --->  False
print(10 < 9)   --->  False
```


```python
==	--->  Equal to
!=	--->  Not equal to
<	--->  Less than
>	--->  Greater than
<=	--->  Less than or equal to
>=	--->  Greater than or equal to
```

<br>
<br>
<br>


# **If, Elif and Else Statements**

An "if statement" is written by using the `if` keyword.  
<br>
The `elif` keyword is Python's way of saying "if the previous conditions were **not true**, then try this condition".  
<br>
The `else` keyword catches anything which isn't caught by the preceding conditions.  

Example
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")  ---> Answer
```


### **There is also another way to write if statement**

```python
a = 200
b = 33

if a > b: print("a is greater than b")  ## This will print "a is greater than b"
```

<br>

***

<br>

# **Python For Loops**  

A `for` loop is used for iterating over a sequence (that is either a `list`, a `tuple`, a `dictionary`, a `set`, or a `string`).

This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the `for` loop we can execute a set of statements, once for each item in a `list`, `tuple`, `set` etc.


**Example**

```python
pets = [
    {
        'name': 'cookie', 
        'age': 2, 
        'home': 'Chicago', 
        'kind': 'cat',
        'toys': ['carrot', 'bunny', 'ball']
    },
    {
        'name': 'Jessie', 
        'age': 5, 
        'home': 'Turkey', 
        'kind': 'dog'
    }
]

first_toy = pets[0]['toys'][0]

for pet in pets:
    if pet['name'] == 'cookie':
        print('My pet is here!')
```