# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("========Задача-1========")
fruits = ["яблоко", "банан", "киви", "арбуз", "маракуйя"]
indent = len(max(fruits, key=len)) + 1
for i in range(len(fruits)):
    print("{}. {:>{}}".format(i+1, fruits[i], indent))

print()

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке и выведите результат.

print("========Задача-2========")
a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 4, 6, 8, 10, 12]
for el in a:
    if el in b:
        a.remove(el)
print(a)


print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# и выведите результат

print("========Задача-3========")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = []
for el in a:
    if el % 2 == 0:
        b.append(el / 4)
    else:
        b.append(el * 2)
print(b)

