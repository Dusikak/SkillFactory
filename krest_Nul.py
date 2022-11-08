def privet():
    print("-------------------")
    print("  Крестики-Нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print("   через пробел    ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")



field = [
    [
        " ",
    ]
    * 3
] * 3
# print(field)

# field[2] = "X"
# print((field[2]))


def sshow():
    print()
    print(f"   | 0 | 1 | 2 |")
    print("---------------")
    # print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}") # вариант 1 рисования клеток
    # print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}") # вариант 1 рисования клеток
    # print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}") # вариант 1 рисования клеток
    # for i in range(3): # вариант 2 рисования клеток
    #     print(f"{i} |{field[i][0]}  | {field[i][1]} | {field[i][2]} |")  # вариант 2 рисования клеток
    #     print("---------------")
    for i, row in enumerate(field):  # вариант 3 рисования клеток
        row_info = f" {i} | {' | '.join(row)} | "  # вариант 3 рисования клеток
        print(row_info)  # вариант 3 рисования клеток
        print("---------------")  # вариант 3 рисования клеток
    print()


# ввод пользователи
def vvod():  # первый вариант ввода

    # x, y = map(int, input("      введите координаты: ").split()) # первый вариант ввода
    #     return x,y # первый вариант ввода
    # x, y  = vvod() # первый вариант ввода
    # print(field([x][y])) # первый вариант ввода
    # print(sshow()) # первый вариант ввода
    while True:
        coordin = input("         Ваш ход: ").split()

        if len(coordin) != 2:
            print("Введите 2 значения! ")
            continue

        x, y = coordin

        if not (x.isnumeric()) or not (y.isnumeric()):  # проверка на числа
            print(("Введите числа! "))
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 and y > 0 or y > 2:  # проверяем на координаты
            # if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты за пределами игрового поля")

        if field[x][y] != " ":
            print(("Клетка занята! "))
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False
    

privet()
field = [[" "] * 3 for i in range(3) ]
num_hod = 0
while True:
    num_hod += 1
    sshow()  # обновляем игровое поле
    if num_hod % 2 == 1:
        print(" Ход крестикп!")
    else:
        print(" Ход нолика!")
    
    x, y = vvod()
    
    if num_hod % 2 == 1:   # заполняем игровое поле по координатам
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    
    if check_win():
        break
    
    if num_hod == 9:
        print(" Ничья!")
        break