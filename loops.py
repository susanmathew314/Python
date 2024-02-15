

#For In Loop
#The for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# names=['Anil','susan','Sri']
# for i in names:
# 	print(i)


#Directlly assigning one list in for loop

#for i in [2,4,6,8,0]:
	#print(i)


#for number in range(10):
	#print(number)


# for number in range(12,20):
# 	print(number)
# print(next)
# for x in range(20,30, 3):
# 	print(x)
# 	print(next2)

# for x in range(40,10,-3):
# 	print(x)

# for i in range(1,21):
# 	if i%5!=0:
# 		print(i)

		
# for i in [2,4,6,8,0]:
# 	print(i)

# for number in range(10):
# 	print(number)

# for number in range(1,21):
# 	print(number)

# for number in range(1,21,2):
# 	print(number)

# for number in range(20,10,-2):
# 	print(number)

# for i in range(1,21):
# 	if i%5!=0:
# 		print(i)


#The range() function in Python is designed to work with integers, not characters or strings.
 #If you want to iterate over a range of characters from 'a' to 'h', you can use the ord() and chr() functions to convert between ASCII values and characters.


# for i in range(ord('a'), ord('l') ):
#     print(chr(i))


# char='a'
# ascii_value=ord(char)
# print("asci",ascii_value)


#While Loop
#while loop is used to repeatedly execute a block of code as long as a specified condition is true.
# i=1
# while i<5:
# 	print('Hello', i)
# 	i=i+1


# 	count = 6
# while count>=1:
#     print(count)
#     #count = count-1 or
#     count-=1


number=8
count=1
while count<=15:
	product=number*count
	print(number,'X', count,'=', product)
	count=count+1
