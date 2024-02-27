# List comprehension is a concise and expressive way to create lists in Python.
# It allows you to create a new list by applying an expression to each item in an
# existing iterable (e.g., a list, tuple, or range).
# List comprehensions are a more compact and readable alternative to traditional loops.

# For Loop
# new_list=[expression for var in collection]

# with Condition
# new_list=[expression for var in collection if condition]

#=================================================================
#Squaring numbers using loop
# number=[1,2,3,4,5,6]
# print(number)
# squared_list=[]
# for i in number:
#     squared_list.append(i**2)
# print(squared_list)
#
# #Squaring numbers using List comprehensions
#
# squared_list_comprehensions=[i**2 for i in number]
# print(squared_list_comprehensions)

#=====================================================
# number=[1,2,3,4,5,6]
# print(number)
# even_number=[]
# for i in number:
#     if i%2==0:
#         even_number.append(i)
# print(even_number)
#
# even_number_comprehensions=[i for i in number if i%2==0]
# print(even_number_comprehensions)

#=============================
# words=['apple','banana','kiwi','orange','mango']
# short_word=[]
# for i in words:
#     if len(i)>=6:
#         short_word.append(i)
# print(short_word)
#
# short_word_comprehension=[i for i in words if len(i)>=6]
# print(short_word_comprehension)
number=[1,2,3,4,5,6]
square=[x**2 if x**2%2!=0 else -x**2 for x in range(1,11)]
square_number=[x**2 if x**2%2!=0 else -x**2 for x in number]

print(square)
print(square_number)




