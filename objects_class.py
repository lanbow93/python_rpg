# Creating classes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
    
    def bark(self):
        print("bark")

d = Dog("Tim", 2)

print(d.get_age())

d.set_age(7)

print(d.get_age())