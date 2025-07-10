def my_function():
    print("Hello, world!")
f = my_function
f()


from typing import Callable
def add(a: int, b: int) -> int:
    return a + b
def multiply(a: int, b: int) -> int:
    return a * b
def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)
# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)
print(result_add, result_multiply)

#Наприклад, ми можемо створити функцію, яка генерує іншу функцію для підняття числа до заданого степеня.
from typing import Callable
def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner
# Використання
square = power(2)
cube = power(3)
print(square(4)) 
print(cube(4))


#створимо словник, де ключами будуть назви операцій, а значеннями — відповідні функції.
from typing import Callable, Dict
# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b
def multiply(a: int, b: int) -> int:
    return a * b
def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner
# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)
# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}
# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25
print(result_add)  
print(result_square)  



def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function
# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

#створимо замикання, яке буде зберігати інформацію про кількість разів виклику функції.
from typing import Callable
def counter() -> Callable[[], int]:
    count = 0
    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count
    return increment
# Створення лічильника
count_calls = counter()
# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3

#Припустимо, у нас є функція, яка приймає два аргументи
def add(a, b):
    return a + b
#Застосувавши каррінг до цієї функції, ми перетворимо її на двій функції, кожна з яких приймає по одному аргументу:
def add(a):
    def add_b(b):
        return a + b
    return add_b
# Використання:
add_5 = add(5)
result = add_5(10)
print(result)


#Припустимо, у нас є функція для обчислення знижки на товар.
#Ця функція приймає відсоток знижки і остаточну ціну товару.
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)
# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)
discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)
#Перетворимо функцію apply_discount, використовуючи каррінг. 
#Це дозволить нам створити "замовлені" функції для різних рівнів знижок,
#кожна з яких буде приймати тільки ціну товару.
from typing import Callable
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)
# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)
discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)
#створити словник, де ключами будуть назви знижок, а значеннями — відповідні функції обчислення знижки, 
#створені за допомогою каррінгу. Це дозволить нам легко вибирати потрібну функцію знижки зі словника.
from typing import Callable, Dict
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}
# Використання функції зі словника
price = 500
discount_type = "20%"
discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")



#Наприклад, у нас є якась дуже складна і важлива функція complicated:
def complicated(x: int, y: int) -> int:
    return x + y
#І ми не хочемо міняти її код з якоїсь причини. Але нам потрібно додати логування до цієї функції, 
#виводити в консоль щоразу, коли вона викликається, з якими аргументами її викликали і що вона повернула в результаті.
def complicated(x: int, y: int) -> int:
    return x + y
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
complicated = logger(complicated)
print(complicated(2, 3))
#Щоб спростити застосування цього шаблону проектування, в Python є спеціальний синтаксис декоратора
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
@logger
def complicated(x: int, y: int) -> int:
    return x + y
print(complicated(2, 3))
#при створенні декораторів використовувати модуль functools, це необхідно для збереження метаданих оригінальної функції,
#яку ми декоруємо. Функція functools.wraps допомагає в цьому, зберігаючи інформацію про оригінальну функцію, 
#як-от ім'я функції та документацію
from functools import wraps
def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
@logger
def complicated(x: int, y: int) -> int:
    return x + y
print(complicated(2, 3))
print(complicated.__name__)


#щоб створити список квадратів чисел від 1 до 5, треба написати наступний код:
sq = []
for i in range(1, 6):
    sq.append(i**2)
print(sq)

#List comprehensions використовуються для створення нових списків та мають наступний синтаксис: 
#[new_item for item in iterable if condition]
#наприклад, попередній приклад можна записати наступним чином:
sq = [x**2 for x in range(1, 6)]
print(sq)
#Умова в синтаксисі дозволяє нам створювати списки за якоюсь умовою. Створимо список квадратів парних чисел від 1 до 9:
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)
#В звичайному стилі попередній приклад прийшлось би записувати так:
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)  # Виведе [4, 16, 36, 64]


#Set comprehensions використовуються аналогічно list comprehensions, але для створення множин.
#  {new_item for item in iterable if condition}
#Збережімо множини квадратів чисел зі списку:
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)
#Set Comprehensions також підтримує умови. Створимо множину квадратів непарних чисел від 1 до 9:
odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)

#Dictionary comprehensions використовуються для створення нових словників. 
# Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення
#{key: value for item in iterable if condition}
#Створимо словник, де ключ - число, а значення - його квадрат.
sq = {x: x**2 for x in range(1, 10)}
print(sq)
#Створимо словник, де ключами будуть числа, а значеннями — їх квадрати, але тільки для чисел, що більші за 5:
sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict)


#Синтаксис лямбда-функції є наступним:
lambda arguments: expression

#приклад
add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8
#
print((lambda x, y: x + y)(5, 3))  # Виведе 8


#Лямбда-функції часто використовуються як аргументи для функцій вищого порядку, таких як map(), filter() або sorted().
#  Наприклад зворотне сортування списку для sorted()
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted)

#Давайте напишемо за допомогою map генератор, який підносить числа із списку numbers до квадрату:
numbers = [1, 2, 3, 4, 5]
for i in map(lambda x: x ** 2, numbers):
    print(i)
#Якщо ми хочем отримати список, а не генератор то код можна записати так:
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

#Можна застосувати map до декількох списків:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)
print(list(sum_nums))

#Замість використання функції map():
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)
#Ми використаємо list comprehensions:
nums = [1, 2, 3, 4, 5]
squared_nums = [x * x for x in nums]
print(squared_nums)
#Для двох списків ми теж можемо використати list comprehensions допомоги функції zip
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)


#Синтаксис filter(): filter(function, iterable)
#Наприклад, виведемо список чисел, які є парними в інтервалі від 1 до 10:
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums))

#Не обов'язково використовувати lambda функцію.
#У цьому прикладі filter() використовує функцію is_positive для відбору тільки додатних чисел:
def is_positive(x):
    return x > 0
nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums))

#давайте відфільтруємо з рядка літери, щоб залишилися лише літери нижнього регістру:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)

#Розглянемо, як можна замінити filter() на list comprehensions:
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)
#Для рядка літер:
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join([x for x in some_str if x.islower()])
print(new_str)


#Перевіримо чи наявний хоч один елемент в списку який є істинним?
nums = [0, False, 5, 0]
result = any(nums)  
print(result)

#В функцію можна передавати генератор або list comprehension. Наприклад перевіримо чи є в списку парні числа?
nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)

#перевірка, чи всі елементи у списку істинні?
nums = [1, 2, 3, 4]
result = all(nums)  
print(result)

#Чи всі елементи списку є парними?
nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even)

#Чи всі слова у списку мають велику початкову букву?
words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)




