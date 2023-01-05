# Создайте программу для игры с конфетами человек против человека. Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint as r
def takecandies(name):
    taken_candies = int(input(f"{name}, сколько конфет хочешь взять: от 1 до 28? "))
    while taken_candies < 1 or taken_candies > 28:
        taken_candies = int(input(f"{name}, бери еще: от 1 до 28 "))
    return taken_candies

Human1 = input("Имя первого игрока: ")
Human2 = input("Имя второго игрока: ")
candies = 2021
step = r(0, 2) # жеребьевка
print(f"{Human1 if step == 1 else Human2}, ходит первым")

while candies > 28:
    taken = takecandies(Human1) if step == 1 else takecandies(Human2)
    candies -= taken
    step += 1 if step < 1 else -1
    print(f"{Human2 if step == 1 else Human1} взял {taken} конфет. Осталось {candies}.")
print(f'Победил: {Human1 if step == 1 else Human2}, забрав последние {candies} конфет и все остальные')