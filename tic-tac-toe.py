import random

the_board = {'top-l':' ', 'top-m':' ','top-r':' ',
             'mid-l':' ', 'mid-m':' ','mid-r':' ',
             'low-l':' ', 'low-m':' ','low-r':' '}

def display_board(board):
    print(board['top-l']+'|'+ board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l']+'|'+ board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l']+'|'+ board['low-m'] + '|' + board['low-r'])

  
def who_starts(player_one, player_two): 
     if random.randint(0, 1) == 0:
         return(print(player_one + ' goes first'))
     else:
          return(print(player_two + ' goes first')) 
    

def play_game():
    # display initial board positions
    display_board(the_board)  
    return


player_one = input('Enter first player name:')
player_two = input('Enter second player name:')
print('Player one : '+player_one +'\n'+ 'Player two : '+player_two)

who_starts(player_one, player_two)
play_game()


# board
# display board
# play game
# turn handling
# check who won
    # check rows
    # check columns
    # check diagonals
# check tie
#     
