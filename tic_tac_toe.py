from random import randrange
from copy import deepcopy
board=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
def display_board(board):
    print("+-----+",end="")
    print("-----",end="")
    print("+-----+")#top
    print("|     |     |     |")
    print(f"|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")  #row index 0
    print("|     |     |     |")
    print("+-----+",end="")
    print("-----",end="")
    print("+-----+")#center
    print("|     |     |     |")
    print(f"|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |") #row index 1
    print("|     |     |     |")
    print("+-----+",end="")
    print("-----",end="")
    print("+-----+")#center
    print("|     |     |     |")
    print(f"|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |") #row index 2
    print("|     |     |     |")
    print("+-----+",end="")
    print("-----",end="")
    print("+-----+")#bottom
    
    return None
display_board(board)
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


# def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_fields={}
    for row in range(3):
        for column in range(3):
            value=board[row][column]
            if value!="X" and value!="O":
                free_fields[value]=(row,column)
    return free_fields
print(make_list_of_free_fields(board))
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        move=randrange(1,100)
        if any(move in row for row in board): #check if randomized variable move is in board
            break
    print(move)
    return None
draw_move(board)
    
