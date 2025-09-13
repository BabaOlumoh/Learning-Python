class Goat():
    #Class object attribute
    #same for any instance of a class
    species = 'Mammal'
    def __init__(self, name, kind, wild):
        self.name = name
        self.kind = kind
        self.wild = wild

    #Operations/Actions --> Methods
    #Method is a function inside a class that works with the object in some way

    def sound(self, number):
        print(f"BAAAA! My name is {self.name} and the number is {number}")
my_goat = Goat(name = "Billy", kind = "Mountain Goat", wild = True )
my_goat.sound(3)


class Circle():

    #Class Object Attribute
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    #Method
    def get_circumference(self):
        circumference = self.radius * self.pi *2
        print(f"The circumference is {circumference}")
    
my_circle = Circle()
my_circle.pi
my_circle.radius
my_circle.get_circumference()