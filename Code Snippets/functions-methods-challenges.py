def vol(rad):
    rad = (4/3)*3.14*(rad **3)
    
    return rad

vol(2)

def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in the range of {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

ran_check(6,2,7)

def ran_bool(num,low,high):
    if low <= num <= high:
        return True
    else: return False

ran_bool(3,1,10)

def up_low(s):
    low_counter = 0
    high_counter = 0
    for letter in s:
        if letter.islower():
            low_counter+=1
            
        elif letter.isupper():
            high_counter+=1
    print(f"No. of lower case characters :  {low_counter}")
    print(f"No. of Upper case characters :  {high_counter}")
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
    into_set = set(lst)
    into_list = list(into_set)
    return into_list

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

def multiply(numbers):
    total = 0
    for item in numbers:
        total = item * item
        return total
    
