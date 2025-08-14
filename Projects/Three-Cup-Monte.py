from random import shuffle

mylist = [' ', 'O', ' ']


def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Enter 0, 1 or 2: ")
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct! You've won this round")
        print(mylist)
        
    else:
        print("Wrong Guess!")
        print(mylist)
    return (mylist, guess)

while True:
        mylist = shuffle_list(mylist)

        guess = player_guess()

        mixed = check_guess(mylist, guess)