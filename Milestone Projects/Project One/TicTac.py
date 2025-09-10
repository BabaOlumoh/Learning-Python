def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_input(players):
    marker = "Nil"

    while marker not in ["X","O"]:
        marker = input("Choose either X or O: ").upper()

        if marker == "X":
            player_1 = "X"
            player_2 = "O"
            print(f"{players[0]} is {player_1} and {players[1]} is {player_2}")
        elif marker == "O":
            player_1 = "O"
            player_2 = "X"
            print(f"{players[0]} is {player_1} and {players[1]} is {player_2}")

    return (player_1, player_2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[7] == board[8] == board[9] == mark) or 
            (board[1] == board[4] == board[7] == mark) or 
            (board[2] == board[5] == board[8] == mark) or 
            (board[3] == board[6] == board[9] == mark) or 
            (board[1] == board[5] == board[9] == mark) or 
            (board[3] == board[5] == board[7] == mark))

def player_name():
    player1 = input("Enter your name player 1: ").capitalize()
    player2 = input("Enter your name player 2: ").capitalize()
    return (player1, player2)

import random

def choose_first(players):
    rand = random.randint(0,1)
    if rand == 0:
        print(f"{players[0]} goes first")
        return players[0]  
    else:
        print(f"{players[1]} goes first")
        return players[1] 

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 

def player_choice(board):
    position = 0  
    number_selector = [1,2,3,4,5,6,7,8,9]

    while position not in number_selector or not space_check(board, position):
        try: 
            position = int(input("Position number(1-9): "))
            if position not in number_selector:
                print("Please choose a number between 1-9")
            elif not space_check(board, position):
                print("That position is already taken!")
        except ValueError:
            print("Please enter a valid number")
    return position

def replay():
    while True:  
        play = input("Enter Y to play again or N to exit: ").upper()
        if play == "Y":
            return True
        elif play == "N":
            return False
        else:
            print("Please enter Y or N")

print("Welcome to Tic Tac Toe!")

while True:
    the_board = [' '] * 10
    players = player_name()
    turn = choose_first(players)  
    marker1, marker2 = player_input(players)

    play_game = input("Enter Y to play or N to exit: ").upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## Gameplay
    while game_on:
        if turn == players[0]:
            print(f"\n{players[0]}'s turn:")  
            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, marker1, position)

            if win_check(the_board, marker1):
                display_board(the_board)
                print(f"{players[0]} has won!")
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print("Tie Game!")
                game_on = False
            else:
                turn = players[1]

        else:  
            print(f"\n{players[1]}'s turn:")
            display_board(the_board)

            position = player_choice(the_board)
            place_marker(the_board, marker2, position)

            if win_check(the_board, marker2):
                display_board(the_board)
                print(f"{players[1]} has won!")
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print("Tie Game!")
                game_on = False
            else:
                turn = players[0]
    
    if not replay():
        print("Game Over!!!")
        break