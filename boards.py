# function that creates board at desired size
# install this module by using: import boards
# this package builds board at desired size, but I do not recommend not using size greater than 11
# testing this module I came to conclusion that every board greater than 11x11 does not work very well
# package tested on Python 3.8.2



def build(board_size):
    for i in range(board_size):
        dash(board_size)
        straight(board_size)
    dash(board_size)


# function that creates straight line 

def straight(size):
    print('|' + size * (size * " " + '|'))

# function that creates dash line

def dash(size):
    print(size * f" {size*'-'}")



