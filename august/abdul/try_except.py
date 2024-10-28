try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError: 
    print("You cannot divide by 0")
except:
    print("Something else happened")
finally: 
    print("This issue has been solved")
    