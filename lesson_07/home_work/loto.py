#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

def Row_9(x = []):
    """
    Функция создаёт список из 9 случайных чисел от 1 до 90
    (по одному из каждого десятка),
    в качестве аргумента может быть передан список недопустимых значений.
    Затем случайные 5 элементов списка заменяются на '  '.
    Получаем ряд для карточки лото из девяти позиций,
    четыре из которых заняты числами.
    """
    import random
    row = []

    row_1 = random.randint(1, 9)
    while row_1 in x:
        row_1 = random.randint(1, 9)
    row.append(row_1)

    def row_i(i):
        row = random.randint((i-1)*10, i*10-1)
        while row in x:
            row = random.randint((i-1)*10, i*10-1)
        return row

    for i in range(2, 9):
        row.append(row_i(i))
    
    row_9 = random.randint(80, 90)
    while row_9 in x:
        row_9 = random.randint(80, 90) 
    row.append(row_9)
    
    exc = random.sample(range(0, 9), 5)

    for i in range(len(row)):
        if i in exc:
            row[i] = '  '

    return row

class Card:
       
    def __init__(self, name='-------- Карточка --------'):
        self.name = name
        self.f_row = Row_9()
        self.s_row = Row_9(self.f_row)
        self.t_row = Row_9(self.s_row + self.f_row)

    def __getitem__(self, i=0):
        if  i < 9:
            return self.f_row[i]
        elif i < 18:
            return self.s_row[i-9]
        elif i < 27:
            return self.t_row[i-18]
        else:
            raise StopIteration

    def __setitem__(self, i, value):
        if  i < 9:
            self.f_row[i] = value
        elif i < 18:
            self.s_row[i-9] = value
        elif i < 27:
            self.t_row[i-18] = value

    def find(self, x):
        for i in range(27):
            if self.__getitem__(i) == x:
                return i
        
        
    
    def __str__(self):
        print(self.name)
        if type(self.f_row[0]) == int:
            print(end=' ')
        for el in self.f_row:
            print(el, end=' ')
        print()

        if type(self.s_row[0]) == int:
            print(end=' ')
        for el in self.s_row:
            print(el, end=' ')
        print()

        if type(self.t_row[0]) == int:
            print(end=' ')
        for el in self.t_row:
            print(el, end=' ')
        print()
        return '--------------------------'


import random

my_card = Card('------ Ваша карточка -----')
ai_card = Card('-- Карточка компьютера ---')

print(my_card)
print(ai_card)

l = list(range(1, 91))
random.shuffle(l)

my_score = 0
ai_score = 0
winner = -1
for i in range(len(l)):
    print()
    print("Новый бочонок: {} (осталось {})".format(l[i], 89-i))
    print()
    print(my_card)
    print(ai_card)
    print()
    p = input("Зачеркнуть число на карточке? (Да -- 'y') ")
    if l[i] in my_card:
        if p == 'y':
            my_card[my_card.find(l[i])] = ' -'
            my_score += 1
        else:
            winner = 2
            break
    else:
        if p == 'y':
            winner = 2
            break
    if l[i] in ai_card:
        ai_card[ai_card.find(l[i])] = ' -'
        ai_score += 1
    if my_score == 12 and ai_score == 12:
        winner = 0
        break
    elif my_score == 12:
        winner = 1
        break
    elif ai_score == 12:
        winner = 2
        break
    

if winner == 1:
    print("Поздравляем! Вы выиграли!")
elif winner == 2:
    print("Вы проиграли!")
else:
    print("Ничья!")
                
        
