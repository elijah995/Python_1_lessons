# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    f = [1, 1]
    f_nm = []
    for i in range(0, m + 1):
        if i >= n:
            f_nm.append(f[i])
        f.append(f[i] + f[i + 1])
    return f_nm       


print(fibonacci(1, 1))
print(fibonacci(1, 10))
print(fibonacci(3, 20))
print(fibonacci(0, 5))

print()
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def l_sort(l):
    l_sorted = []
    for i in range(len(l)):
        l_sorted.append(l.pop(l.index(min(l))))
    return l_sorted

l = [9, 23, 45, 21, 109, -1, 93, -14]
print(l)
print(l_sort(l))

print()
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filtered(cond, lst):
    filtered = []
    for item in lst:
        if cond(item) == True:
            filtered.append(item)
    return filtered

l = range(20)
print(filtered(lambda x: x > 5, l))
print(filtered(lambda x: x ** 2 in l, l))

import math

print(filtered(lambda x: math.sqrt(x) in l, l))
    

print()
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parallelogram(a, b, c, d):
    if b[0] - a[0] ==  c[0] - d[0] and b[1] - a[1] == c[1] - d[1]\
    and d[0] - a[0] == c[0] - b[0] and d[1] - a[1] == c[1] - b[1]:
        return True
    else:
        return False

a1, a2, a3, a4 = [3, 2], [5, 7], [11, 8], [9, 3]
print(parallelogram(a1, a2, a3, a4))
      
    

