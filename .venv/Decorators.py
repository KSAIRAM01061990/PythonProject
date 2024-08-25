# decorators example without arguments

def upper(fun):
    def inner():
        value = fun()
        return value.upper()
    return inner

@upper
def funtion1():
    return "hello world"

print(funtion1())


# decorators example with  arguments
def subtract(func):
    def inner(a,b):
        if b == 0 :
            return "enter correct input value"
        return func(a,b)
    return inner

@subtract
def function2(x,y):
    z=x/y
    return z

print(function2(4,2))

# how to use mulple decorator in single function

def upper(func):
    def lower():
        value = func()
        return value.upper()
    return lower

def split(func):
    def lower1():
        value = func()
        return value.split()
    return lower1

@split
@upper
def function1():
    return "hello world"

print(function1())

# Decorator with argument

def outer(exp):
    def argument_decorator(func):
        def inner ():
            str1 = func()
            return str1 + exp
        return inner
    return argument_decorator

@outer("sairam")
def function2():
    return " Hello good morning "

print(function2())

# Multiple functions how to use single decorators

def div_decorator(func):
    def inner(*args):
        list = []
        list = args[1:]
        for i in list:
            if i == 0 :
                return "enter proper input value "
            return func(*args)
    return inner

@div_decorator
def div(a,b):
    return a/b

@div_decorator
def div1(a,b,c):
    return a/b/c


print(div(10,2))
print(div1(12,2,2))

# How to apply the decorators on calss
def namecheck(method):
    def inner(name_referensh):
        if name_referensh.name == "Sairam":
            print("hey my name is also same ")
        else :
            return method(name_referensh)
    return inner
class printing:
    def __init__(self,name):
        self.name = name
    @namecheck
    def print_name(self):
        print("entered user name is : " , self.name)

a=printing("Sairam")
a.print_name()

# How to use clss as a decorators