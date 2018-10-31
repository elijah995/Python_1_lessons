# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


s = input().split()
x1 = [int(i) for i in s[0].split('/')]
x1.append(1) # на случай, если первое слагаемое целое
x2 = [int(i) for i in s[2].split('/')]
x2.append(1)
char = int(s[1] + '1')
denom = x1[1] * x2[1]
num = x1[0] * x2[1] + char * x2[0] * x1[1]
if num < 0:
    char = -1
    num = abs(num)
else:
    char = 1
a = num
while a != 1:
    if num % a == 0 and denom % a == 0:
        num = num // a
        denom = denom // a
    a -= 1
if num % denom == 0:
    print(char * (num // denom))
elif num > denom:
    integ = char * (num // denom)
    num = num % denom
    print("{} {}/{}".format(integ, num, denom))
else:
    print("{}/{}".format(char * num, denom))


print()
# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

workers = []
with open(".\data\workers", "r", encoding="utf8") as fin:
    fin.readline()
    for line in fin:
        line = line.strip().split()
        workers.append(line)
hours = []        
with open(".\data\hours_of", "r", encoding="utf8") as fin:
    c
    for line in fin:
        line = line.strip().split()
        hours.append(line)

workers = sorted(workers, key=(lambda x: x[1]))
hours = sorted(hours, key=(lambda x: x[1]))

salaries = []
for w, h in zip(workers, hours):
    if int(h[2]) == int(w[4]):
        salaries.append([h[0], h[1], h[2], w[2]])
    elif int(h[2]) < int(w[4]):
        s = round(int(h[2]) / int(w[4]) * int(w[2]), 2)
        salaries.append([h[0], h[1], '{}-{}={}'.format(w[4], int(w[4]) - int(h[2]), h[2]), str(s)])
    else:
        s = round((int(h[2]) / int(w[4]) - 1) * int(w[2]) * 2, 2)
        salaries.append([h[0], h[1], '{}+{}={}'.format(w[4], int(h[2]) - int(w[4]), h[2]), str(int(w[2]) + s)])

for string in workers:
    print('\t\t'.join(string))
print()
for string in hours:
    print('\t\t'.join(string))
print()
for string in salaries:
    print('\t\t'.join(string))

s = [["Имя", "Фамилия", "Отработано", "Зарплата"]]
s.extend(salaries)
with open('.\data\salaries', "w", encoding="utf8") as fout:
    for string in s:
        fout.write('\t\t'.join(string) + "\n")

print()
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

from collections import defaultdict

fruits = defaultdict(list)
with open(r'.\data\fruits.txt', 'r', encoding="utf8") as fin:
    for line in fin:
        if line != '\n':
            line = line.strip()
            fruits[line[0]].append(line + '\n')
            
for letter in fruits.keys():
    with open(r'.\data\fruits_' + letter + '.txt', "w", encoding="utf8") as fout:
        for fruit in fruits[letter]:
            fout.write(fruit)


