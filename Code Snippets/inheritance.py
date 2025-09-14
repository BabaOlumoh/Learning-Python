#Base class: the inherited class gets its methods from the base class
class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()

#Inherited class: derives methods from the base class
class Dog(Animal): #The animal class is passed a parameter to be inherited

    def __init__(self): 
        Animal.__init__(self) #instance of the animal class is created
        print("Dog Created")

    def who_am_i(self): #You can override methods created in the base class
        print("I am a dog!")

    def bark(self):
        print("Woof!")

mydog = Dog()

print(mydog.who_am_i())
mydog.bark()