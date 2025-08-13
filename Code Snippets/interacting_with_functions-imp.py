from random import shuffle

mylist = [' ', 'O', ' ']

def shuffle_list(mylist):
    shuffle(mylist)
    return (mylist)

def user_guess():
    guess = ""
    while guess not in ['0', '1', '2']:
        guess = input("Enter 0, 1 or 2: ")
    
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct, you've won this round!")
        print(mylist)
    else:
        print("Wrong guess!")
        print(mylist)

mixedup_list = shuffle_list(mylist)

guess = user_guess()

check_guess(mixedup_list, guess)