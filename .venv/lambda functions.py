# assign the lambda function to variable

add=lambda  x,y:x+y
print(add(1,3))

# without assign the lambda function to variable

print((lambda x,y : x ** y) (2,3))

multipleval = lambda x,y,z : (x*y)**z
print(multipleval(y=2,z=3,x=2))

# pass multiple arguments trough lambda function

multipleargs= lambda *args : sum(args)
print(multipleargs(2,4,5,6,7,8,))

# optional arugment values

optionalvalue= lambda x,y=20,z=100 : x+y+z
print(optionalvalue(20))
print(optionalvalue(10,20,30))

# higher order function

high_order_fun = lambda x , fun : x+fun(x)
print(high_order_fun(10, lambda x : x*x))

# by using lambda functions how to write conditions

print((lambda x : x % 2 and 'odd' or 'even') (11))

# filter function by using lambda function
num =[10,20,15,25,60,80,30]

numbers=list(filter(lambda num : num>30,num))
print(numbers)

num1=[10,20,15,25,60,80,30]

numbers1=list(filter(lambda num : (num % 4 ==0), num1))
print(numbers1)

# map function by using lambda function

num3=[10,20,15,25,60,80,30]

number3 = list(map(lambda x : pow(x,3), num3))
print(number3)

#reduce funtion in lambda function

from functools import reduce

num4 = [10,20,15,25,60,80,30]
sum = reduce(lambda x , y : x+y , num4)
print(sum)

# how to use the lambda function in user defined functions

def qudraticvalue(a,b,c):
    return  lambda x : a*x**2+b*x+c

f=qudraticvalue(2,3,5)
print(f(2))