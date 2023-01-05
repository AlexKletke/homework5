# Создайте программу для игры с конфетами человек против бота. Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

from random import randint as r
def takecandies(name):
    taken_candies = int(input(f"{name}, сколько конфет хочешь взять: от 1 до 28? "))
    while taken_candies < 1 or taken_candies > 28:
        taken_candies = int(input(f"{name}, бери еще: от 1 до 28 "))
    return taken_candies

def bot(candies):
    random = r(1, 29)
    while candies - random <= 28 and candies > 29:
        random = r(1, 29)
    return random

Human = input("Имя человека: ")
Namebot = input("Имя бота: ")
candies = 2021
step = r(0, 2) # жеребьевка
print(f"{Human if step == 1 else Namebot}, ходит первым")

while candies > 28:
    taken = takecandies(Human) if step == 1 else bot(candies)
    candies -= taken
    step += 1 if step < 1 else -1
    print(f"{Namebot if step == 1 else Human} взял {taken} конфет. Осталось {candies}.")
print(f'Победил: {Human if step == 1 else Namebot}, забрав все себе')