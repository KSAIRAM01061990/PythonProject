print("hello world")

first_string = "This is \"double quotes\" in double quotes"
second_string = 'This is \'single quotes\' in single quotes'
not_new_line = "String without a new \\n line"
long_str = "Lorem ipsum, dolor sit amet, \
sed do eiusmod tempor incididunt ut."

print(first_string)
print(second_string)
print(not_new_line )
print(long_str )


# backslash
data=" escape the special characters \\n \"data coming from SQL DB \" "
print(data)

# new line

data = " saikumar \n sairam \n kanamarlapudi"

print(data)

# carriage return

data="not this \r \"only this\" "
print(data)

string_value="hello world"
print(string_value[10])

# string_value[1]="b"

string_value="hello world"

for i in string_value:
    print (i);

# slice


my_string="hello world"
slice_object= slice(1,3)
print(my_string[slice_object])

my_string="hello"
print(my_string[::-1])

# split , upper ,lower,find,strip

string_value="hello-world"
print(string_value.split("-"))

string_value="hello-world"
for i in string_value.split("-"):
    print(i)

string_value="hello-world"
print(string_value.upper())

string_value="HELLO-WORLD"
print(string_value.lower())

string_value="hello-world"
print(string_value.find("ello-world"))

string_value="  hello - world  "
print(string_value.strip())

# format method and f-string syntax

age = 33
name = "Filip"
location = "UK"
message = "Hello, my name is {}, I am {}, I am from {}".format(name, age, location)
print(message)

age = 33
name = "Filip"
location = "UK"
message = f"Hello, my name is {name}, I am {age}, I am from {location}"
print(message)


