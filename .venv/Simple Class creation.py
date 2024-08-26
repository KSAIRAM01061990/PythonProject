# Creat and instance creation

class person:
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname  = lastname
        self.age  = age
        self.gender =gender

    def concatenatename (self):
            fullname = self.firstname+self.lastname
            return fullname


obj = person('sairam',' Kanamarlapudi',35,'Male')
print(obj.concatenatename())

print(obj.firstname)
print(obj.lastname)
print(obj.age)
print(obj.gender)


# Inheritance concept in python

class person1():
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def person2(self,languages):
        print(f" list of languages know : {languages}")

class employeedata(person1):  # calling parent class in to child class
    def __init__(self,firstname,lastname,age,gender,salary,jobtitle):
     # person1.__init__(self,firstname,lastname,age,gender)
     super().__init__(firstname, lastname, age, gender)
     self.salary = salary
     self.jobtitle = jobtitle

    def display_info(self):
        print(f" employee name {self.firstname}{self.lastname} work as a {self.jobtitle}")


obj = employeedata('sairam',' Kanamarlapudi',35,'male', '$20','Data engineer')
obj.display_info()
obj.person2('English,Telugu,Hindi')
