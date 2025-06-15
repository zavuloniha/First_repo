def say_hello():
		# тіло функції
    print('Привіт, Світ!')
# Кінець функції say_hello()
# виклик функції
say_hello()
# ще один виклик функції
say_hello()


def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень
x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')
print_max(3, 4)  # пряма передача значень
x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів


def add_numbers(num1: int, num2: int) -> int:
    sum = num1 + num2
    return sum
result = add_numbers(5, 10)
print(result)  # Виведе: 15


def greet(name: str) -> str:
    return f"Привіт, {name}!"
greeting = greet("Олексій")
print(greeting)  # Виведе: Привіт, Олексій!


def is_even(num: int) -> bool:
    return num % 2 == 0
check_even = is_even(4)
print(check_even)  # Виведе: True


def modify_string(original: str) -> str:
    original = "змінено"
    return original
str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var)                # виведе: оригінал


def modify_list(lst: list) -> None:
    lst.append(4)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3, 4]


def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]


def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes
result = string_to_codes("Hello world!")
print(result)


x = 50
def func() -> None:
    x = 2
    print('Зміна локального x на', x)  # Зміна локального x на 2
func()
print('Глобальний x як і раніше', x)  # x як і раніше 50


def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"
    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)
    inner_func()
outer_func()


def func_outer():
    x = 2
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    return x
result = func_outer()  # 5


x = 50
def func():
    global x
    print('x дорівнює', x)  # x дорівнює 50
    x = 2
    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2
func()
print('Значення x складає', x)# Значення x складає 2


def greet(name, message="Привіт"):
    print(f"{message}, {name}!")
# використовує значення за замовчуванням для message
greet("Олексій")  
# передача власного значення для message
greet("Марія", message="Добрий день")  


def func(a, b=5, c=10):
    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)
# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)
# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)


def say(message, times=1):
    print(message * times)
say('Привіт') 
say('Світ', 5)


def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)
price_bread = 15
price_butter = 50
price_sugar = 60
current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)
print(f'Нова вартість хліба: {current_price_bread}')
print(f'Нова вартість масла: {current_price_butter}')
print(f'Нова вартість цукру: {current_price_sugar}')


def print_all_args(*args):
    for arg in args:
        print(arg)
print_all_args(1, 'hello', True)


def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result
print(concatenate("Hello", " ", "world", "!"))


def concatenate(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result
print(concatenate("Hello", " ", "world", "!"))


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
greet(name="Alice", age=25)


def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)
example_function(1, 2, 3, name="Alice", age=25)


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
person_info = {"name": "Alice", "age": 25}
greet(**person_info)


#можна легко створити рекурсивну функцію для обчислення факторіала
def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок
print(factorial(5)) # виведе 120


#Рекурсивний підхід до обчислення чисел Фібоначчі базується на прямому застосуванні цього визначення
def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок
print(fibonacci(10)) # виведе 55


def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n = ", n, ": ", result)
        return result
print(factorial(5))



def greeting ():
    print("Hello world!")
greeting()


def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
invitation = invite_to_event("Olena")
print(invitation)


def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price
discount_price(58, 0.5)


#задания

def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
invitation = invite_to_event("Olena")
print(invitation)


def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
    apply_discount()
    return price
discount_price(58, 0.5)


def get_fullname(first_name, last_name, middle_name=""):
    if middle_name != "":
        return f"{first_name} {middle_name} {last_name}"
    else:   return f"{first_name} {last_name}"
name_printing = get_fullname ("Lena", "Green")
print(name_printing)


def format_string(string, length):
   
   
    if len(string) >= length:
        return f"{string}"
    else :
       # spaces = " " * (length - len(string))
        spaces = " " * ((length - len(string)) // 2)
        return  f"{spaces}{string}"  

formated = format_string("abaa", 15)
print(formated)


def first(size, *args):
    sum_for_first = size + len(args)
    return sum_for_first
print(first(5, "first", "second", "third"))

def second(size, **kwargs):
    sum_for_second = size + len(kwargs)
    return sum_for_second
print(second(3, comment_one="first", comment_two="second", comment_third="third"))


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
def number_of_groups(n, k):
    fact1 = factorial (n)
    fact2 = factorial(n - k)
    fact3 = factorial (k)
    number_list = int (fact1  / (fact2 * fact3))
    return number_list
print(number_of_groups(50, 7))
