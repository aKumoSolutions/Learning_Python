## list example
# example = ['Amin', 27,  True, 25.5, [1,2,3]]
# print(example [-2]) # [1:4] from 1 to 4 index


# tlist = ['Amin', 'abdul']
# tlist.append("Ahmad")
# print(tlist)

# tlist.insert(2, ["Kris"])
# tlist[2].append("Khulsen")
# print(tlist)

## revolving from a list

# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.pop (1)
# fruits.remove("apple")
# fruits.sort()
# fruits.reverse()

# print(fruits)
fruits = ['apple', 'banana', 'apple', 'cherry', 'orange', 'apple']
unique_fruits = []

for fruit in fruits:
    count = unique_fruits.count(fruit)
    if count == 0:
        unique_fruits.append(fruit)
        print(unique_fruits)
    


# res = []
# res = [x for x in fruits if fruits.count(x) == 1]
# print(res)