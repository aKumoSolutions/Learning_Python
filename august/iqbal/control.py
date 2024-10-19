# for i in range(1, 10):
#     if i == 10:
#         print(i + 2)
#         continue ## break
#     print(i + 1)


fruits = ['apple', 'banana', 'cherry', "carrot"]
removed = 0
for item in fruits:
    if item == "carrot":
        fruits.remove(item)
        removed += 1
        continue

    elif item == "potato":
        pass
    print(item, "is a great fruit")
print(fruits)
print(removed, "# of carrots removed")

# if 'pear' or 'banana' in fruits:

#     print("yes")
# else:
#     print("no")