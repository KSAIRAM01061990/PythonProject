# Touple are immutables -- you can store the data with peranthesis ()

my_first_touple=(10.6,20,50)
print(my_first_touple)

# packing unpacking

print(*my_first_touple)

x=(1,2,3)
y=(1,2,3)

print(x==y)
print(id(x) , id(y))
print(x is y)

x=[1,2,3]
y=[1,2,3]

print(x==y)
print(id(x) , id(y))
print(x is y)

# swap the values


(a,b,c)=(10,20,30)

print(a,b,c)

my_touple=(1,2,3,4)
print(my_touple[1])


#swap the values
a,b=1,2
temp=a
a=b
b=temp
print(a,b)

# by using packing and unpacking

a,b=1,2
print(a,b)
a,b=b,a
print(a,b)

