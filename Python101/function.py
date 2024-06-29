result = None

def math(name):
    print("Hello", name)

# math("Abdul")
# math(name="Abdul")

def math(a, b=5):
    global result
    result = a + b
    return result

def addition(x=2, y=2): ## parameters
    print(x + y)

def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}")


# name = None

def get_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    return f"{first_name} {last_name}"

user = get_name()




