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
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.



def make_list_of_free_fields(board):
    free_fields={}
    for row in range(3):
        for column in range(3):
            value=board[row][column]
            if value!="X" and value!="O":
                free_fields[value]=(row,column) #tuple assignment
    return free_fields
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def enter_move(board):
    user_move=int(input("Input field number to put O and win! :  "))
    free_fields=make_list_of_free_fields(board)
    if user_move in free_fields:
        row, col =free_fields[user_move]
        board[row][col]='O' # replacing
        del free_fields[user_move] # deleting certain field from free_fields
    else:
        print("Wrong number of field")
    return None
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields=make_list_of_free_fields(board) #it needs access to the free_fields dict
    move=randrange(1,10)
    while move not in free_fields: #while loop true until find proper number within range 1-9
        move=randrange(1,10)
    row, col = free_fields[move] #assigning row,col to tuple from return of free_fields[move]
    board[row][col] = 'X' #replacing 
    del free_fields[move]
    
    return None

def victory_for(board, sign):
    if ((board[0][1] and board[0][0] and board[0][2]) or (board[1][1] and board[1][0] and board[1][2]) or (board[2][1] and board[2][0] and board[2][2]) or (board[0][0] and board[1][1] and board[2][2]) or (board[0][2] and board[1][1] and board[2][0]) or (board[0][0] and board[1][0] and board[2][0])or (board[0][1] and board[1][1] and board[2][1])or (board[0][2] and board[1][2] and board[2][2]))== sign:
        return True
    else:
        return False
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


# display_board(board)
while True:
    print(make_list_of_free_fields(board))
    draw_move(board) # First computer's move
    if victory_for(board, 'X')==True:
        print("COMPUTER WIN!")
        break
    display_board(board) # Displays board
    enter_move(board) # User move
    if victory_for(board, 'O')==True:
        print("USER WIN!")
        break
    display_board(board) # Displays board