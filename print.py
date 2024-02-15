
# # String Concatination
name='Sri'
age=15
print('My name is '+name+' and I am '+str(age)+' years')

# # String Interpolation:
name='Sri'
age=15
print(f'My name is {name} and I am {age} years')

# #Format() method
name='Sri'
age=15
print('My name is {} and I am {} years'.format(name,age))

# # % Formatting %S= string, %d= integer, %f=float
name='Sri'
age=15
print('My name is %s and I am %d years'%(name,age))

# # Precision and width

pi=3.1415

print('Value of pi: {:.2f}'.format(pi))
print('Value of pi: %.2f' %(pi))

# #allignmen
name ='John'
print('Name:{:<10}'.format(name),end='')
print('Name:',name)

print('apple', 'orange', 'banana', sep=', ')
#
#
print('Hello' , end=' ')
print('World')
#
print('Line 1 \nLine 2')
#
print('apple', 'orange', 'banana', sep=', ', end='.\n')
print('World')

print(r'c:\uer\user\new folder\data.txt')
print('c:\\uer\\user\\new folder\\data.txt')


print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)