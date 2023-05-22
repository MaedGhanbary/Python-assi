from termcolor import colored
from pyfiglet import Figlet
f = Figlet(font='banner3-D')
n = 0
print (colored(f.renderText('Welcome to Tic Tac Toe *.*'), 'light_yellow'))
def win1() :
    print(colored(f.renderText("WOW Player1 Won XD" ),'green'))
    quit()

def win2():
    print(colored(f.renderText("WOW player2 Won XD"),'green'))
    quit()

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()
 
def check_game():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        win1()
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        win1()
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        win1()
    elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        win1()
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        win1()
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        win1()
    elif game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        win1()
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        win1()

def check_gamee():
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O" :
        win2()
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        win2()
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        win2()
    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        win2()
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        win2()
    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        win2()
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        win2()
    elif game_board[2][0] == "O" and game_board[1][1] == "O" and game_board[0][2] == "O":
        win2()
    

game_board = [["-" , "-" , "-"],
              ["-" , "-" , "-"],
              ["-" , "-" , "-"]]
show()
while True:
    n += 1
    print("Player1")
    while True:
        row = int(input("Enter row: "))-1
        col = int(input("Enter col: "))-1
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if game_board[row][col] == "-" :
                game_board [row][col] = "X"
                break
            else:
                print("Chooe anther cell!!")
        else:
            print("Choose in range [1,3]")
    show()
    check_game()
    if n == 5 :
        print(colored(f.renderText("Oops no one won :("),'red'))
        quit()
    
    print("Player2")
    while True:
        row = int(input("Enter row: "))-1
        col = int(input("Enter col: "))-1
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if game_board[row][col] == "-" :
                game_board [row][col] = "O"
                break
            else:
                print("Chooe anther cell!!") 
        else:
            print("Choose in range [1,3]")   
    show()
    check_gamee()