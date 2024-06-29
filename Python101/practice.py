all = {'instructors': ['Ahmad', 'Abdul', 'Kris', 'Gulnaz', 'Esen'], 'members': ["Abdulhamid", "Ahmadyar", "Aiya", "Esenbek", "Gulnaz", "Kris", "Marlen", "Meerim", "Mohammad", "Salmon", "Simon"]}

# both = [all['instructors'][person] for person in range(len(all['instructors'])) if all['instructors'][person] in all['members']]

# for person in range(len(all['instructors'])):
#     inst = all['instructors'][person]
#     if inst in all['members']:
#         both.append(inst)

# print(both)

def name():
    try:
        name = input("Please enter full name: ")
        return name
    except:
        return None


def age():
    try: 
        age = int(input("Please enter your age: "))
        return age
    except ValueError:
        print("Not valid number")
        return None


def location():
    try:
        location = input("Please enter your home town: ")
        return location
    except:
        return None

def hobby():
    hobbies = []
    try: 
        while True:
            hobby = input("Please enter your hobby or press enter for none: ")
            if hobby == '':
                break
            else: 
                hobbies.append(hobby)

        return hobbies
    except:
        print("Something went wrong")

people = []
pet =

while len(people) < 2:
    people.append({'full name': name(), 'age': age(), 'location': location(), 'hobbies': hobby()})

print(people)
