# dictionary is mutable data type it allow the data any data type. by using {}  we can create dictionary

d = {
    "name": "Filip",
    "age": 32,
    "is_registered": False,
    "rate": 12.5,
    "total_score": 200,
    "linked_ids": [1, 45, 98]
}
print(d)

#access

name=d["name"]
print(name)

#update
d["age"]=34

#add
d["preference"]= None

#remove
del d["preference"]

print(d)

# display dictionary values

for pair in d.items():
    print(pair)

# altrenate way

for key,value in d.items():
    print(key) ; print(value)

# keys() and values()

for key in d.keys():
    print(key)

for values in d.values():
        print(values)

# get method

print(d.get("name"))

dict1={1:'a',2:'b',3:'c',4:'d'}
print(dict1)
print(dict1.items())
print(dict1.keys())
print(list(dict1))
print(tuple(dict1))
print(set(dict1))
print(dict1.values())
print(dict1.get(1))
dict1[1]='abc'
print(dict1)
dict1.update({10:'abcde'})
print(dict1)
dict1.popitem()
print(dict1)
dict1.pop(3)
print(dict1)
dict1.clear()
print(dict1)





