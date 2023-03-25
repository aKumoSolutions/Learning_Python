# **Functions**

A `function` is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can `return` data as a result.

<br>

## **Creating a Function**
In Python a function is defined using the `def` keyword:

```python
def my_function():
  print("Hello from a function")
```

<br>

## **Calling a Function**
To call a function, use the function name followed by parenthesis:

**Example 1**
```python
def my_function():
  print("Hello from a function")

my_function()
```
<br>

***

<br>

**If a `function` needs to return a value, then use `return` keyword**

**Example 2**
```python
users = []

def ask_name():
    name = input("Enter your name: ")
    # print(f"Welcome aboard {name}")
    return name

def ask_age():
    age = input("Enter your age: ")
    # print(f"You entered: {age}")
    return int(age)

users.append({"name": ask_name(), "age": ask_age()})
users.append({"name": ask_name(), "age": ask_age()})

print(users)
```

<br>

***

<br>

## **Arguments In Funciton**
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just **separate them with a comma**.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

```python
def function1(name, age, pet)
    print(name, age, pet)
```

<br>

***

<br>


## ***Args and ** Kwargs**

Python has `*args` which allow us to pass the variable number of non keyword arguments to function.

*args (Non-Keyword Arguments)  

```python
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
```

Python passes variable length non keyword argument to function using `*args` but we cannot use this to pass keyword argument. For this problem Python has got a solution called `**kwargs`, it allows us to pass the variable length of keyword arguments to the function. 

<br>


- **kwargs (Keyword Arguments)

```python
def function(**kwargs):
    if 'name' in kwargs:
        print("name exists")
    
    print(kwargs['name'])
    print(kwargs['age'])
    
```



<br>

***

<br>


## **Modules**

A Python `module` is a file containing Python definitions and statements. A module can define `functions`, `classes`, and `variables`. A module can also include `runnable code`. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

Read more about modules: https://docs.python.org/3/tutorial/modules.html

<br>

**File functions.py**
```python
def find_actors(actors: list, name: str):
    x = 0
    for actor in actors:
        if name in actor['name']:
            x = x + 1
            print(actor['name'])

    return f"We found {x} number {name}"
```


**Importing function from functions.py file**

```python 
import functions

actors = functions.actors
 
actor = functions.find_actor(actors=actors, name="Tom")
print(actor)
```


<br>

***

<br>

### **Requests module**


The `requests` module allows you to send HTTP requests using Python.

The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).


```python
# from functions import find_actor, actors
import requests, pprint

pp = pprint.PrettyPrinter(indent=4)

def github_status():
    ## syntax
    ##requests.get(url, header, data)
    github_status = requests.get('https://www.githubstatus.com/api/v2/status.json')
    status_r = github_status.json()
    if status_r['status']['indicator'] == 'none':
        description = status_r['status']['description']
        indicator = status_r['status']['indicator']
    else:
        description = status_r['status']['description']
        indicator = status_r['status']['indicator']

    return description, indicator

print(github_status())
```