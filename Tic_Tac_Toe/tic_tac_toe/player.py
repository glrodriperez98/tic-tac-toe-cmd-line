
##HANDLES PLAYER-RELATED LOGIC (INPUT, TURN MANAGEMENT, MARKER CHOICE)

from tic_tac_toe.board import space_check

#Player marker input
def player_input():
    
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Choose who goes first at random
def choose_first():
    import random
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Player choice of marker position
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
