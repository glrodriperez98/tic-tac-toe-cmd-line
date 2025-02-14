
## HANDLES DISPLAY BOARD AND UPDATES DURING GAME

from tic_tac_toe.utils import clear_screen

#Display board
def display_board(board):
    #print command below is a really *ugly* solution to prevent board repitition...need better solution
    clear_screen()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#Place marker
def place_marker(board, marker, position):
    board[position] = marker

#Space check
def space_check(board, position):
    
    return board[position] == ' '

#Full board check
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #BOARD IS FULL IF RETURNS TRUE
    return True

#Win board check in all directions
def win_check(board,mark):

    #CHECK ALL ROWS, COLUMNS AND DIAGONALS, and check to see if they all share the same marker
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
