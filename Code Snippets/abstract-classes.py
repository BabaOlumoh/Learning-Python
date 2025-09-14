#An abstract class is not to be instantiated; it doesn't need an instance because it's used as a building block for other classes to inherit from
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
#This class is going to inherit from the base abstract class above
#The inherited class doesn't need a constructor as one is already implemented in the base class
class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"

fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())