#a function is a block of organized, reusable code that performs a specific task or a set of tasks.
# Functions provide modularity and allow you to break down your code into smaller, manageable pieces.


# def greet():
#     print('Hello')
#     print('Welcome')
#
#
# print('Out of function')
# greet()

#========================================================
# Argument passgin in function

# def greet(name):
#     print('Hello',name)
#
#
# greet('Anmol')
#------------------------
# names=['Sri','Susan','Anmol','Bob','Yellow']
# def greet(arg1):
#     for i in arg1:
#         print('Hello',i)
#
# greet(names)

#=====================================
# PAssing more than one argument

# def add(x,y):
#     c=x+y
#     print(c)
#
# add(4,6)

#=================================
# Returning Single Value:

# def add(x,y,z):
#     c=x+y+z
#     return c
#
# result=add(4,6,5)
#
# print(result*2)

#===================================

def add_sub_mul(x,y):
    c=x+y
    d=x-y
    e=x*y
    return c,d,e

result1,result2,result3=add_sub_mul(4,6)

print(result1, result2, result3

      )