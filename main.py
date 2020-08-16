


# Tic Tac Toe game will be developed in 4 stages

# 1st stage - drawing a board game
# 2nd stage - check tic tac toe
# 3rd stage - tic tac toe draw 
# 4th stage - finalization and adding details

# idea & developing plan: practicepython.org 
# author : stefan jovicevic
# github: github.com/sjovicevic
# august 2020
# serbia

# NOTICE: main.py cannot work without boards.py & winner.py modules

import boards
import winner
import os


def initialization(player_num):
    if player_num == 'X':
        return list(map(int, (input('Player 1 (X) >>> ')).split(',')))
    else:
        return list(map(int, (input('Player 2 (O) >>> ')).split(',')))

def validation(element):
    if element[0] in range(1,4) and element[1] in range(1,4):
        return True

# main part of the program
def machinery(board, value, moves, win):
     # player
        # initializing player's desired move
        move = initialization(value)
        # checking if the input is valid
        if not validation(move):
            print("Invalid input, try again")
        else:
            # checking if field is occupied
            if board[move[0]-1][move[1]-1] == '.':
                board[move[0]-1][move[1]-1] = value
                # building newly formed board after each move
                boards.build(board)
                # making sure player played his move
                moves+=1
            else:
                print("Field is filled, try again!")
        
        # if player is winner 
        if winner.board_winner(board, value) == value:
            print(f"Winner is Player {value}!\n")
            # win is useful because last if, out of while loop check if there is a winner
            win = True
        return win, moves

def play():
    board = [['.','.','.'], ['.','.','.'], ['.','.','.']]
    boards.build(board)
    moves = 0
    win = False

    # main part of the program
    while moves < 9:
        # checking who is on move
        if moves % 2 == 0:
            win, moves = machinery(board, 'X', moves, win)
            if win:
                break
        else:
            win, moves = machinery(board, 'O', moves, win)
            if win:
                break


    if not win:
        print("It's a tie!")
    




# making sure if someone sometimes use this as a independent module

if __name__ == '__main__':
    # board initialization and creation of base board
    if (input('Do you need tutorial? y/n >>> ')).lower() == 'y':
        print("""
            Tic-tac-toe or Xs and Os is a game for two players, X and O, 
            who take turns marking the spaces in a 3×3 grid. 
            The player who succeeds in placing three of their marks
            in a horizontal, vertical, or diagonal row is the winner.
            Marking is done with x,y format where x is row number, y is column number.

            e.g. 
            
            Player 1 (X) >>> 2,3
        
        """)
    while (input('Play? y/n >>> ')).lower() == 'y':
        os.system('clear')
        print('______________________________________________________________________________')
        play()



# testing finished, hopefully everything works!
