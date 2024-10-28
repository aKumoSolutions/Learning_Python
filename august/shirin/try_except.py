
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid integer.")
except:
    print("Something else heppened")
finally:
    print("This issue has been solved")