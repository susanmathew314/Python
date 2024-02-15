# def greet():
#     print('Hello')
#
# greet()
#===================================================

# Function with arguments

# def add(x,y):
#     c=x+y
#     print(c)
#
# add(5,6)

#================================================
#Function with single return value
#====================
# def add(x,y):
#     c=x+y
#     return c
#
# Var = add(7,6)
# Var1=Var*2
# print(Var1)
#============================
#Fun c tion with two return value
# def Anil(x,y):
#     c=x+y
#     d=x-y
#     return d,c
#
# Result1, Result2 = Anil(7,6)
# print(Result2,Result1)


My_list=['Anil','Anmol','Sri','Ram','Shyam']

# def greeting(x):
#     for name in x:
#     # for name in range(1000):
#         print('Greetings of the day: ',name)
#
# greeting(My_list)

def calc(num1, num2, operator):
    if operator =='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        return 'Invalid operator provided'

Num1=int(input('Please provide the first number: '))
Num2=int(input('Please provide the 2nd number: '))
operator=input('Please provide the operator to calculate: ')

result=calc(Num1,Num2,operator)
print(result)