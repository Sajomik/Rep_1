map=[1,2,3,
     4,5,6,
     7,8,9]

def print_map(map):
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])
print_map(map)

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
def cell_symbol():
    if symbol == "X":
        map[ind] = "X"
    elif symbol == "O":
        map[ind] = "O"
    else:
        print("Неправильно введен символ")

def check_win():
    win = ""
    for i in victories:
      if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
        win='X'
      if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
        win='O'
    return win

victory = False

while victory == False:
    print("Игрок, выберете клетку и введите ваш символ")
    cell = int(input("номер клетки:"))
    if 1<=cell<=9:
        None
    else: print("Неправильно введен номер клетки")
    symbol = input("Ваш символ(X/O):")
    ind = map.index(cell)
    cell_symbol()
    print_map(map)

    win = check_win()
    if win !="":
        victory = True
    else:
        victory = False

print('Победа', win)





