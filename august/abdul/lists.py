
## list example
#             0     1    2     3      4
example = ['Abdul', 24, True, 24.6, [1, 3, 2, 0], True]

# print(example)
example[4].sort()
print(example)

## adding to a list
tlist = ['Abdul', "Akmal", "Abdul"]
tlist.append("Ahmad")
print(tlist)

tlist.insert(2, ["Kris"])
tlist[2].append("Khuslen")
print(tlist.index("Abdul"))

## revoving from a list
fruits = ['apple', 'kiwi', 'banana', 'apple', 'orange']
other_fruits = fruits
fruits.pop(1)
fruits.remove("apple")
fruits.sort()
fruits.reverse()

print(fruits)
print(other_fruits)




