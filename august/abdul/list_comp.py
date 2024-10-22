fruits = ['apple', 'kiwi', 'banana', 'apple', 'apple', 'orange']
unique_fruits = []

for fruit in fruits:
    count = unique_fruits.count(fruit)
    if count == 0:
        unique_fruits.append(fruit)


# res = [fruits.index(fruit) for fruit in fruits]
res = [ fruits[x] for x in range(len(fruits)) if x == fruits.index(fruits[x])]

res = []
print(len(fruits))
for x in range(len(fruits)):
    print(x, fruits[x], fruits.index(fruits[x]))
    if x == fruits.index(fruits[x])
        res.append(fruits[x])
