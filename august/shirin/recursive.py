
# def factorial(n):
#     if n == 1:
#         return 1
#     print(n, n-1)
#     return n * factorial(n - 1)

# print(factorial(5)) 

def decToBin(n):
    if n == 1:
        return "1"
    if n == 0:
        return "0"
    return decToBin(n // 2) + str(n % 2)

# print(decToBin(11))

binary = ''
x = 10
while x != 0:
    binary += str(x % 2)
    x = x // 2
    
print(binary[::-1])