user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are younger than 30 years old')
    print('Congratulations, you qualify!')


password = input('Do you know your secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')


# Joining multiple conditions

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange programme')
else:
    print('Sorry, you do not qualify')


user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you don not qualify')


user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((user_age < 25 and not user_country == 'Germany') or (user_age < 25 and user_country == 'Germany')):
    print('You qualify')
else:
    print('You don\'t qualify!')


# Loops

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

# Break and Continue

while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)


for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
