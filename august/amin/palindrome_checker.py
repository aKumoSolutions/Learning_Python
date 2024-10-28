
list = []

user_input = input("Please enter word or phrase: ")

case = user_input.replace(" ", "")
case1 = case.lower()

# for l in case:
list.append(case1)

reversed = list[0][::-1]

if list[0] == reversed:
    print("Palindrome word")
else:
    print("no Palindrome found")
