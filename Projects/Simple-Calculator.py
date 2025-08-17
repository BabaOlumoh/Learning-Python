#Practising *args and **kwargs
#args returns a tuple
#kwargs returns a dictionary

def user_input():
    user_write = int(input(""))
def addition(*args):
    return sum(args)

def subtraction(*args):
    subtract = args - args
    return subtract

print