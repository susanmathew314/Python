#a decorator is a design pattern that allows you to extend or modify the behavior of
# #functions or methods without changing their actual implementation.
# Decorators are typically used to add functionality to existing functions or methods in a clean and concise way.

#A decorator is a function that takes another function as input and returns a new function.
# The new function usually enhances or modifies the behavior of the original function in some way.




def printhello(func):
    def wrapper():
        print('hi')
        func()
        print('Bye')

    return wrapper
@printhello

def greet():
    print('Hello')


greet()


