# step 1 - draw the board
# step 2 - ask player if he is playing X or O
# step 3 - separate board on 9 numbered fields
# add player info for mark that is playing
# add player names input ?
# step 4 - ask player for number 1-9 according to num fields
# reset board view after each player move
# make rulls for player wins
# ask player if he is going to play again

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
    


# test_board = [' ']*10
# display_board(test_board)

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


player_input()
