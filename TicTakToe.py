from helpers import draw_board, check_turn, check_for_win
import os

spots = {1: "1",
         2: "2",
         3: "3",
         4: "4",
         5: "5",
         6: "6",
         7: "7",
         8: "8",
         9: "9"
         }

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
# Reset the screen
    os.system("cls" if os.name == "nt" else "clear")
    draw_board(spots)
    #if Invalid turn occurred, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press q to quit")
    # Get input from player
    choice = input()
    if choice == "q":
        playing = False
        # Check if player gave a number 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if spot has already been taken
        if not spots[int(choice)] in ["X", "O"]:
            # valid input
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Check if game has ended
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False    
    
# Out of loop print results
# Draw the board last time
os.system("cls" if os.name == "nt" else "clear")
draw_board(spots)
# Name winner
if complete:
    if check_turn(turn) == "X": print("Player 1 Wins!")
    else: print("Player 2 Wins!")
else:
    print("No Winner")
    
print("Thanks for playing!")