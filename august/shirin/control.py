
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1,10):
#     if i == 5:
#         x = i
#         continue
#     print(i)
# print(x)

fruits = ['apple', 'banana', 'cherry', 'carrot']
removed = 0
for item in fruits:
    if item == 'carrot':
        fruits.remove(item)
        removed += 1
        continue
    
    elif item == "potato":
        pass ## placeholder
    print(item, "is a fruit")
    
print(fruits)
print(removed, "# carrots removed")