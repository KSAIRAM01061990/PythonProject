# loops  while/for

# x=int(input("enter initial value for while loop"))
# y=int(input("enter last value for while loop"))
#
# while x<=y:
#     print(x)
#     x+=1

# calculate the sum of even number
#
# n=int(input(" enter value for calculation : "))
# sum_result=0
# div_value=2
# x=1
#
# while x<n:
#     x +=1
#     if x % div_value:
#         continue
#     sum_result += x
#
# print("sum of even number :", sum_result)


# calculate sum of odd numbers
#
# n=int(input(" enter value up to calculate odd and even sum values  : "))
# x=0;
# # sum_result=0
# sum_result_even=0
# sum_result_odd=0
#
# while x<n:
#     x += 2
#     if x % 2 ==0 :
#         sum_result_even +=x
#     else :
#         sum_result_odd +=x
#
# print( "sumof even number ", sum_result_even )
# print( "sumof odd number ", sum_result_odd)


# by using for loop can you find the inserted number is prime number or not

x=int(input("enter input number : "))

for div in range(2,x):
    if not x % div :
        print("not prime number")
        break
else :
        print("prime number :",x)



