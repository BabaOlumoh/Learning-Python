import string
string.ascii_lowercase

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

#Important logic
def multiply(numbers):
    total = 0
    for item in numbers:
        total = item * item
        return total
    
multiply([1,2,3,-4])

def palindrome(s):
    reversed_string = s[::-1]
    if reversed_string == s:
        return True
    else: return False

palindrome('helleh')

#important
def ispangram(str1, alphabet = string.ascii_lowercase):
    #convert args to set to use issuperset method
    str1_set = set(str1)
    alphabet_set = set(alphabet)

    if str1_set.issuperset(alphabet_set):
        return True
    else:
        return False
    
ispangram("The quick brown fox jumps over the lazy dog")

def lesser_of_two_evens(a,b):
    #Lesser
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print (a)
        elif a > b:
            print(b)
    elif a % 2 != 0 or b % 2 != 0:
        #Greater
        if a > b:
            print (a)
        elif a < b:
            print (b)

lesser_of_two_evens(2,4)

def animal_crackers(text):
    text_split = text.split()
    if text_split[0][0] == text_split[1][0]:
        return True
    else: return False

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or (n1 + n2 == 20):
        return True
    else: return False

makes_twenty(20,10)
makes_twenty(2,3)

