#Simplest example
def my_decorator(func):
    def wrapper():
        print('Prints before the code!\n')
        func()
        print('Executes after the code!\n')
    return wrapper

@my_decorator
def standalone_function():
    print('Leave me alone!\n')

standalone_function()

#Sandwich examples
def bread(func):
    def wrapper():
        print("<'''''''''>")
        func()
        print("<_________>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("~salad~")
        func()
        print("~tomatoes~")

    return wrapper

@bread
@ingredients
def sandwich():
    print("--ham--")

@ingredients
@bread
def strange_sandwich():
    print("--ham--")

sandwich()
print("\n")
strange_sandwich()

#Return text with the bold and italics outside

def make_bold(func):
    def wrapper():
        return "<b>" + func() + "<\\b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return "<i>" + func() + "<\\i>"
    return wrapper

@make_bold
@make_italic
def greeting():
    return "Hello!"

print(greeting())