# Создайте программу для игры в ""Крестики-нолики"".

list = [i for i in range(1, 10)] # поле из 9 ячеек: 3 строки, 3 столбца
victory =   [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] # условия победы - 8 вариантов
def print_list(list): # рисуем поле
    print('-' * 13)
    for i in range(3):
        print('>', list[0 + i * 3],'|', list[1 + i * 3], '|', list[2 + i * 3], '<')
        print('-' * 13)
def moving(step, symbol):
    index = list.index(step)
    list[index] = symbol

def get_result(name_player1, name_player2):
    win = ""
    for i in victory:
        if list[i[0]] == "X" and list[i[1]] == "X" and list[i[2]] == "X":
            win = name_player1
        if list[i[0]] == "O" and list[i[1]] == "O" and list[i[2]] == "O":
            win = name_player2       
    return win
    
name_player1 = input("Введите имя первого игрока: ")
name_player2 = input("Введите имя второго игрока: ")
game_over = False
player1 = True

while game_over == False:
    print_list(list)
    if player1 == True:
        symbol = "X"
        step = int(input(f"{name_player1}, ходите: "))
    else:
        symbol = "O"
        step = int(input(f"{name_player2}, ходите: "))
    moving(step,symbol)
    win = get_result(name_player1, name_player2)
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)
           
print_list(list)
print("Победил" if win != "" else "Ничья")

