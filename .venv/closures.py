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