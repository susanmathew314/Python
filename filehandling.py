# Mode
# r=read
# w=write
# a=append
# Reading File

# file=open('C:\\Users\\susan\\PycharmProjects\\learningPython\\Pythonpractice\\data.txt','r')
# print(file.read())

#write file
# file=open('abc.csv','w')
# file.write('Computer')

#Append
file=open('abc.csv','a')
file.write(' Delhi')

file=open('abc.csv','r')
print(file.read())


