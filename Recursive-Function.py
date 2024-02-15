#A recursive function is a function that calls itself during its execution.
# In other words, the function performs repetitive tasks by invoking itself with modified
# input parameters each time, leading to a repetitive sequence of function calls.
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i=0
def greet():
    global i
    # i=0
    i=i+1
    print('Hello',i)
    greet()

greet()

