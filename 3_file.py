a = 0.2 + 0.1
print(a)

int_number = 3
float_number = 3.3
complex_number = 3.3 + 2j


age = 18
is_adult = age >= 18  # True

age = 15
is_adult = age >= 18  # False


message = "Hello world!"

s1 = "Hello"
s2 = "world!"
joined_string = s1 + " " + s2

name = "Oleg"
hello_string = f"Hello, {name}!"

s1 = 'Hello'
s2 = 'world!'
joined_string = f"{s1} {s2}"  # Hello world!

s1 = 'Hello'
s2 = 'world!'
joined_string = f"{s1} {s2}"  # Hello world!

connect_to_database = None

side_a = 10
side_b = 5
hypotenuse = (side_a**2 + side_b**2)**0.5
S = side_a * side_b / 2

n = 5000

hours = n // (60 * 60)
minutes = (n - hours * 60 * 60) // 60
seconds = n - hours * 60 * 60 - minutes * 60

ratio = 10
result = 8 * (ratio + 5) - ratio ** 2

-3 ** 2  # -9
(-3) ** 2  # 9

x1 = 10
y1 = 10
x2 = 25
y2 = 25
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Привіт", end=" ")

a = input("Рядок запрошення: ")
# На екрані ви побачите: Рядок запрошення:

age = input("How old are you?")
age = input("How old are you? ")
age = int(age)
pi = float('3.14')
pi_str = str(3.14)
age_str = str(29)
bool(0)  # False
bool(1)  # True

a = float(input("Введіть сторону квадрата a: "))
P = 4 * a
print(f"Периметр квадрата дорівнює {P}")

# Встановлюємо ціни на продукти
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Кількість кожного продукту
num_croissants = int(input("Введіть кількість круасанів: "))
num_glasses = int(input("Введіть кількість склянок: "))
num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# Обчислення загальної вартості
total_cost = num_croissants * price_per_croissant + \
             num_glasses * price_per_glass + \
             num_coffee_packs * price_per_coffee_pack

# Визначаємо кількість повних доларів і центів
total_dollars = int(total_cost)
total_cents = int(total_cost * 100)

# Вивід результату
print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
print(f"Загальна вартість у центах: {total_cents} центів")

my_list = list()

empty_list = []

my_list = [1, 2, 3, 4, 5]

my_list = [1, "Hello", 3.14]
my_list.append(4)
my_list.remove("Hello")

some_iterable = ["a", "b", "c"]
first_letter = some_iterable[0]
middle_one = some_iterable[1]
last_letter = some_iterable[2]

some_iterable = ["a", "b", "c"]
first_letter = some_iterable[-3]
middle_one = some_iterable[-2]
last_letter = some_iterable[-1]

some_iterable = [1, 2, 3]
some_iterable[1] = -2

chars = ['a', 'b', 'c']
last = chars.pop(1)

chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)

chars = ["a", "c"]
chars.insert(1, "b")

chars = ['a', 'b']
chars.clear() # []

chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']

chars =  ['a', 'b']
chars_copy = chars.copy()

chars = ["banana", "apple", "cherry"]
chars.reverse()

my_dict = {}

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)
del my_dict["age"]
print(my_dict)
print("name" in my_dict)
print("age" in my_dict)

my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")

my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com", "age": 26})

my_dict.clear()

new_dict = my_dict.copy()

my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

pythonCopy code
name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику


empty_set = set()

a = set('hello')

b = {1, 2, 3, 4, 5}

numbers = {1, 2, 3, 1, 2, 3} #буде з 1, 2, 3

#Нехай у нас є список, з якого треба видалити дублікати
lst = [1, 2, 3, 1, 2, 2, 3, 4, 1].
d_lst = set(lst)
lst=list(d_lst)

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.remove(4)
print(numbers)  # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2)
print(numbers)  # {1, 3}

numbers = {1, 2, 3}
numbers.discard(4)
print(numbers)  # {1, 3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}

my_frozenset = frozenset([1, 2, 3, 4, 5])

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця
print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})


my_tuple = tuple() # або
my_tuple = ()
my_tuple = (1, 2, 3)
my_tuple = (1,)
my_tuple = (1, "Hello", 3.14)
my_tuple = 1, "Hello", 3.14

first_item = my_tuple[0]  # Отримати перший елемент

points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}

game_string = 'My favorite "Game"'

s = "Hello world!"
print(s[0])# H
print(s[-1])# !

s = "Hello world!"
s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError

s = "Hello" 
print(s.upper()) # Виведе 'HELLO'

s = "Bill Jons"
print(s.startswith("Bi"))  # Виведе True

s = "hello.jpg"
print(s.endswith("jpg"))  # Виведе True

s = "hello world".capitalize()  # Результат: "Hello world"

s = "hello world".title()  # Результат: "Hello World"

"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))
# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))
# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))
# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))


послідовність[початок:кінець:крок]
s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Виведе 'Hello'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2] 
odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = numbers[1:10:2]
even_numbers = numbers[1::2] # Виведе [2, 4, 6, 8, 10]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
three_numbers = numbers[2:10:3] #[3, 6, 9]
three_numbers = numbers[2::3] #[3, 6, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_numbers = numbers[::-1]
print(reverse_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy_numbers = numbers[:]
print(copy_numbers)

length = 2.75
width = 1.75
area= length * width
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)

length = "2.75"
width = "1.75"
area= float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(show)

name = input("Your name? ")
email = input ("Your email? ")
age = int(input("Your age? "))
height = float(input("Your height? "))
is_active = True

length = float(input("Input the length of the room: "))
width = float(input("Input the width of the room: "))
area = length * width

my_list = []
my_list.insert(0, 2024)
my_list.insert(1, "Python")
my_list.insert(2, 3.12)

my_list = [2024, 3.12]
some_data = ['Python']
my_list.extend(some_data)
my_list.insert(1, "Python")
my_list.reverse()

data = {}
data = {}
data.update({"year": 2024, "lang": 'Python', "version": 3.12})

cat = {}
info = {"status": "vaccinated", "breed": True}
data = {}
cat.update({"nick": 'Simon', "age": 7, "characteristics": ['kind', 'noisy']})
age = cat.get("age")
cat.update(info)
