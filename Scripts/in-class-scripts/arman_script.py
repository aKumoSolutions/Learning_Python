feelings = []
good_pets = []

name = input("What is your name? :")
feeling = input(f"Hello {name}! How are you? :")
if feeling in ['good', 'Good', 'Well', 'well', 'great', 'Great']:
    feelings.append(feeling)
    print(f"{name}, I am glad to hear that")
    good_pet = input("I believe you have pet right? :")
    if good_pet in ['yes', 'of corse', 'y']:
        good_pets.append(good_pet)
        pet_name1 = input("What is his/her name? :")
        print(f"{name}, You are lucky, becouse {pet_name1} mekes you happy!!!")
    else:
        print(f"{name}, I am sorry. I though you happy becouse you have a pet")
else:
    print(f"I am so sorry to hear that")
    pet_name2 = input ("I can make you little bit happy. I can present you pet, how would you call his/her? :")
    print(f"I hope {name} and {pet_name2} will be friends forever!!!!!!")