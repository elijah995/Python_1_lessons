# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
#import hw05_easy as easy

#print('sys.argv = ' , sys.argv)

def print_help():
    print("help - получение справки")
    print("go_to - перейти в директорию")
    print("show_content - просмотреть содержимое текущей директории")
    print("rmdir - удалить директорию")
    print("mkdir - создать директорию")

def go_to():
    dir_name = input("Укажите имя директории для перехода: ")
    try:
        os.chdir(dir_name)
        print('Успешно перешёл в директорию {}'.format(dir_name))
    except FileNotFoundError:
        print('Невозможно перейти в директорию: директория {} не существует'.format(dir_name))
        
def show_content():
    lst = os.listdir()
    for el in lst:
        print(el)
        
def mk_dir():
    dir_name = input("Укажите имя создаваемой директории: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('Директория {} успешно создана'.format(dir_name))
    except FileExistsError:
        print('Невозможно создать директорию: директория {} уже существует'.format(dir_name))

def rm_dir():
    dir_name = input("Укажите имя удаляемой директории: ")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директория {} успешно удалена'.format(dir_name))
    except FileNotFoundError:
        print('Невозможно удалить директорию: директория {} не существует'.format(dir_name))


        
do = {
    "help": print_help,
    "go_to": go_to,
    "show_content": show_content,
    "mkdir": mk_dir,
    "rmdir": rm_dir
}

try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")





