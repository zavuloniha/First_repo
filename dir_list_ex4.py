# import sys
# import pathlib
# from colorama import Fore, Style

# #  python3 Task_3.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/

# #  python3 Task_3.py /Users/lmohylna/Documents/backups/.kube-2/

# def print_directory_structure(dir_path, prefix=""):
#     if dir_path.exists():
#         for item in dir_path.iterdir():
#             if item.is_dir():
#                 print(f'{Fore.RED}{item}{Style.RESET_ALL}')
#                 print_directory_structure(item, prefix + "   ")
#             elif item.is_file:
#                 print(f'{Fore.GREEN}{item}{Style.RESET_ALL}')
          
#     else:
#         print(f"Ошибка: Директория не найдена.")

# dir_path = pathlib.Path(sys.argv[1])
#print_directory_structure(dir_path)    


from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)  # Ініціалізація colorama

def list_directories(path: Path, prefix=""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(prefix + Fore.BLUE + item.name + "/")
            list_directories(item, prefix + "    ")
        elif item.is_file:
            print(f'{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}')
            #print( + Fore.GREEN + item.name)

root_dir = Path("/Users/lmohylna/Documents/backups/.kube-2/")

if not root_dir.exists():
    print(Fore.RED + f"Директорія '{root_dir}' не існує.")
else:
    print(Fore.BLUE + root_dir.name + "/")
    list_directories(root_dir, prefix="    ")



    # import os

# def print_directory_structure(root_dir):
#   """
#   Выводит структуру директории, включая имя корневой директории.

#   Args:
#     root_dir: Путь к корневой директории.
#   """
#   print(f"Структура директории: {root_dir}")
#   for dirpath, dirnames, filenames in os.walk(root_dir):
#     # Вывод текущей директории
#     level = dirpath.replace(root_dir, "").count(os.sep)
#     indent = ' ' * 4 * (level)
#     print(f"{indent}{os.path.basename(dirpath)}/")
#     # Вывод файлов в текущей директории
#     subindent = ' ' * 4 * (level + 1)
#     for filename in filenames:
#       print(f"{subindent}{filename}")

# # Пример использования:
# root_directory = "/Users/lmohylna/Documents/backups/.kube-2/"  # Текущая директория
# print_directory_structure(root_directory)


import os

def list_of_items_in_root_dir(root_dir):
    structure = []
    for root, dirs, files in os.walk(root_dir):
        structure.append((root, dirs, files))
      
    return structure

def give_structure(structure):
    for root, dirs, files in structure:
        level = root.replace(structure[0][0], '').count(os.sep)
        отступ = ' ' * 4 * level
        print(os.path.basename(root))
        print(f'{отступ}{os.path.basename(root)}/')
        for dir_ in dirs:
            print(f'{отступ}    {dir_}/')
        for file_ in files:
            print(f'{отступ}    {file_}')


root_dir = "/Users/lmohylna/Documents/backups/.kube-2/" 
structure = list_of_items_in_root_dir(root_dir)
give_structure(structure)



import os
from colorama import Fore, Back, Style
def print_directory_structure(root_dir, prefix=""):
    """
    Рекурсивно выводит структуру директории.

    Args:
        root_dir: Корневая директория для обхода.
        prefix: Префикс для отступов при выводе.
    """
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            #print(f"{Fore.RED}{prefix}├── {item}{Style.RESET_ALL}/")
            print(f"{Fore.RED}{prefix}    {item}{Style.RESET_ALL}/")
            #print_directory_structure(path, prefix + "│   ")
            print_directory_structure(path, prefix + "   ")
        else:
            #print(f"{Fore.BLUE}{prefix}└── {item}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{prefix}   {item}{Style.RESET_ALL}")

# Пример использования:
directory_to_print = "/Users/lmohylna/Documents/backups/.kube-2/"  # Текущая директория
print_directory_structure(directory_to_print)





import os
from colorama import Fore, Back, Style
def print_directory_structure(root_dir, prefix=""):
    """
    Рекурсивно выводит структуру директории.

    Args:
        root_dir: Корневая директория для обхода.
        prefix: Префикс для отступов при выводе.
    """
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isdir(path):
            print(f"{Fore.RED}{prefix}{item}{Style.RESET_ALL}/")
            print_directory_structure(path, prefix + "  ")
        else:
            print(f"{Fore.BLUE}{prefix}{item}{Style.RESET_ALL}")

# Пример использования:
directory_to_print = "/Users/lmohylna/Documents/backups/.kube-2/"  # Текущая директория
print_directory_structure(directory_to_print)