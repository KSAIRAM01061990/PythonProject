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