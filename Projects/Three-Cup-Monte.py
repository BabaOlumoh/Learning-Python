from random import shuffle

score = 0 
def shuffle_list(mylist):
    shuffle(mylist)
    return (mylist)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2', '6']:
        guess = input("Enter 0, 1, 2 or 6 to quit: ")
    if guess == '6':
        print("Game closed")
        return None
    return int(guess)


def check_guess(mylist, guess):
    
    if mylist[guess] == 'O':
        print("Correct! You've won this round")
        global score
        score +=1
        print(mylist)

    else:
        print("Wrong Guess!")
        print(mylist)
    return (mylist, guess)


while True:
    mylist = [' ', 'O', ' ']
    mylist = shuffle_list(mylist)
    guess = player_guess()
    counter =+ 1

    if guess is None:
        print(f"Player won {score} rounds")
        break
    mixed = check_guess(mylist, guess)
    print(f"Player has won {score} rounds")
    