# local variable declaration

def localvariable():
     x=4
     print("inside function x : ",x)


print(localvariable())

# global variable declaration

y = 4;
def globalvariable():
    x = 3
    print("inside function x,y : ",x,y)

print(y)
print(globalvariable())

# how to change the glocal varibale value in local scope

y = 4
def global_variable():
    x = 4
    global y
    y = y + 5
    print("inside function x,y :",x,y)

print("outside function y : ",y)
print(global_variable())
print("outside function y : ",y)

# enclosing variable creation and change the enclosed variable value in local scope
# LEGB (local,enclosed,global,built-in)

x = 14
def outer():
    y = 17
    print("enclosing scope y :",y)

    def inner():
        z = 20
        nonlocal y
        y = y+15
        print("local scope x,y, z :",x,y,z)

    print(y)
    inner()
    print(y)
outer()


