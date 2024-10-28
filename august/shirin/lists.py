
example = ['Anna', 25, True, 23.4, [1, 3, 2, 0] ]

# print(example) # prints the whole list
# print(example[0]) # prints the first element of the list
# print(example[-1]) # prints the last element of the list
# print(example[4][0]) # prints the first element of the 4 element of the list, which is list
# print(example[1:4]) # prints from a specified starting point, to the specified ending pont


# print(example.count(25)) # count() count how many times an element occurs in the list

# print(example[4])
# example[4].sort()
# print(example[4])

## adding to a list
# tlist = ['Abdul', 'Akmal']
# tlist.append('Ahmad')
# # print(tlist)

# tlist.insert(2, ['Kris'])
# tlist[2].append("Khuslen")
# # print(tlist)

# print(tlist.index('Abdul'))


## removing from a list
fruits = ['apple', 'kiwi', 'banana','orange']
other_fruits = fruits
fruits.pop() # deletes the last element in the list (by deefault the index is -1)
fruits.sort() # sorts the list
fruits.reverse() # reverses the list order
fruits.remove("apple") # removes element by providng a value

print(fruits)
print(other_fruits)