
# with return keyword
def squar_root(x):
    return x ** 2

print(squar_root(5))

# without return keyword
def happy_birthday(name,age):
    print(f"happy B day {name}");
    print(f"how old you {age} ");

happy_birthday("sai",35)


# assigning them to variables

my_fun=squar_root
print(my_fun(5))

#passing functions as arguments

def function_name(func,*args):
    result=[]
    for i in args:
        result.append(func(i))
    return result

print(function_name(squar_root,3,6,7))

#storing them in data structures

def cube(x):
    return x ** 3

print(cube(3))


function_names={'squar_root': squar_root, 'cube' :cube }
function_names
print(function_names['cube'](3))
print(function_names['squar_root'](3))
