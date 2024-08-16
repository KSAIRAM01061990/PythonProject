my_first_list =["hello",12345,"epam","[how is your day today ]"]
print(my_first_list)

# how to update the list value

my_first_list[2]="678910"

print(my_first_list)

# how to add the value to the list

my_first_list.append("[Parthik venkat sai]")

print(my_first_list)


my_list_value=[1,2,3,4,5,6,7,8,9,10]

for i in my_list_value[::2]:
    print(i)

#    sort

list_value=[10,4,6,7,9,10,14,67,12.2345]
# list_value.sort()
# print(list_value)
print(len(list_value))

# extend

list_data="abc"
list_value.extend(list_data)
print(list_value)

#count

x=10
print(list_value.count(x))

#pop

data="9020221"
list_value.append(data)
print(list_value)
print(list_value.pop())
print(list_value)

# to add the all number to the list which we enter

n=int(input("insert value : "))
list_data=[]
for i in range(1,n):

    if i % 2 ==0:
        list_data.append(i)

print(list_data)


# Program to check if a number is prime or not

num = 9

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")



