#While loop will continue to execute a block of code while some condition remains True

'''
while some_boolean_condition is true:
    do_somethiing
else: do_something_else
'''

#While loop
x = 0

while x < 5:
    print(f"The value of x is {x}")
    x += 1
else: 
    print("X is not less than 5")

'''
break: Breaks out of the current cloeset enclosing loop
continue: Goes to the top of the closest enclosing loop
pass: Does nothing at all '''

#Break
x = 0

while x < 5:
    if x == 2:
        break
    print(f"The value of x is {x}")
    x += 1
else: 
    print("X is not less than 5")

#Continue
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

#Pass
x  = [1,2,3]

for item in x:
    # comment
    pass #acts as a placeholder sometimes
print("end of script")

