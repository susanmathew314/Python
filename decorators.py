#-------------------------------------
# # Decorator function
# def my_decorator(func):
#     def wrapper():
#         print("Before the function")
#         func()
#         print("After the function")
#     return wrapper

# # Function decorated with my_decorator
# @my_decorator
# def say_hello():
#     print("Hello!")

# # Calling the decorated function
# say_hello()
#----------------------------------------
def age_verification_decorator(func):
    def wrapper(student_name, age):
        if age >= 18:
            print(f"{student_name} is eligible to participate.")
            func(student_name, age)
        else:
            print(f"Sorry, {student_name} is too young to participate.")

    return wrapper

@age_verification_decorator
def participate_in_activity(student_name, age):
    print(f"{student_name} is joining the activity!")

# Example usage
participate_in_activity("Alice", 20)
participate_in_activity("Bob", 16)