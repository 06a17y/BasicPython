# Class、Object

class Person:
    def __init__(self, name, gender,age, country):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country
    
    def bio_gender(self):
        if self.gender == "female":
            return "bio-female"
        else:
            return "bio-male"

    def add(self, num1, num2):
        return num1 + num2

Student = Person("Amy", "female", 20, "Japan") # Student object has three attributes

print(Student.name) # Amy
print(Student.bio_gender()) # bio-female
print(Student.add(5,6)) # 11