# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Boston']

# for city in cities:
#     print(city)

# cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
# for index in range(len(cities)):
#     print("Current index: ", index, '| Current city: ', cities[index])


# set a empty list
# while the lenth of the list is less than 5
# ask user to enter a city name
# before appending the city to the list, check if city exists

cities = []
while len(cities) != 0:
    usr_input = input("Please enter city name: ")
    if usr_input in cities:
        print("City already exists:", usr_input)
        break
    else:
        cities.append(usr_input)



cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
cities[0], cities[4] = cities[4], cities[0]
# print(cities)

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]

sum = 0.0
for spending in spendings:
    sum += spending
# print('Money spent:', sum)

spendings.sort(reverse=True)
# print(spendings)

words = ["Cherry1", "Banana", "apple", "abdul", "Acute", "Exit"]
words.sort()
# print(words)

## copying list
original_list = [1, 2, 3, 4, 5]
new_list = original_list.copy
new_list.append(6)
