from IPython.display import clear_output


def display_board(board):
    clear_output()
    print('|---------------|')
    print('| '+board[7]+'  |  '+board[8]+'  |  '+board[9]+' |')
    print('|----|-----|----|')
    print('| '+board[4]+'  |  '+board[5]+'  |  '+board[6]+' |')
    print('|----|-----|----|')
    print('| '+board[1]+'  |  '+board[2]+'  |  '+board[3]+' |')
    print('|---------------|')
    



def player_input():

    marker = ''

    # Keep asking player 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    # Assign Player 2, the oposite marker
    if marker == 'X':
        return('Player 1 is with : X', '\nPlayer 2 is with : O')
    else:
        print('Player 1 is with : O', '\nPlayer 2 is with : X')


def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    
    # WIN TIC TAC TOE? 
    
    # ALL ROWS, and check to see if they all share the same marker?
    return ((board[1] == board[2] == board[3] == mark) or #across bottom
    (board[4] == board[5] == board[6] == mark) or # across middle
    (board[7] == board[8] == board[9] == mark) or # across top
    (board[1] == board[4] == board[7] == mark) or # down left
    (board[2] == board[5] == board[8] == mark) or # down middle
    (board[3] == board[6] == board[9] == mark) or # down right
    (board[3] == board[5] == board[7] == mark) or # diagonal
    (board[1] == board[5] == board[9] == mark)) # diagonal
    # ALL COLUMNS, check too see if marker matches
    # 2 diagonals, check for a match

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True

def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or space_check(board,position):
        position = int(input('Choose a position : (1-9)'))
    return position

def replay():
    
    choice = input('Play again? Yes or No')
    
    return choice == 'Yes'

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here (board, whos first, choose markers x,o)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n')
    if play_game == 'y':
        game_on = True 
    else:
        game_on = False
        

    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player1_marker,position)
            
            # check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 2'
           
        else:
            #Player 2 Turn
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board,player2_marker,position)
            
            # check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    break
                else:
                    turn = 'Player 1'
            
            #pass

    if not replay():
        break