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


# Get data from ano file
def get_data():
    datajoueur = {}
    datajoueur2 = {}
    date_maps = {}
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
    date_maps["maps"] = []

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
        if (take[0] == "20") and (take[1] == "20"):
            date_maps["maps"] = [[int(take[0]), int(take[1])]]
    return datajoueur, datajoueur2, date_foods, date_maps


# create var for get_data return and create var for map size
datajoueur, datajoueur2, date_foods, date_maps = get_data()
col_data = date_maps["maps"][0][0]
row_data = date_maps["maps"][0][1]

# Supprimer les doublons
normal_team1_raw = datajoueur["normal"]
normal_team1 = []
for i in normal_team1_raw:
    if i not in normal_team1:
        normal_team1.append(i)
datajoueur["normal"] = normal_team1
normal_team2_raw = datajoueur2["normal"]
normal_team2 = []
for i in normal_team2_raw:
    if i not in normal_team2:
        normal_team2.append(i)
datajoueur2["normal"] = normal_team2

# create dict game
temp_dict_team1 = {}
for x in range(len(datajoueur["normal"])):
    temp_dict_team1["(" + str(datajoueur["normal"][x][0]) + "," + str(datajoueur["normal"][x][1]) + ")"] = \
        ["normal", 100]
temp_dict_team1["(" + str(datajoueur["alpha"][0]) + "," + str(datajoueur["alpha"][1]) + ")"] = ["alpha", 100]
temp_dict_team1["(" + str(datajoueur["omega"][0]) + "," + str(datajoueur["omega"][1]) + ")"] = ["omega", 100]
team1 = temp_dict_team1

temp_dict_team2 = {}
for x in range(len(datajoueur2["normal"])):
    temp_dict_team2["(" + str(datajoueur2["normal"][x][0]) + "," + str(datajoueur2["normal"][x][1]) + ")"] = ["normal",
                                                                                                              100]
temp_dict_team2["(" + str(datajoueur2["alpha"][0]) + "," + str(datajoueur2["alpha"][1]) + ")"] = ["alpha", 100]
temp_dict_team2["(" + str(datajoueur2["omega"][0]) + "," + str(datajoueur2["omega"][1]) + ")"] = ["omega", 100]
team2 = temp_dict_team2

temp_dict_foods = {}
for x in range(len(date_foods["berries"])):
    temp_dict_foods["(" + str(date_foods["berries"][x][0]) + "," + str(date_foods["berries"][x][1]) + ")"] = \
        ["berries", date_foods["berries"][x][2]]
for x in range(len(date_foods["apples"])):
    temp_dict_foods["(" + str(date_foods["apples"][x][0]) + "," + str(date_foods["apples"][x][1]) + ")"] = \
        ["apples", date_foods["apples"][x][2]]
for x in range(len(date_foods["nice"])):
    temp_dict_foods["(" + str(date_foods["nice"][x][0]) + "," + str(date_foods["nice"][x][1]) + ")"] = \
        ["nice", date_foods["nice"][x][2]]
for x in range(len(date_foods["rabbits"])):
    temp_dict_foods["(" + str(date_foods["rabbits"][x][0]) + "," + str(date_foods["rabbits"][x][1]) + ")"] = \
        ["rabbits", date_foods["rabbits"][x][2]]
for x in range(len(date_foods["deers"])):
    temp_dict_foods["(" + str(date_foods["deers"][x][0]) + "," + str(date_foods["deers"][x][1]) + ")"] = \
        ["deers", date_foods["deers"][x][2]]
foods = temp_dict_foods
game = {"MAP": date_maps["maps"], "WEREWOLVES": {"TEAM_1": team1, "TEAM_2": team2}, "FOODS": foods}


# create list board
def create_board(col=col_data, row=row_data):
    """ Create the empty board list with the chosen size
    Parameters
    −−−−−−−−−−
    col: le nombre de colonnes pour le plateau de jeu (int, optional)
    row: le nombre de lignes pour le plateau de jeu (int, optional)

    Returns
    −−−−−−−
    board: la liste board avec la taille choisie

    Version
    --------
    specification: Pongoli Alessandro (v.1 20/02/21)
    """

    board = [[' ' for i in range(col)] for i in range(row)]
    return board


def board(board_list=create_board(), game=game):
    """ Set board dict and show it on terminal with the last version of it too
        Parameters
        −−−−−−−−−−
        board_list: la liste board vide (list)
        game: le dictionnaire game (dict)

        Returns
        −−−−−−−
        Pas de return mais affiche le plateau du jeu

        Version
        --------
        specification: Pongoli Alessandro (v.1 20/02/21)
        """
    list_board = board_list
    board = {}

    team1_normal = []
    team1_alpha = []
    team1_omega = []

    team2_normal = []
    team2_alpha = []
    team2_omega = []

    berries = []
    apples = []
    mice = []
    rabbits = []
    deers = []

    characters = "()"

    for key in game["WEREWOLVES"]["TEAM_1"].keys():
        item = key
        for x in range(len(characters)):
            item = item.replace(characters[x], "")
        item = item.split(",")
        item = [int(i) for i in item]
        item.append(game["WEREWOLVES"]["TEAM_1"][key][1])
        if game["WEREWOLVES"]["TEAM_1"][key][0] == "normal":
            team1_normal.append(item)
        if game["WEREWOLVES"]["TEAM_1"][key][0] == "omega":
            team1_omega.append(item)
        if game["WEREWOLVES"]["TEAM_1"][key][0] == "alpha":
            team1_alpha.append(item)

    for key in game["WEREWOLVES"]["TEAM_2"].keys():
        item = key
        for x in range(len(characters)):
            item = item.replace(characters[x], "")
        item = item.split(",")
        item = [int(i) for i in item]
        item.append(game["WEREWOLVES"]["TEAM_2"][key][1])
        if game["WEREWOLVES"]["TEAM_2"][key][0] == "normal":
            team2_normal.append(item)
        if game["WEREWOLVES"]["TEAM_2"][key][0] == "omega":
            team2_omega.append(item)
        if game["WEREWOLVES"]["TEAM_2"][key][0] == "alpha":
            team2_alpha.append(item)

    for key in game["FOODS"].keys():
        item = key
        for x in range(len(characters)):
            item = item.replace(characters[x], "")
        item = item.split(",")
        item = [int(i) for i in item]
        item.append(game["FOODS"][key][1])
        if game["FOODS"][key][0] == "berries":
            berries.append(item)
        if game["FOODS"][key][0] == "apples":
            apples.append(item)
        if game["FOODS"][key][0] == "mice":
            mice.append(item)
        if game["FOODS"][key][0] == "rabbits":
            rabbits.append(item)
        if game["FOODS"][key][0] == "deers":
            deers.append(item)

    # Set coordinate into board list for normal, alpha, omega team1 objects
    for x in range(len(team1_normal)):
        list_board[team1_normal[x][0] - 1][team1_normal[x][1] - 1] = "\u2658"
    list_board[team1_alpha[0][0] - 1][team1_alpha[0][1] - 1] = "\u2655"
    list_board[team1_omega[0][0] - 1][team1_omega[0][1] - 1] = "\u2656"

    # Set coordinate into board list for normal, alpha, omega team2 objects
    for x in range(len(team2_normal)):
        list_board[team2_normal[x][0] - 1][team2_normal[x][1] - 1] = "\u265E"
    list_board[team2_alpha[0][0] - 1][team2_alpha[0][1] - 1] = "\u265B"
    list_board[team2_omega[0][0] - 1][team2_omega[0][1] - 1] = "\u265C"

    # Set coordinate into board list for berries, apples, mice, rabbits, deers objects
    for x in range(len(berries)):
        list_board[berries[x][0] - 1][berries[x][1] - 1] = "X"
    for x in range(len(apples)):
        list_board[apples[x][0] - 1][apples[x][1] - 1] = "\u25CB"
    for x in range(len(mice)):
        list_board[mice[x][0] - 1][mice[x][1] - 1] = "\u25B3"
    for x in range(len(rabbits)):
        list_board[rabbits[x][0] - 1][rabbits[x][1] - 1] = "\u2764"
    for x in range(len(deers)):
        list_board[deers[x][0] - 1][deers[x][1] - 1] = "\u2606"

    board["board"] = list_board

    # Set list for show energy on terminal
    team1_all = []
    for x in range(len(team1_normal)):
        temp_team = team1_normal[x]
        temp_team.append("normal")
        team1_all.append(temp_team)
    temp_team = team1_alpha[0]
    temp_team.append("alpha")
    team1_all.append(temp_team)
    temp_team = team1_omega[0]
    temp_team.append("omega")
    team1_all.append(temp_team)

    team2_all = []
    for x in range(len(team2_normal)):
        temp_team = team2_normal[x]
        temp_team.append("normal")
        team2_all.append(temp_team)
    temp_team = team2_alpha[0]
    temp_team.append("alpha")
    team2_all.append(temp_team)
    temp_team = team2_omega[0]
    temp_team.append("omega")
    team2_all.append(temp_team)

    foods_energy = {"berries": 10, "apples": 30, "nice": 50, "rabbits": 100, "deers": 500}
    # show board
    clear()
    list_num = ["0 ", "1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "11", "12", "13", "14", "15", "16",
                "17", "18", "19"]
    print("   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19")  # Affiche les numeros horizontal
    for x in range(0, row_data):
        print(list_num[x], end="")  # Affiche les numeros vertical
        for y in range(0, col_data):
            if (x + y) % 2 == 0:
                if y < col_data - 1:
                    print(colored.fg('blue') + colored.bg('white') + " " + board["board"][x][y],
                          end=" " + colored.attr('reset'))
                else:
                    print(colored.fg('blue') + colored.bg('white') + " " + board["board"][x][y],
                          end=" " + colored.attr('reset'))
                    if 0 < x < 9:
                        print(" Team1", team1_all[x][3], "coordinate:", team1_all[x][0], team1_all[x][1],
                              "Energy:", team1_all[x][2], "| Team2", team2_all[x][3], "coordinate:", team2_all[x][0],
                              team2_all[x][1], "Energy:", team2_all[x][2])
                    if x == 9:
                        print(" Berries Energy:", foods_energy["berries"], "| Apples Energy:", foods_energy["apples"])
                    if x == 11:
                        print(" Deers Energy:", foods_energy["deers"])
                    if x >= 12:
                        print("")
            else:
                if y < col_data - 1:
                    print(colored.fg('yellow') + colored.bg('black') + " " + board["board"][x][y],
                          end=" " + colored.attr('reset'))
                else:
                    print(colored.fg('yellow') + colored.bg('black') + " " + board["board"][x][y],
                          end=" " + colored.attr('reset'))
                    if 0 <= x < 9:
                        print(" Team1", team1_all[x][3], "coordinate:", team1_all[x][0], team1_all[x][1],
                              "Energy:", team1_all[x][2], "| Team2", team2_all[x][3], "coordinate:", team2_all[x][0],
                              team2_all[x][1], "Energy:", team2_all[x][2])
                    if x == 10:
                        print(" Nice Energy:", foods_energy["nice"], "| Rabbits Energy:", foods_energy["rabbits"])
                    if x >= 12:
                        print("")


board()
