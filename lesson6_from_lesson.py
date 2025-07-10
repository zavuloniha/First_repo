import sys
from pathlib import Path
#from colorama import Fore, Back, Style


#  python Task_3.py /Users/lmohylna/My22/Projects2/goit-pycore-hw-04/goit-pycore-hw-04/

# for arg in sys.argv:
#     print(arg)

print(sys.argv)



if len(sys.argv) != 2: 
    print("Please provide path!")
    sys.exit()
    # or exit()

file_path = sys.argv[1]
print(file_path)
with open(file_path) as file:
    for line in file:
        print(line.rstrip())
        #print(line, end='')

from colorama import Fore, Back, Style


print(Fore.RED + 'Це червоний текст')
print(Back.GREEN + 'Це текст на зеленому фоні')
print(Style.DIM + 'and dim text')
print(Style.RESET_ALL)
print('Це звичайний текст після скидання стилю')

print(Fore.RED + Back.GREEN + "some red text" + Style.RESET_ALL)

print(f'{Fore.RED}{Back.GREEN}some red text{Style.RESET_ALL}')        



from pathlib import Path
current_folder = Path('.')
folder_structure = list(current_folder.iterdir())
print(folder_structure)


print(list(folder_structure[0].iterdir()))