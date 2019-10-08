import random

the_board = {'top-l':' ', 'top-m':' ','top-r':' ',
             'mid-l':' ', 'mid-m':' ','mid-r':' ',
             'low-l':' ', 'low-m':' ','low-r':' '}
current_letter ='X'
game_still_going =True

# to display the board
def display_board(board):
    print(board['top-l']+'|'+ board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l']+'|'+ board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l']+'|'+ board['low-m'] + '|' + board['low-r'])

# to decide which player starts the game  
def who_starts(player_one, player_two): 
     if random.randint(0, 1) == 0:
         return(print(player_one + ' goes first'))
     else:
          return(print(player_two + ' goes first')) 
    
# to play the game
def play_game():
    # display initial board positions
    display_board(the_board)  
    while game_still_going:
        handle_moves(current_letter)

        # check if game over
        if_game_over(the_board, current_letter)

        # change turn
        flip_player()
        
    return


# to handle moves between the two players
def handle_moves(letter):
    while True:
        print( ' top-l = Top Left \n top-m = Top Middle \n top-r = Top Right')
        print( ' mid-l = Middle Left \n mid-m = Middle Middle \n mid-r = Middle Right') 
        print( ' low-l = Lower Left \n low-m = Lower Middle \n low-r = Lower Right')
        position = input('\n Enter the position where you want to insert:\n')

        if the_board.get(position, ' ') !=' ':
            print('The position is already filled. Please enter another position: ')
            continue

        the_board[position] = letter
        display_board(the_board)
        return position


# to check if the game is over (if there is a winner or its a tie)
def if_game_over(board, letter):
    if (board['top-l'] == board['top-m'] == board['top-r']!=' ' or 
    board['mid-l'] == board['mid-m'] == board['mid-r']!=' ' or 
    board['low-l'] == board['low-m'] == board['low-r']!=' ' or  
    board['top-l'] == board['mid-l'] == board['low-l']!=' ' or 
    board['top-m'] == board['mid-m'] == board['low-m']!=' ' or 
    board['top-r'] == board['mid-r'] == board['low-r']!=' ' or 
    board['top-l'] == board['mid-m'] == board['low-r']!=' ' or 
    board['top-r'] == board['mid-m'] == board['low-l']!=' '):
        print('winner is '+letter)
        

# change turns
def flip_player():
  global current_letter
  # If the current player was X, make it O
  if current_letter == 'X':
    current_letter = 'O'
  # Or if the current player was O, make it X
  elif current_letter == 'O':
    current_letter = 'X'
     

player_one = input('Enter first player name:')
player_two = input('Enter second player name:')
# print('Player one : '+player_one +'\n'+ 'Player two : '+player_two)

who_starts(player_one, player_two)
play_game()



