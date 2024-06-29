try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    # This runs if a ValueError occurs (e.g., input is not a number)
    print("That's not a valid number!")

except ZeroDivisionError:
    # This runs if a ZeroDivisionError occurs (e.g., division by zero)
    print("You can't divide by zero!")

finally:
    # This runs no matter what
    print("Finished trying to divide.")