pets = []

name = input("What is your name? : ")
age = input(f"Hello there {name}! How old are you? : ")
pet = input("Do you have any pets? ")
pet_name = input("What is his/her name: ")
if pet in ['y', 'Y', 'yes', 'yep', 'for sure', 'totally']:
    pets.append(pet_name)
    print(f"{name} has a pet named {pet_name}!")
else:
    print(f"{name} doesn't have a pet 🙁")


print(pets)