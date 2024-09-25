# Sets are immutable {} it similar to list , only different it won't allow the duplicate values

my_set_value={1,2,3,4,5,6,7,7,7}
print(my_set_value)


set1={"a","b","c","d","e","f"}
set2={"c","d","e","f","h","a"}
set3={"g","h","i","j","k","a"}
# union
union=set1.union(set2,set3)
union1=set1|set2|set3
print(union)
print(union1)

#Intersection

Intersection=set1.intersection(set2,set3)
print(Intersection)

#difference

difference=set1.difference(set2,set3)
print(difference)

#update
set1.update(set2,set3)
print(set1)

#add

set1.add("abcd")
print(set1)

#remove
set1.remove("abcd")
print(set1)

#clear
set1.clear()
print(set1)

# create a empty set
a = set()
print(type(a))

set1 = {1,2,3,'a','b','c'}
print(set1)
# set don't allow the duplicate values
set2 ={1,2,3,6,7,8,9,5,5,5}
print(set2)

# set methods

set1={'a','b','c','d'}
print(set1)

# add()
set1.add('k')
print(set1)

# pop()
set1.pop()
print(set1)

# remove()
#set1.remove('k')
#set1.remove('l')
print(set1)

# discord()
set1.discard('l')
print(set1)

# clear(),Copy()
# union
set1={1,2,3,4,5,6,7}
set2={'a','b','c','d'}
print(set1.union(set2))
set1.update(set2)
print(set1)

# difference method

set1 = {1,2,3,4,5,6,7,8}
set2 = {4,5,6,7,8}

print(set1.difference(set2))

# difference_update()

set1={1,2,3,4,5,6}
set2={4,5,6,7,8}

set1.difference_update(set2)
print(set1)

# intersection menthod

set1={4,5,6,7,8,9}
set2={5,3,6,7,2,8}
print(set1.intersection(set2))

# isdisjoint menthod

set1={4}
set2={5,3,6,7,2,8}
print(set1.isdisjoint(set2))

# symmetric_difference() method

set1={1,2,3,4,5,6,7,9}
set2={9,8,10,11,23,45}

print(set1.symmetric_difference(set2))

# issubset,issuperset

# buit in functions

set1 ={1,2,3,4,5,6,7,9}
print(sum(set1))
print(len(set1))
print(max(set1))
print(min(set1))
print(sorted(set1))

print("enter values : " )
set1 = set(input().split())
print(set1)

a= int( input())
print(a)

