# Intro to List
city1 = 'New York'
city2 = 'Los Angeles'
city3 = 'Chicago'
city4 = 'Huston'
city5 = 'Phoenix'


top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']

print(top_cities)

print(top_cities[0])
print(top_cities[1])
print(top_cities[-1])

print(top_cities[0:3])


# deleting elements in list

top_cities = ['New York', 'Los Angeles',
              'Singapore', 'Chicago', 'Huston', 'Phoenix']
del top_cities[2]
print(top_cities)


book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4)
print(book_ratings)

book_ratings.insert(1, 10)
print(book_ratings)

# Iterating lists

top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for city in top_cities:
    print("Current city: ", city)


top_cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']
for index in range(len(top_cities)):
    print("Current index: ", index, '| Current city: ', top_cities[index])


spendigs = [32.45, 18.65, 23.45, 78.32, 5.23]

sum = 0.0
for spending in spendigs:
    sum += spending
print('Money spent:', sum)
