# Write a program that uses 
# a nested loop to print a 3x3 grid of *

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print(" ")

names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(index, name)