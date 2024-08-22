# def value():
#     value()
#
# print(value())

# Factorial value with loop
def factorialvalue(n):
    if n == 0 or n == 1:
        factorial = 1
    else :
        factorial = 1
        for i in range(1,n):
         factorial = factorial * i

    return factorial

print(factorialvalue(5))

# factorial valuewith out loop

def factorialvalue1(n):
    if n == 0 :
        factorial=  1
    else :
        factorial = n * factorialvalue1(n-1)
    return factorial


print(factorialvalue1(3))

# fabonacci series
a=0
b=1
for i in range(0,10) :
    c=a+b
    a=b
    b=c
    print(c ,end=' ')

