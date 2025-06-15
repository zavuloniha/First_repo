
num = 15  # приклад значення для num

if num > 10:
    print("num більше за 10")
else:
    print("num не більше за 10")



x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")




a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')


a = input('Введіть число')
a = int(a)

if a == 1:
    print('Число дорівнює 1')
elif a > 0:
    print('Число додатне')
else:
    print("a <= 0")




money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")


result = None
if result:
    print(result)
else:
    print("Result is None, do something")


user_name = input("Enter your name: ")

if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True
print(a is c)  # False


if my_var is None:
    # Робимо щось, якщо 'my_var' є 'None'


name = "Taras"
age = 22
has_driver_licence = True
if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")


a = True and False  # False

a = True or False  # True

a = not 2 < 0  # True



# #розглянемо завдання "FizzBuzz”
# Виводить "Fizz", якщо число кратне якомусь певному числу (наприклад, 3);
# Виводить "Buzz", якщо число кратне іншому певному числу (наприклад, 5);
# Виводить "FizzBuzz", якщо число кратне обом цим числам;
# В іншому випадку виводить саме число.
# Задаємо конкретне число
num = int(input())
# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)


#рекомендується для виділення одного рівня вкладеності для блоку інструкцій використовувати 4 пробіли
x = int(input("X: "))
y = int(input("Y: "))
if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))
result = y / x


#Також можна виділяти декілька рівнів вкладеності, додаючи ще 4 пробіли зліва для всіх інструкцій блоку
x = int(input("X: "))
y = int(input("Y: "))
if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))

        if x == 0:
            print("X can`t be equal to zero")
            x = int(input("X: "))
result = y / x



if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")


is_nice = True
state = "nice" if is_nice else "not nice"


some_data = None
msg = some_data or "Не було повернено даних"


fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _: #Символ _ тут використовується як "заглушка" для вказівки на будь-які інші випадки, які не відповідають переліченим
        print("Unknown fruit.")


point = (1, 0)
match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")


pets = ["dog", "fish", "cat"]
match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")


fruit = 'apple'
for char in fruit:
    print(char)


alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")


some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)


odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)


#порахувати скільки символів в рядку та скільки пробілів в рядку
# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")
# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів
# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1
# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")


k = 0
while k < 10:
    k = k + 1
	print(k)


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1


while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break


a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)


for i in range(1, 10):
    if i % 2 == 0:
        print(f”{i} є парним числом.“)
    else:
        print(f”{i} є непарним числом.“)


while True:
    number = input("number = ")
    number = int(number)
    while True:
        print(number)
        number = number - 1
        if number < 0:
            break


#код призводить до помилки SyntaxError
number = int(input("number = "))
if number < 0:
    break


for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(0, 10, 2):
    print(i)


some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)


list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
for number, letter in zip(list1, list2):
    print(number, letter)


numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)
for key in numbers.keys():
    print(key)
for val in numbers.values():
    print(val)
for key, value in numbers.items():
    print(key, value)


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")

#задания

is_next = None
num = int(input("Enter the number of points: "))
if num >= 83:
   is_next = True
else:
 is_next = False


work_experience = int(input("Enter your full work experience in years: "))
if work_experience<=5 and work_experience>1:
    developer_type = "Middle"
elif work_experience<=1:
    developer_type = "Junior"
else:
    developer_type = "Senior"


num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 1:
        result = "Positive odd number"
    else :
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"


num = int(input("Enter the integer (0 to 100): "))
sum = 0
while num >= 0:
    sum = sum + num
    num = num -1 
print(sum)


message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    if char == search:
        result += 1
print(result)


pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool//quantity
except ZeroDivisionError:
    print('Divide by zero completed!')


