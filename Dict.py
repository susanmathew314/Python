#Each item in a dictionary has a key-value pair, where the key is unique within the dictionary, and the value is associated with that key.
 #Dictionaries are defined using curly braces {} and have a key-value format separated by colons (:).


 #Creating Dict:
my_dict={'Name':'Anil','Age':15,'City':'Banglore'}
# print(my_dict)
# print(type(my_dict))

#Accessing the element
# print(my_dict['Name'])

#Adding or updating elements:
# my_dict['Occupation']='Engineer'
# print(my_dict)

#Removing Element
# del my_dict['Age']
# print(my_dict)

#Keys, Values, Items:
# keys=my_dict.keys()
# values=my_dict.values()
# items=my_dict.items()

# print('Keys :', keys)
# print('Values :',values)
# print('Items :',items)

#Updating from Another Dict
# another_dict={'Gender':'Male','Occupation':"Engineer"} #This is another dict
# my_dict.update(another_dict)
# print(my_dict)

Program={'JS':'Atom','CS':'VS','Python':['PyCharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclips'}}
#print(Program)
#print(Program['JS'])
#print(Program['CS'])
# print(Program['Python'])
# print(Program['Python'][0])
# print(Program['Python'][1])
# print(Program['Java'])
# print(Program['Java']['JEE'])

#Assignment
#clear the dictionary, 

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print("Dictionary:", my_dict)


my_dict.clear()

print("Dictionary after clearing:", my_dict)

#copy
original_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Using copy() method
copied_dict = original_dict

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict )