

import math
y = int(input("Enter number to check if it's prime: "))
square_root = math.sqrt(y)
integers = int(square_root + 1)
for num in range(2,integers):
    res = y % num 
    # print(num, res)
if res == 0:
    print("Not a Prime")
else:
    print("Prime number")