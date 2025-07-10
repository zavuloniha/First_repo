import sys
import pathlib
from colorama import Fore, Back, Style

#  python3 Task_3.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/
# python3 Task_3.py /Users/lmohylna/Documents/backups/.kube-2/
dir_path = pathlib.Path(sys.argv[1])

if dir_path.exists():
    print(f'{Fore.RED}{dir_path}{Style.RESET_ALL}')
    for item in dir_path.iterdir():
        if item.is_dir():
            print(f'{Fore.RED}{item}{Style.RESET_ALL}')
           
        elif item.is_file:
            print(f'{Fore.GREEN}{item}{Style.RESET_ALL}')
          
else:
    print(f"Ошибка: Директория не найдена.")