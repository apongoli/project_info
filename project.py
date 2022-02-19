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


# create list board
def create_board(col=20, row=20):
    board = [[' ' for i in range(col)] for i in range(row)]
    return board


# Initialise Game Board
def init_board(col=20, row=20):
    """
    Parameters
    −−−−−−−−−−
    col: le nombre de colonnes pour le plateau de jeu (int, optional)
    row: le nombre de lignes pour le plateau de jeu (int, optional)

    Returns
    −−−−−−−
    Pas de return mais affiche le plateau du jeu

    Version
    --------
    specification: Pongoli Alessandro (v.1 19/02/21)
    """

    board = create_board()

    # Ino file data processing
    datajoueur, datajoueur2, date_foods = get_data()
    white_normal = datajoueur["normal"]
    white_alpha = datajoueur["alpha"]
    white_omega = datajoueur["omega"]

    black_normal = datajoueur2["normal"]
    black_alpha = datajoueur2["alpha"]
    black_omega = datajoueur2["omega"]

    berries = date_foods["berries"]
    apples = date_foods["apples"]
    mice = date_foods["nice"]
    rabbits = date_foods["rabbits"]
    deers = date_foods["deers"]

    # Set coordinate into board list for normal, alpha, omega white objects
    for x in range(len(white_normal)):
        board[white_normal[x][0]-1][white_normal[x][1]-1] = "\u2658"
    board[white_alpha[0]-1][white_alpha[1]-1] = "\u2655"
    board[white_omega[0]-1][white_omega[1]-1] = "\u2656"

    # Set coordinate into board list for normal, alpha, omega black objects
    for x in range(len(black_normal)):
        board[black_normal[x][0]-1][black_normal[x][1]-1] = "\u265E"
    board[black_alpha[0]-1][black_alpha[1]-1] = "\u265B"
    board[black_omega[0]-1][black_omega[1]-1] = "\u265C"

    # Set coordinate into board list for berries, apples, mice, rabbits, deers objects
    for x in range(len(berries)):
        board[berries[x][0]-1][berries[x][1]-1] = "X"
    for x in range(len(apples)):
        board[apples[x][0]-1][apples[x][1]-1] = "\u25CB"
    for x in range(len(mice)):
        board[mice[x][0]-1][mice[x][1]-1] = "\u25B3"
    for x in range(len(rabbits)):
        board[rabbits[x][0]-1][rabbits[x][1]-1] = "\u2764"
    for x in range(len(deers)):
        board[deers[x][0]-1][deers[x][1]-1] = "\u2606"

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


init_board()
