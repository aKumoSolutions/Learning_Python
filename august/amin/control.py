# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 10):
#     if i == 5:
#         continue ##break
#     print(i)

fruit = input("Fruit: ")
fruits = ['carrot','apple', 'banana', 'cherry', "carrot" ]
removed = 0
for fruit in fruits:
    if fruit == "carrot":
        fruits.remove(fruit)
        removed += 1
        continue
    elif fruit == "potato":
        pass

    print(fruit,"is a great fruit!")

print(fruits)
print(removed, "# of carrots removed")