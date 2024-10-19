
for i in range(1, 10):
    if i == 5:
        print(i + 2)  
        continue  

    print(i + 1)



fruits = ['apple', 'banana', 'cherry', 'carrot']
removed = 0  

for item in fruits:
    if item == "carrot":
        fruits.remove(item)
        removed += 1  
        continue  
    
    print(item, "is a great fruit!")  

print(fruits)  
print(removed, "# of carrots removed")
