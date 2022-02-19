import colored
from os import system, name


# function who clear CMD
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


# Get data from ino file
def get_data():
    datajoueur = {}
    datajoueur2 = {}
    date_foods = {}
    fh = open("groupe_15.ano", "r")
    lines = fh.readlines()
    cpt = 0
    datajoueur["normal"] = []
    datajoueur2["normal"] = []
    date_foods["berries"] = []
    date_foods["apples"] = []
    date_foods["nice"] = []
    date_foods["rabbits"] = []
    date_foods["deers"] = []
    for line in lines:
        take = line.split()

        for num in take:

            if take[0] == '1' and 1 <= cpt <= 150:
                if take[3] == "alpha":
                    datajoueur["alpha"] = [int(take[1]), int(take[2])]
                if take[3] == "omega":
                    datajoueur["omega"] = [int(take[1]), int(take[2])]
                if take[3] == "normal":
                    datajoueur["normal"] += [[int(take[1]), int(take[2])]]
            if take[0] == "2":
                if take[3] == "alpha":
                    datajoueur2["alpha"] = [int(take[1]), int(take[2])]
                if take[3] == "omega":
                    datajoueur2["omega"] = [int(take[1]), int(take[2])]
                if take[3] == "normal":
                    datajoueur2["normal"] += [[int(take[1]), int(take[2])]]
        cpt += 1
    for line in lines:
        take = line.split()
        if (take[0] == "4" and take[1] == "4") or (take[0] == "4" and take[1] == "5") or (
                take[0] == "5" and take[1] == "4") or take[0] == "5" and take[1] == "5" or (
                take[0] == "16" and take[1] == "16") or (take[0] == "16" and take[1] == "17") or (
                take[0] == "17" and take[1] == "16") or (take[0] == "17" and take[1] == "17"):
            date_foods["berries"] += [[int(take[0]), int(take[1]), int(take[3])]]
        if (take[0] == "1" and take[1] == "4") or (take[0] == "1" and take[1] == "5") or (
                take[0] == "20" and take[1] == "16") or (take[0] == "20" and take[1] == "17"):
            date_foods["apples"] += [[int(take[0]), int(take[1]), int(take[3])]]
        if (take[0] == "4" and take[1] == "1") or (take[0] == "5" and take[1] == "1") or (
                take[0] == "16" and take[1] == "20") or (take[0] == "17" and take[1] == "20"):
            date_foods["nice"] += [[int(take[0]), int(take[1]), int(take[3])]]
        if (take[0] == "5" and take[1] == "7") or (take[0] == "16" and take[1] == "14"):
            date_foods["rabbits"] += [[int(take[0]), int(take[1]), int(take[3])]]
        if (take[0] == "7" and take[1] == "5") or (take[0] == "14" and take[1] == "16"):
            date_foods["deers"] += [[int(take[0]), int(take[1]), int(take[3])]]

    return datajoueur, datajoueur2, date_foods


# Initialise Game Board
def init_board(col=20, row=20):
    """
    :param col: le nombre de colonnes pour le plateau de jeu
    :param row: le nombre de lignes pour le plateau de jeu
    :return: pas de return mais affiche le plateau du jeu

    Version
    --------
    specification: Pongoli Alessandro (v.1 19/02/21)
    """
    board = [[' ' for i in range(col)] for i in range(row)]

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

    clear()
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
                    print(colored.fg('yellow') + colored.bg('black') + " " + board[x][y],
                          end=" " + colored.attr('reset'))
                else:
                    print(colored.fg('yellow') + colored.bg('black') + " " + board[x][y],
                          end=" " + colored.attr('reset'))
                    print("")


# init_board()
datajoueur, datajoueur2, date_foods = get_data()
print(datajoueur)
print("\n")
print(datajoueur2)
print("\n")
print(date_foods)
