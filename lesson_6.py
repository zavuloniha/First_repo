
import math
sin_pi = math.sin(math.pi)

from math import pi, sin
sin_pi = sin(pi)

#cкрипт mymodule.py, який містить ось такий код:
# mymodule.py
def say_hello(name):
    return f"Hello, {name}!"
#використання цього модуля в іншому файлі Python, наприклад в main.py, ми імпортуємо його
# main.py
import mymodule
print(mymodule.say_hello("World"))
#or
# main.py
from mymodule import say_hello
print(say_hello("World"))
#також можна змінити назву функції say_hello в середині main.py, коли імпортуємо її з модуля mymodule.py
# main.py
from mymodule import say_hello as greeting
print(greeting("World"))

from module_name import item_name as alias

# main.py
from mymodule import say_hello as greeting
print(dir())
print(greeting("World"))
#функцію dir() без аргументів в середині модуля, вона повертає список назв усіх об'єктів 
# (змінних, функцій, класів тощо), доступних у поточній області видимості

#Змінимо вміст модуля mymodule.py на такий
def say_hello(name):
    print(f'Hello, {name}')
print("You imported hello.py")
say_hello('user')

# main.py
from mymodule import say_hello as greeting
print(greeting("World"))

#зберегти можливість імпорту з цього модуля, не викликаючи його
# ми можемо модифікувати наш модуль mymodule.py:
def say_hello(name):
    print(f'Hello, {name}')
if __name__ == '__main__':
    print("You imported hello.py")
    say_hello('user')

#прийнято весь код, який потрібно виконати, 
#коли модуль викликається із консолі (не імпортується), поміщати у функцію main
def say_hello(name):
    print(f'Hello {name}')
def main():
    print("You imported hello.py")
    say_hello('user')
if __name__ == '__main__':
    main()


import sys
import os
print(sys.modules["os"]) #Виведення буде шлях, де знаходиться модуль os при виконанні скрипту

import sys
import os
print(sys.modules.keys()) #поверне повний список імен завантажених модулів

#Отримати список модулів, вбудованих у мову, можна за допомогою змінної sys.builtin_module_names
import sys
import os
print(sys.builtin_module_names)

# ви можете зробити простий скрипт echo.py, 
# який буде виводити у консоль всі передані при виклику аргументи
import sys
for arg in sys.argv:
    print(arg)
#запустити скрипт echo.py наступною командою:
 python echo.py test --user -hello some text 

print(sys.argv) #выведет путь к файлу в котором запускаем код

#Давайте створимо скрипт arg.py, щоб він обробляв перший аргумент запуску
import sys
def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])
if __name__ == "__main__":
    main()
#Під час виклику такого скрипту командою
 python arg.py 123 
#Ви побачите у консолі 123


#Припустимо, що модуль salary_calculations.py 
#ви розмістили у директорії calculations поряд з main.py.
def add_bonus(salary: int, bonus: int) -> int:
    return salary + bonus
#В такому випадку ви можете імпортувати модуль salary_calculations.py
from calculations import salary_calculations
salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015
#Або ми може імпортувати тільки функцію
from calculations.salary_calculations import add_bonus
salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015


#Якщо ж розробник подумав про користувача то __init__.py має виглядає ось так:
from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad
__all__ = ['nice_function', 'not_bad']
#Тепер можна скористатися таким імпортом функцій з пакету
from utility import nice_function, not_bad
nice_function()
not_bad("Test string")
#або таким:
from utility import *
nice_function()
not_bad("Test string")


#Файл jokes_handler.py:
import random
import pathlib
current_dir = pathlib.Path(__file__).parent
def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
#Файл __init__.py:
from .jokes_handler import get_random_joke
#основний скрипт main.py
from joke import get_random_joke
def main():
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}!")
    while True:
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break
if __name__ == "__main__":
    main()


python -m pip list

pip3 list

 pip install requests
pip install requests==2.28.2
pip install requests>=2.28.2
pip install requests<=2.28.2
pip uninstall requests

#Список встановлених пакетів з версіями:
pip freeze

#створити нове віртуальне оточення
python3 -m venv .venv

#виконайте активацію віртуального оточення.
#На Windows у командному рядку (CMD)
.\.venv\Scripts\activate.bat
#На Windows у PowerShell:
.\.venv\Scripts\Activate.ps1
#На macOS та Linux:
source .venv/bin/activate

pip install package_name

#Щоб повернутися до системного Python, виконайте в консолі
deactivate

#Щоб видалити віртуальне оточення, 
#достатньо фізично видалити директорію .venv з усім її вмістом в директорії проєкту.

pip freeze > requirements.txt

#Щоб встановити пакети, перелічені у requirements.txt, використовуйте команду:
pip install -r requirements.txt


#Порівняємо два підходи до написання функції, яка перевіряє, чи є число парним.
#Якщо не враховувати принцип KISS то функція могла бути наступного вигляду
def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
#Якщо ми застосуємо принцип KISS то функцію is_even ми запише так:
def is_even(number: int) -> bool:
    return number % 2 == 0

#більш складний приклад. Наприклад визначимо чи є рядок паліндромом
def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
	    if char.isalnum():
		    new_s += char.lower()
	s = new_s
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True
print(is_palindrome("Козак з казок"))  # Виведе: True

 #застосуванням принципів KISS наш код мав би виглядати наступним чином:
def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()
    s = new_s
    return s == s[::-1]
# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True


#Розглянемо наступний приклад
# Розрахунок площі 
length1, width1 = 5, 10
area1 = length1 * width1
# Багато різного коду
length2, width2 = 7, 12
area2 = length2 * width2

#Щоб застосувати принцип DRY нам потрібно повторюваний код помістити в функцію
def calculate_area(length: float, width: float) -> float:
    return length * width
area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)

#Уявімо, що у нас є модуль math_operations.py, який містить функцію для розрахунку площі прямокутника
# math_operations.py
def calculate_area(length, width):
    return length * width
#Тепер ми можемо використовувати цю функцію у різних частинах нашої програми, імпортуючи її
from math_operations import calculate_area
area1 = calculate_area(10, 5)
area2 = calculate_area(20, 15)


#Щоб об'єднати файли в проєкті,
# можна імпортувати функції або класи з інших файлів у main.py. Це може виглядати так:
from my_module import my_function
def main():
    my_function()
if __name__ == "__main__":
    main()







