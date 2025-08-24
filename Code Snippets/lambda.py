def square(num):
    result = num**2
    return result

lambda num: num **2
mynums = [1,2,3,4,5,6]
names = ["Andy", "Eve", "Sally"]
list(map(lambda num:num**2,mynums))
list(filter(lambda num:num%2 == 0,mynums))

#Turn it into lambda
def slicer(s):
    if len(s) % 2 == 0:
        return "Even"
    else: return s[0]
list(map(slicer, names))
list(map(lambda slicer:len(slicer)%2==0 ,names))