


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


# testing

moves = 0
move = 0
while moves <= 4:
    if moves % 2 == 0:
        move = (input("Player 1 - Enter your position in {x,y} format >>> ")).split(',')
        print(move)
    else:
        move = (input("Player 2 - Enter your position in {x,y} format >>> ")).split(',')
        print(move)
    moves+=1


