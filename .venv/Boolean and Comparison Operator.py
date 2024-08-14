# < , > , <=,>=,==,!=  true , flase
# logical operatators "and or not"
a=100
b=200
c=250
result = a<b and b<c
print(result)


a=1000
b=100
if a<=b and a!=b:
    print("a is less value")
else:
    print ("a is big value")

a = 1000
b = 100
if a <= b and a != b:
    print("a is less value")
elif a==b and a>=b:
    print("a is big value")
else:
    print("a is not satisfied")

#if/elif construction

a="read"
if a=="read":
    print("perform read operation")
elif a=="insert":
    print("perform insert operation")
elif a=="update":
    print("perform update operation")
elif a=="delete":
    print("perform delete operation")
else :
    print(" perform no opeation ")

# match/case construction it support for python 3.10 version

# a="read"
# match a:
#  case "read":
#      print("perform read opeartion")
#  case "insert":
#      print ("perform insert operation")
#  case "update":
#      print("perfrom update statement")
#  case "delete":
#      print("perform delete operation")
#  case _:
#      print("perform no opeartion")

# ternary operator and  if/else operator

fruit="apple"
rs_fruit="yes" if fruit=="apple" else "no"
print(rs_fruit)

fruit="apples"
if fruit=="apple":
    print("yes")
else :
    print("no")






