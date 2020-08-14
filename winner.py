
# main function 
def board_winner(ls):
    winner = 0
    for i in range(len(ls)):
        # check if player 1 is the winner
        if row(ls, i, 1) or column(ls, i, 1) or diagonals(ls, 1):
            winner = 1
            return winner
            break
        # check if player 2  is the winner
        elif row(ls, i, 2) or column(ls, i, 2) or diagonals(ls, 1):
            winner = 2
            return winner
            break
    # check if it's a tie
    if winner == 0:
        return winner

            
# check if there is a winner in row
def row(ls, row_index, value):
    winner = 0
    for i in ls[row_index]:
        if i == value:
            winner+=1
    if winner == 3:
        return True
    else:
        return False

# check if there is a winner in column
def column(ls, columun_index, value):
    winner = 0
    for i in range(len(ls)):
        if ls[i][columun_index] == value:
            winner+=1
    if winner == 3:
        return True
    else: 
        return False


#check if there is a winner on diagonals (primary or secondary)
def diagonals(ls, value):
    primary, secondary = 0, 0
    length = len(ls)
    for i in range(length):
        if ls[i][i] == value:
            primary+=1
        if ls[i][length-i-1] == value:
            secondary+=1
    if primary == length or secondary == length:
        return True
    else:
        return False
