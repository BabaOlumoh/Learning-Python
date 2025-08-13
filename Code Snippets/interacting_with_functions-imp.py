from random import shuffle

mylist = [' ', 'O', ' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return (mylist)

def user_guess():
    guess = ""
    while guess not in ['0', '1', '2']:
        guess = input("Enter 0,1 or 2")
    
    return int(guess)

