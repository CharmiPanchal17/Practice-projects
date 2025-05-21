##making a tic tac toe game
from random import *

print("--Welcome to the tic tac toe game.--")

def convert_position(position):
    # i is row
    # j is column
    i = (position - 1) // 4
    j = (position - 1) % 4

    return i, j

def tictactable():
#forming 2 lists one avail one original.
    Board= [
                 [  1 ,  2 ,  3 ,  4 ],
                 [  5 ,  6 ,  7 ,  8 ],
                 [  9 , 10 , 11 , 12 ],
                 [ 13 , 14 , 15 , 16 ]
    ]
    avail= list(Board)
    print_table(avail)
    return Board,avail

def print_table(Board):
    print('--------------------')
    for i in Board:
        print('|', end="")
        for j in i:
            if len(str(j)) < 2:
                print(' ' + str(j), end=" | ")
            else:
                print(j, end=" | ")
        print('\n--------------------')

def selecting_letter():

    #asking user the letter they want.
    Player= input("Please choose a letter X or O. : ").upper()
    print("you  chose letter : " , Player)

    if Player == "X" or Player == "O":
        return Player
    else:
        print("Invalid input. Please select X or O.")

def selecting_position(avail, Player):
    Computer = getting_computer_letter(Player)

    invalid = True
    while invalid:
        #getting user positions.
        userinput = int(input("Please select your position.: "))
        i, j = convert_position(userinput)
        if avail[i][j] == "X" or avail[i][j] == "O":
            print("Already taken. Please try again.")
        else:
            avail[i][j] = Player
            invalid = False
    
    #getting  an answer from the computer.
    invalid = True
    while invalid:
        computerinput = randint(0,16)
        i, j = convert_position(computerinput)
        if avail[i][j] == "X" or avail[i][j] == "O":
            print(i, j)
        else:
            avail[i][j] = Computer
            print("Computer chooses ", computerinput)
            invalid = False

def getting_computer_letter(Player):
    if Player == "X":
        Computer = "O"
    elif Player == "O":
        Computer = "X"

    return Computer



# where letter is either X or O
def getting_the_winner(avail, letter) -> bool:
    if avail[0][0] == letter and avail[0][1] == letter and avail[0][2] == letter and avail[0][3] == letter:
        return True
    if avail[1][0] == letter and avail[1][1] == letter and avail[1][2] == letter and avail[1][3] == letter:
        return True
    if avail[2][0] == letter and avail[2][1] == letter and avail[2][2] == letter and avail[2][3] == letter:
        return True
    if avail[3][0] == letter and avail[3][1] == letter and avail[3][2] == letter and avail[3][3] == letter:
        return True
    if avail[0][0] == letter and avail[1][0] == letter and avail[2][0] == letter and avail[3][0] == letter:
        return True
    if avail[0][1] == letter and avail[1][1] == letter and avail[2][1] == letter and avail[3][1] == letter:
        return True
    if avail[0][2] == letter and avail[1][2] == letter and avail[2][2] == letter and avail[3][2] == letter:
        return True
    if avail[0][3] == letter and avail[1][3] == letter and avail[2][3] == letter and avail[3][3] == letter:
        return True
    if avail[0][0] == letter and avail[1][1] == letter and avail[2][2] == letter and avail[3][3] == letter:
        return True
    if avail[0][3] == letter and avail[1][2] == letter and avail[2][2] == letter and avail[3][0] == letter:
        return True
    if avail[0][1] == letter and avail[2][2] == letter and avail[2][3] == letter:
        return True
    if avail[0][2] == letter and avail[1][1] == letter and avail[2][0] == letter:
        return True   
    if avail[1][0] == letter and avail[2][1] == letter and avail[3][2] == letter:
        return True
    if avail[1][3] == letter and avail[2][2] == letter and avail[3][1] == letter:
        return True
    
    return False

Player = selecting_letter()
Board, avail = tictactable()

game_over = False

while not game_over:
    selecting_position(avail, Player)
    print_table(avail)
    
    did_player_win = getting_the_winner(avail, Player)
    did_computer_win = getting_the_winner(avail, getting_computer_letter(Player))

    if did_player_win:
        print("Player won")
        game_over = True
    elif did_computer_win:
        print("Computer won")
        game_over = True
    elif did_computer_win and did_player_win:
        print("its a tie")
        game_over = True