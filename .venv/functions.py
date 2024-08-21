
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


# Arguments

def function_name(a,b):
    print(f"{a}+{b}={a+b}")

function_name(4,5)

#Arguments by Position or Name

def sub_number(minuend,subtractend):
    print(f"{minuend}-{subtractend}={minuend-subtractend}")


sub_number(1,3)
sub_number(3,1)

sub_number(subtractend=3,minuend=1)

#mixed arguments

def calc_value(minusend,subtraend,degree):
    value=(minusend-subtraend)**(degree)
    print(f"({minusend}-{subtraend})^{degree}={value}")

calc_value(5,subtraend=1,degree=2)

#Required and Optional Arguments

function_name(1,2)

def function_value(a,b=1):  # b optional value
    print(f"{a}-{b}={a-b}")

function_value(5)

#Positional and Keywords Arguments

def show_packed_arguments(*args,**kwargs):
    print(f"args : {args} ; kwargs : {kwargs}")

show_packed_arguments(1,'name',arg1=[1,2,3,4],arg2='name')


def show_unpackaed_args(a,b,c,d,e):
    print(a,b,c,d,e)

list_of_args=[1,2,'name']
key_of_args= {'e':'value', 'd':4}

show_unpackaed_args(*list_of_args,**key_of_args)

def foo(pos1, pos2, /, pos_or_kwd1, pos_or_kwd2='default', *args,
kwd_only1, kwd_only2='default', **kwargs):
    print(
        f"pos1={pos1}",
        f"pos2={pos2}",
        f"pos_or_kwd1={pos_or_kwd1}",
        f"pos_or_kwd2={pos_or_kwd2}",
        f"args={args}",
        f"kwd_only1={kwd_only1}",
        f"kwd_only2={kwd_only2}",
        f"kwargs={kwargs}",
        sep="\n",
    )

foo(1,2,3,kwd_only1=4)
foo(1,2,3,'no default',6,'it is argument',kwd_only1=4,kwd_only2='no default',kwarg1=6,kwarg2='it is keyward arguments')


#Arguments by Value or Reference

def by_value(text,num):
    text=text*num
    print(text)

text='hello world'

by_value(text,3)

print(text)

student={'ram': 100 ,'sai':50}
def by_reference(student):
    new ={'amit':300,'kumar':100}
    student.update(new)
    print(f"in side of the function : {student}")

by_reference(student)
print(f'out side of the funtion : {student}')