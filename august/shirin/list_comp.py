
fruits = ['apple', 'kiwi', 'banana', 'apple', 'orange']
unique_fruits = []

## to remove the duplicates
# for fruit in fruits:
#     count = fruits.count(fruit)
#     if count > 1:                
#         fruits.remove(fruit)
        
# print(fruits)

## to find unique elements
# for fruit in fruits:
#     count = fruits.count(fruit)
#     if count == 1:                
#         fruits.append(fruit)
        
# print(fruits)

## List comprehension
res = []
# res = [x for x in fruits if x not in res]
# print(res)

# for x in fruits:
#     if res.count(x) == 0:
#         res.append(x)

# print(res)

# evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)

res = [fruits[x] for x in range(len(fruits)) if x == fruits.index(fruits[x])]

res = []
print(len(fruits))


