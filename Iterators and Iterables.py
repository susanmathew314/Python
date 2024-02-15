
# list1=[7,8,9,0] 


# # print(list1[0])


# # for i in list1:
# # 	print(i)

# #Itirrator start=============

# it=iter(list1) #Now we are converting list Iterable to List Iterators.
# # print(it) #iter() will chage the list into iterator, it will not initilise in memory location.

# print(next(it))
# print('Hello')
# print(next(it))
# #One more wayt o get the value from Iterator

# print(it.__next__())
# print(it.__next__())

numbers=[5,7,3,8,2,0,1]
element=iter(numbers)

print('Sussan')
print(next(element))
print('Sussan')
print(next(element))
for i in element:
	print(i)




