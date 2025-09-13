'''
class Dog(): name of the class
    def __init__ --> name of the object|(self, breed --> parameters) :
    self.breed --> attributes(variable) = breed --> parameters now assigned to attributes


'''

class Dog():
    def __init__(self,breed, name, spots):
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        
        self.breed = breed
        self.name = name

        #Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed = "Lab", name = "Sammy", spots = False)
my_dog.breed
my_dog.name
my_dog.spots

class Goat():
    #Class object attribute
    #same for any instance of a class
    species = 'Mammal'
    def __init__(self, name, kind, wild):
        self.name = name
        self.kind = kind
        self.wild = wild

my_goat = Goat(name = "Billy", kind = "Mountain Goat", wild = True )
my_goat.name
my_goat.kind
my_goat.wild
my_goat.species

