#Polymorphism refers to the way different object classes can share the same method name and then those can be called from the same place even though a variety of objects might be passed in
class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    
niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

#There are two ways to implement Polymorhism
#1. A for loop
#2. A function

#For loop
for pet in [niko, felix]:
    print(pet.speak())

#Function
def pet_speak(pet):
    print(pet.speak())

