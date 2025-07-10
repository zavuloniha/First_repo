import os
import pathlib

def list_directory_contents(path):
    """
    Выводит содержимое указанной директории, включая файлы и папки.
    """
    try:
        for item in pathlib.Path(path).glob('*'):
            print(item)
    except FileNotFoundError:
        print(f"Ошибка: Директория '{path}' не найдена.")
    except PermissionError:
        print(f"Ошибка: Недостаточно прав для доступа к директории '{path}'.")

# Пример использования
directory_path = "/Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/" # Текущая директория
list_directory_contents(directory_path)




from pathlib import Path

#current_folder = Path('.')
current_folder = Path('/Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/')
folder_structure = list(current_folder.iterdir())
print(folder_structure)

print(list(folder_structure[3].iterdir()))




import os
directory = "/Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/"
for dirpach, dirnames, filenames, in os.walk(directory):
    for dirname in dirnames:
        print('Каталог: ', os.path.join(dirpach, dirname))
        for filename in filenames:
            print('Файл: ', os.path.join(dirpach, filename))



import os

def print_directory_tree(root_dir):
    """
    Выводит структуру директории, включая имя корневой директории.
    """
    print(root_dir)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))
        for filename in filenames:
            print(os.path.join(dirpath, filename))

# Пример использования:
root_directory = "/Users/lmohylna/Documents/backups/.kube-2/"  # Текущая директория
print_directory_tree(root_directory)




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
            print(f"{Fore.RED}{prefix}├── {item}{Style.RESET_ALL}/")
            print_directory_structure(path, prefix + "│   ")
        else:
            print(f"{Fore.BLUE}{prefix}└── {item}{Style.RESET_ALL}")

# Пример использования:
directory_to_print = "/Users/lmohylna/Documents/backups/.kube-2/"  # Текущая директория
print_directory_structure(directory_to_print)




import os

directory = "/Users/lmohylna/My22/Body/"

def list_files_recursively(directory):
    """
    Recursively lists all files within a given directory and its subdirectories.

    Args:
        directory (str): The path to the directory to traverse.

    Returns:
        list: A list of full paths to all files found.
    """
    files_list = []
    try:
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):
                files_list.append(full_path)
            elif os.path.isdir(full_path):
                files_list.extend(list_files_recursively(full_path))
    except OSError as e:
        print(f"Error accessing directory {directory}: {e}")
    return files_list

# Example usage:
# current_directory = "."
# all_files = list_files_recursively(current_directory)
# for file_path in all_files:
#print(file_path)



import sys
import os
import pathlib
from pathlib import Path
from colorama import Fore, Back, Style

#  python temp1_copy.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/
dir_path = Path('/Users/lmohylna/My22/Body/')
#dir_path = pathlib.Path(sys.argv[1])
prefix = ""
if dir_path.exists():
    #for item in dir_path.iterdir():
    dir_path_names = os.listdir(dir_path)
    
    for item in dir_path_names:
        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            print(f'{Fore.RED}{prefix}├── {item}{Style.RESET_ALL}')
            
        elif os.path.isfile(full_path):
            print(f'{Fore.GREEN}{prefix}└── {item}{Style.RESET_ALL}')
           
else:
    print(f"Ошибка: Директория не найдена.")

