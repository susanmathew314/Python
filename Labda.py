#A lambda function in Python is a small,
# anonymous function defined with the lambda keyword.
# Lambda functions can take any number of arguments,
# but they can only have one expression.
# They are often used when you need a simple,
#throwaway function for a short period.


#normal function
def square(a):
    return a*a
result=square(5)
print(result)


#Lamda
#labda argument:expression
func= lambda a:a*a
result=func(5)
print(result)


add=lambda x,y:x+y
result=add(6,7)
print(result)

def mx(x,y):
    if x>y:
        return x
    else:
        return y
print(mx(78,67))

mx=lambda x,y:x if x>y else y
print(mx(7,7))
list1=[7,8,9]
def square(list1):
    list2=[]
    for num in list1:
        list2.append(num**2)
    return list2
ret=square(list1)
print(ret)


#lambda
retw=(list(map(lambda x:x**2,list1)))
tupleexample=(tuple(map(lambda x:x**2,list1)))
setexample=(set(map(lambda x:x**2,list1)))
print(retw)
print(tupleexample)
print(setexample)

          #Filter
numbers=[1,2,3,4,5,6]

evennumbers=list(filter(lambda x:x%2==0, numbers))
oddnumbers=list(filter(lambda x:x%2!=0, [1,2,3,4,5,6,7,8,9]))
print(evennumbers)
print(oddnumbers)