
print("\n TIC TAC TOE \n")
print ("Choose players X and O.  Whoever's turn it is, type the number that corresponds with the spot you want your mark. First to get 3 in a row, column or diagonal wins.")

# 3x3 Grid with numbers 1-9
def grid():
    print("""
    1|2|3
    -----
    4|5|6
    -----
    7|8|9
    """.format())

grid() 

#Variables are to keep track of the series.
#will be xw within functions
x_wins = 0
#will be ow within functions
o_wins = 0
#will be dr within functions
draws = 0
#when it's x's turn to start a game
x_starts = True

def new_game(xw, ow, dr, starter):
    game_on = True
    
    pos = [" "," "," "," "," "," "," "," "," "]
    # Turn count 
    if starter == True:
        #X starts the game
        turn = 1
        #For O to start the next game
        starter = False
    else:
        #O starts the game
        turn = 0
        #For X to start the next game
        starter = True

    while game_on:
        
        if turn % 2 == 1:
            player_turn = "X"
        else:
            player_turn = "O"

        print("It is %s's turn" % (player_turn))

        try:
            player_select = int(raw_input("Choose a number location: "))
            if player_select > 0 and player_select < 10:
                if pos[player_select - 1] == " ":
                    # Depending on turn count: place chosen location with X or O.
                    pos[player_select - 1] = player_turn
                else:
                    print ("\n \n Position already taken. Try again")
                    turn -= 1
            else: 
                print ("\n \n Not a valid input. Choose a number between 1-9")
                turn -= 1
        
        except (TypeError, ValueError, NameError):
            print ("\n \n Not a valid input. Choose a number between 1-9")
            turn -= 1

        print("""
        {}|{}|{}
        -----
        {}|{}|{}
        -----
        {}|{}|{}
        """.format(pos[0],pos[1],pos[2],pos[3],pos[4],pos[5],pos[6],pos[7],pos[8]))
        turn += 1

        # If player has 3 in a row, player wins.
        if turn > 4:
            if pos[0] == player_turn and pos[1] == player_turn and pos[2] == player_turn or pos[3] == player_turn and pos[4] == player_turn and pos[5] == player_turn or pos[6] == player_turn and pos[7] == player_turn and pos[8] == player_turn or pos[0] == player_turn and pos[3] == player_turn and pos[6] == player_turn or pos[1] == player_turn and pos[4] == player_turn and pos[7] == player_turn or pos[2] == player_turn and pos[5] == player_turn and pos[8] == player_turn or pos[0] == player_turn and pos[4] == player_turn and pos[8] == player_turn or pos[2] == player_turn and pos[4] == player_turn and pos[6] == player_turn:
                print ("%s WINS!!!" % (player_turn))
                game_on = False
                if player_turn == "X":
                    xw += 1
                else:
                    ow += 1
                

        # If all numbers have been replaced but no one has 3 in a row: It's a draw.
        if starter == False and turn == 10 or starter == True and turn == 9:
                print ("It's a draw!")
                game_on = False
                dr += 1
        
    play_again(xw, ow, dr, starter)
        
def play_again(xw, ow, dr, starter):
    print("\n Series:")
    print ("Number of X wins: %s" % (xw))
    print ("Number of O wins: %s" % (ow))
    print ("Number of Draws: %s \n" % (dr))
    new = str(raw_input("Would you like to play again?  Type y for yes: "))
    if new == 'y' or new == 'Y':
        grid()
        new_game(xw, ow, dr, starter)   

new_game(x_wins, o_wins, draws, x_starts)