

list1 = set()
list2 = set()

input1 = input("Type in numbers divided by 'space': ")
input2 = input("Second list: ")

ready = input1.split(" ")
ready2 = input2.split(" ")

elements = [int(num) for num in ready]
elements2 = [int(num) for num in ready2]

list1.update(elements)
list2.update(elements2)

comp = list1.intersection(list2)
diff = list1.difference(list2)
print(comp, "these elements exist in both list")
print(diff, "this elements doesn't exist in second list")




