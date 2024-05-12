from graphics_dependency import graphics
from check_dependency import control
player_count = 0
player_mark = "X" 
# 1 = x
# 2 = O

def crd():
    while True:
        inp = input("row, col: ")
        coordinates_row = inp.split(",")
        coordinates = [int(coordinates_row[0].strip(" ")),int(coordinates_row[1].strip(" "))]
        coordinates[0] = coordinates[0]-1
        coordinates[1] = coordinates[1]-1
        if -1 < coordinates[0]  < 3 and -1 < coordinates[1]  < 3:
            break
        else: print("Out of range"); continue
        
    return coordinates

def game():
    lst = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
    while True:
        global player_count
        print("Game starts")
        print("Ener via comma(1, 3)")
        while True:
            coordinates = crd()
            print(coordinates)
            print(player_count)
            if (player_count % 2 == 0):
                player_mark = "X"
            else: player_mark = "O"
            if lst[coordinates[0]][coordinates[1]] == 0:
                lst[coordinates[0]][coordinates[1]] = player_mark
            else: 
                print("Position alredy taken")
                continue
            player_count += 1
            graphics(lst)
            if control(lst) == None: #Game continues
                pass
            elif control(lst) == "X":
                print("Player 1 win")
                break
            elif control(lst) == "O":
                print("Player 2 win")
                break
            elif control(lst) == 0:#Board filled
                print("Nichja")
                break
        inp = input("Wanna play again?(Y/N)")
        if inp == "Y":
            lst = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
            player_count = 0
        elif inp == "N": break
        else: pass
game()