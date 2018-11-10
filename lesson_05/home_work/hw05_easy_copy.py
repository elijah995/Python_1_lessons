# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dirs(y = 9, x = 1):
    import os

    path = os.getcwd()
    for i in range(x, y+1):
        try:
            os.mkdir(path + '\dir_' + str(i))
        except FileExistsError:
            print('Директория {} уже существует'.format(path + '\dir_' + str(i)))
            
def remove_dirs(y = 9, x = 1):
    import os
    
    path = os.getcwd()
    for i in range(x, y+1):
        try:
            os.rmdir(path + '\dir_' + str(i))
        except FileNotFoundError:
            print('Директория {} не найдена'.format(path + '\dir_' + str(i)))

make_dirs()
remove_dirs()
            

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def get_dirs():
    import os

    path = os.getcwd()
    lst = os.listdir(path)
    lst_dir = []
    for el in lst:
        if os.path.isdir(el):
            lst_dir.append(el)
    print(lst)
    print(lst_dir)
    return lst_dir

get_dirs()
    



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    import sys
    import shutil
    name = sys.argv[0]
    shutil.copyfile(name, name[:-3] + '_copy.py')

copy_file()
                     


