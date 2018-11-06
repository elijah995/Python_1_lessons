# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

# без re
s = "mtMmEZUOmcq"
while s != 'stop':
    upper = [-1]
    for i in range(len(s)):
        if s[i].isupper(): 
            upper.append(i)
    upper.append(len(s))
    frag = []
    for j in range(len(upper) - 1):
        if s[upper[j] + 1:upper[j + 1]] != '':
            frag.append(s[upper[j] + 1:upper[j + 1]]) 
    print(frag)
    s = input()

# с re
import re

s = "mtMmEZUOmcq"
result = re.sub('[A-Z]', ' ', s)
result = result.split()
print(result)

print()
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.


# без re
s = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
while s != 'stop':
    s += ' '    # на случай, если искомая последовательность в конце
    k = 0       # счётчик состояний
    j = ''
    res = []
    for i in range(len(s)):
        if k == 0:
            if s[i].isupper() == False:
                k = 1
            else:
                k = 0
        elif k == 1:
            if s[i].isupper() == False:
                k = 2
            else:
                k = 0
        elif k == 2:
            if s[i].isupper():
                k = 3
        elif k == 3:
            if s[i].isupper():
                k = 4
            else:
                k = 0
        elif k == 4:
            if s[i].isupper():
                j += s[i-2]
                k = 5
            else:
                k = 1
        elif k == 5:
            if s[i].isupper():
                j += s[i-2]
            else:
                res.append(j)
                j = ''
                k = 0
    print(res)
    s = input()
    

# с re
s = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
res = re.findall('[a-z]{2}[A-Z]+[A-Z]{2}', s)
result = []
for el in res:
   result.append(el[2:-2])
print(result)


print()
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

def random_number(x):
    s = ''
    for i in range(x):
        s += str(random.randint(0, 9))
    filename = 'random_number_' + str(x) + '.txt'
    with open(filename, 'w', encoding='utf8') as fout:
        fout.write(s)

random_number(2500)
with open('random_number_2500.txt', 'r', encoding='utf8') as fin:
        s = fin.readline()

k = 1
sub_s = ''
max_s = ''
max_k = 0
for i in range(1, len(s)):
    if k == 1:
        if s[i] == s[i-1]:
            k += 1
            sub_s += s[i-1]
    elif k > 1:
        if s[i] == s[i-1]:
            k += 1
            sub_s += s[i-1]
        else:
            if k > max_k:
                sub_s += s[i-1]
                max_s = sub_s
                max_k = k
                k = 1
                sub_s = ''
            else:
                sub_s = ''
                k = 1
print(max_s)


