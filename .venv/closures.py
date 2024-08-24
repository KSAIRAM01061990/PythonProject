# how to declare the closures

def outer():  # outer function
    x = 4

    def inner():  # nested function
        print("value x :", x)
    return inner

a = outer()
print(a())

# eclosure example

def outer_fun():
    x="hello"

    def inner_fun():
        y="world"
        print("inside function value x,y : ",x,y)

    return inner_fun

a=outer_fun()
print(a())

# How to call the func as a argument to the another function

def function1():
    print(" i am a function 1")

def function2(fun):
    print(" I am a function 2 will be calling function 1")
    return fun()

function2(function1)