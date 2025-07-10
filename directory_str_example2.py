# import sys
# import pathlib
# from colorama import Fore, Back, Style

# #  python3 directory_str_example2.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/

# dir_path = pathlib.Path(sys.argv[1])

# if dir_path.exists():
#     for item in dir_path.iterdir():
#         if item.is_dir():
#             print(f'{Fore.RED}{item}{Style.RESET_ALL}')
           
#         elif item.is_file:
#             print(f'{Fore.GREEN}{item}{Style.RESET_ALL}')
          
# else:
#     print(f"Ошибка: Директория не найдена.")

from pathlib import Path
from colorama import Fore, Style, init

from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)  # Ініціалізація colorama

def list_directories(path: Path, prefix=""):
    print(prefix + Fore.BLUE + path.name + "/")

    # Виводимо файли поточної директорії
    for item in sorted(path.iterdir()):
        if item.is_file():
            print(prefix + "    " + Fore.GREEN + item.name)

    # Рекурсивно виводимо підкаталоги
    for item in sorted(path.iterdir()):
        if item.is_dir():
            list_directories(item, prefix + "    ")

# Задайте шлях до кореневої директорії
root_dir = Path("/Users/lmohylna/Documents/backups/.kube-2/")

if not root_dir.exists():
    print(Fore.RED + f"Директорія '{root_dir}' не існує.")
else:
    list_directories(root_dir)



# import sys
# import pathlib
# from colorama import Fore, Back, Style

# #  python3 Task_3.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/
# # python3 Task_3.py /Users/lmohylna/Documents/backups/.kube-2/
# dir_path = pathlib.Path(sys.argv[1])

# if dir_path.exists():
#     print(f'{Fore.RED}{dir_path}{Style.RESET_ALL}')
#     for item in dir_path.iterdir():
#         if item.is_dir():
#             print(f'{Fore.RED}{item}{Style.RESET_ALL}')
           
#         elif item.is_file:
#             print(f'{Fore.GREEN}{item}{Style.RESET_ALL}')
          
# else:
#     print(f"Ошибка: Директория не найдена.")



import sys
import os
import pathlib
from pathlib import Path
from colorama import Fore, Back, Style

#  python temp1_copy.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/
#dir_path_to_print = Path('#w-04/goit-pycore-hw-04/')
#dir_path = pathlib.Path(sys.argv[1])

def directity_structure(dir_path, prefix =""):
    #dir_path_names = os.listdir(dir_path)
    #if dir_path_name.exists():
    #for item in dir_path.iterdir():
    dir_path_names = os.listdir(dir_path) 
   
    for item in dir_path_names:
        full_path = os.path.join(dir_path, item)
        print()  
        if os.path.isdir(full_path):
            print(f'{Fore.RED}{prefix}├── {item}{Style.RESET_ALL}/')
            directity_structure(full_path, prefix + "│   ")
        elif os.path.isfile(full_path):
            print(f'{Fore.GREEN}{prefix}└── {item}{Style.RESET_ALL}')
           
    #else:
     #   print(f"Ошибка: Директория не найдена.")


dir_path_to_print = Path('/Users/lmohylna/Documents/backups/')
directity_structure(dir_path_to_print)




import os

def get_all_files_structure(root_dir):
    structure = []
    for root, dirs, files in os.walk(root_dir):
        structure.append((root, dirs, files))
    return structure    
        
def to_print_structure(structure):        
    for root, dirs, files in structure:
        item_name = os.path.basename(root)
        level = root.replace(structure[0][0], '').count(os.sep)
        prefix = ' ' * 4 * level 
        print(f'{prefix}{item_name}')  
        for dir_ in dirs:
            print(f'{prefix}{dir_}/') 
        for file_ in files:
            print(f'{prefix}{file_}')
          

#if __name__ == "__main__":

directory =  "/Users/lmohylna/Documents/backups/"  # Замените на реальный путь
structure = get_all_files_structure(directory)
to_print_structure(structure)

