# a = int(input("enter insert value for adding : "))
# b = int(input("insert value for adding : "))
# c=a+b
# print(c)

print(abs(-65))

# number methods
import math
a=17.8
print(math.ceil(a))
print(math.floor(a))
print(math.sqrt(a))
print(type(a))

class a :
    pass
print(dir(a))


# string functions
a='hello world'
print(a.split(' '))
a='ram.kanamarlapudi@gmail.com'
a=a.split('@')
a=a[0]
a=a.split('.')
firstname=a[0]
lastname=a[1]
print(firstname,lastname)

a='123456789+3j'
print(a.isnumeric())


a='ram.kanamarlapudi@gmail.com'
a=a.replace('.',' ')
print(a.replace('@',' '))

a='12345'
print(a.join('hello'))

a='hello world'
print(a[::-1])
print(type(a))

# string functions
a="hello world"
print(a.capitalize())
print(a.title())
print(a.isspace())
print(a.swapcase())
print(a.index('l',0,10))
print(a.index('h'))
print(a.find('z'))
print(a.count('h'))
print(a.startswith('h'))
print(a.endswith('b'))


# a="saikumar.kanamarlapudi@gmail.com"
# print(a.index('@',0))
# b=a.index('@',0)
# c=a[:b]
# print(c.split('.'))


# bool Data type

# a= bool(input("enter details : "))
# print(a)
# print(type(a))

# list /Listindexing/list slicing

a=[]
b=[123,'abc','2+3j','hello world']
print(b)
print(b[1:3:2])

