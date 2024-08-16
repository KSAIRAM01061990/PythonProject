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
