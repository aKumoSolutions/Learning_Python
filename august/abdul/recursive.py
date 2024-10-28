# 10 // 2 = 5 (0)
# 5 // 2 = 2 (1)
# 2 // 2 = 1 (0)
# 1 // 2 = 0 (1)
# 10 - 1010

def decTobin(n):  ## 10 // 2=5   10 % 2=0 (r) 
    # if n == 1:
    #     return "1"
    if n == 0:
        return "0"
    
    return decTobin(n // 2) + str(n % 2)

# print(decTobin(10))

binary = ''
x = 10
while x != 0:
    binary += str(x % 2)
    x = x // 2

print(binary[::-1])