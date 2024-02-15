#=,copy,deepcopy
#Shallow or Deep Copy
# list1=[1,2,3,4]
# list2=list1
# print(list1)
# print(list2)
#
# list2[1]=100
# list1[2]=200
# print(list1)
# print(list2)
#


#shalow and deep copy

# =,copy() -is shallow copy

# deepcopy()

# list1=[1,2,3,4]
# list2=list1
# print(list1)
# print(list2)
# list2[1]=100
# print(list1)
# print(list2)
#+++++++++++++++++++++++++++++++++=
#copy(), Shallowcopy - When we are working with simple list then data wont be shared. Meanse if you are changing list2 it will have no impact on list1.
# print("second")
# list1=[1,2,3,4]
# list2=list1.copy()
# print(list1)
# print(list2)
# list2[1]=100
# print(list1)
# print(list2)

#nested list - When we are working with nested list and chaning the existing data, it will be shared.
# But, when we are adding data in any of list it will not be shared.
# list1=[[1,2,3,4],[5,6,7,8]]
# list2=list1.copy()
# print(list1)
# print(list2)
#
# list1[0][0]=50
# list2[1][0]=100
# print(list1)
# print(list2)
#
# list1.append([11,22,33,44])
# print(list1)
# print(list2)

#Deep copy - When we are working with simple list then data wont be shared. Meanse if you are changing list2 it will have no impact on list1.

# import copy
# list1=[1,2,3,4]
# list2=copy.deepcopy(list1)
# print(list1)
# print(list2)
# list2[1]=100
# print(list1)
# print(list2)

#Deepcopy- Nested List-
#When we are working with nested list in deepcopy then data is not getting shared either way
import copy
list1=[[1,2,3,4],[5,6,7,8]]
list2=copy.deepcopy(list1)
print(list1)
print(list2)

list1[0][0]=50
list2[1][0]=100
print(list1)
print(list2)

list1.append([11,22,33,44])
print(list1)
print(list2)