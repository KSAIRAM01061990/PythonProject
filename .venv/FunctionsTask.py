def squareroot_value(n):
    if n == 0 :
        return 1
    else :
        value = { }
        for i in range(1,n+1):
            new={i:i*i}
            value.update(new)

        return value

print(squareroot_value(5))


def union_value (*args):
       value1 = args[0]
       value2 = args[1]
       value3 = args[2]
       value= set(value1).union(set(value2)).union(set(value3))
       return value
print(union_value([1,2,3,4,5,6],(4,5,6,7,8,9),{5,7,8,9,10}))
