#Map is used to match a function with variables, lists etc

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square,my_nums)

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

def slicer(mystring):
    if len(mystring)%2 == 0:
        return "Even"
    else: return mystring[0]

names = ["Andy", "Eve", "Sally"]

list(map(slicer,names))

for name in map(slicer, names):
    print(name)