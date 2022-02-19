import colored
from os import system, name


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Initialise Game Board
col = 20
row = 20
board = [[' ' for i in range(col)] for i in range(row)]
clear()
"""
print("\u2655")  # white Alpha
print("\u2656")  # white Omega
print("\u2657")  # white Human
print("\u2658")  # white Normal

print("\u265B")  # black Alpha
print("\u265C")  # black Omega
print("\u265D")  # black Human
print("\u265E")  # black Normal

print("\u2764")  # Rabbits
print("\u25CB")  # Apple
print("X")  # Berries
print("\u25B3")  # Mice
print("\u2606")  # Deer
"""

board[1][1] = "\u2655"
board[0][0] = "\u2656"
board[0][1] = "\u2658"
board[1][0] = "\u2658"
board[0][2] = "\u2658"
board[1][2] = "\u2658"
board[2][2] = "\u2658"
board[2][1] = "\u2658"
board[2][0] = "\u2658"

board[18][18] = "\u265B"
board[19][19] = "\u265C"
board[19][18] = "\u265E"
board[18][19] = "\u265E"
board[19][17] = "\u265E"
board[18][17] = "\u265E"
board[17][17] = "\u265E"
board[17][18] = "\u265E"
board[17][19] = "\u265E"

board[3][3] = "X"
board[3][4] = "X"
board[4][3] = "X"
board[4][4] = "X"
board[15][15] = "X"
board[15][16] = "X"
board[16][15] = "X"
board[16][16] = "X"
board[0][3] = "\u25CB"
board[0][4] = "\u25CB"
board[19][15] = "\u25CB"
board[19][16] = "\u25CB"
board[3][0] = "\u25B3"
board[4][0] = "\u25B3"
board[15][19] = "\u25B3"
board[16][19] = "\u25B3"
board[4][6] = "\u25B3"
board[15][13] = "\u25B3"
board[6][4] = "\u2606"
board[13][15] = "\u2606"

for x in range(0, row):
    for y in range(0, col):
        if (x + y) % 2 == 0:
            if y < col - 1:
                print(colored.fg('blue') + colored.bg('white') + " " + board[x][y], end=" " + colored.attr('reset'))
            else:
                print(colored.fg('blue') + colored.bg('white') + " " + board[x][y], end=" " + colored.attr('reset'))
                print("")
        else:
            if y < col - 1:
                print(colored.fg('yellow') + colored.bg('black') + " " + board[x][y], end=" " + colored.attr('reset'))
            else:
                print(colored.fg('yellow') + colored.bg('black') + " " + board[x][y], end=" " + colored.attr('reset'))
                print("")
