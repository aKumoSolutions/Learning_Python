## break
# for i in range(1, 10):
#     if i == 5:
#         print(i + 2)
#         continue ## break

#     print(i + 1)   
fruits = ['apple', 'carrot', '3', 'banana', 'cherry', 'carrot']
removed = 0
for item in fruits:
    if item.isdigit():
        print("broken loop")
        break

    if item == "carrot":
        fruits.remove(item)
        removed += 1
        continue

    elif item == "potato":
        pass ## placeholder

        print(item, "is a great fruit!")
else:
    print(fruits)
    print(removed, "# of carrots removed")
