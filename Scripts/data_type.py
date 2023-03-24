my_string = "Hello-World!"
# print(type(my_string))
# print(dir(my_string))
# print(my_string.split('-'))

# name = "Abdul"
# print("My name is " + name)
# print("My name is {}".format(name))
# print("My name is %s" % name)
# print(f"My name is {name}")

# name = input("What is your name: ")
# print(f"Hello there {name}")

my_int = 12345
# print(type(my_int))

my_str = str(my_int)
# print(type(my_str))

my_list = ['abdul', 'esen', 'ahmad']
my_list.append('akmal')

# print(my_list)

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


