


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


import boards
import winner


# testing in progress

# board initialization and creation of base board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
boards.build(board)
moves = 0

# main part of the program
while moves < 9:
    # checking who is on move
    if moves % 2 == 0:
        # Player 1
        # initializing player's desired move
        move = list(map(int, (input('Player 1 - enter you move in {x,y} format! >>> ')).split(',')))
        # checking if the input is valid
        if not (move[0] in range(1,4) and move[1] in range(1,4)):
            print("Invalid input, try again")
        else:
            # checking if field is occupied
            if board[move[0]-1][move[1]-1] == 0:
                board[move[0]-1][move[1]-1] = 1
                # building newly formed board after each move
                boards.build(board)
                moves+=1
            else:
                # warning message that field is occupied
                print("Field is filled, try again!")
    if winner.board_winner(board) == 1:
        print("Winner is Player 1!\n")
        break
    else:
        # Player 2
        # exact same thing as player 1 part of the code
        move = list(map(int, (input('Player 2 - enter you move in {x,y} format! >>> ')).split(',')))
        if move[0] >= 4 or move[1] >= 4 or move[0] <= 0 or move[1] <= 0:
            print("Invalid input, try again")
        else:
            if board[move[0]-1][move[1]-1] == 0:
                board[move[0]-1][move[1]-1] = 2
                boards.build(board)
                moves+=1
            else:
                print("Field is filled, try again!")
    
    if winner.board_winner(board) == 2:
        print("Winner is Player 2!\n")
        break

if winner.board_winner(board) == 0:
        print("It's a tie!\n")
print(board)
    