from collections import UserDict
class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value
# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict)


from collections import UserDict
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]
class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"
    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"
if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]
    print("---------------------------")
    for customer in customers:
        print(customer.phone_info())
    print("---------------------------")
    for customer in customers:
        print(customer.email_info())


#Простий приклад використання UserList:
from collections import UserList
class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)
# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)
# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)


from collections import UserList
class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))
countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())


from collections import UserString
# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]
# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())
# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())


#приклад показує модифікований рядок з методом truncate, який обмежує розмір рядка до MAX_LEN символів
from collections import UserString
class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]
ts = TruncatedString('hello world!')
ts.truncate()
print(ts)


#Базовий приклад синтаксису @dataclass виглядає наступним чином:
from dataclasses import dataclass
@dataclass
class ExampleClass:
    attribute1: type
    attribute2: type = default_value
#Традиційно, якщо вам потрібно створити клас для зберігання даних,
#ви б мали б вручну визначити метод __init__ для ініціалізації атрибутів.
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
#Якщо використати декоратор @dataclass, ми можемо автоматизувати створення класу, значно спростивши код.
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
#В наступному прикладі клас Article містить атрибути зі стандартними значеннями
@dataclass
class Article:
    title: str
    author: str
    views: int = 0


#створимо клас Rectangle, який буде обчислювати 
# та виводити площу різних прямокутників, заданих користувачем.
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    def area(self) -> int:
        return self.width * self.height
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)
print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")


#Для створення перелічення використовується наслідування від класу Enum. 
# Кожен атрибут класу представляє окремий член перелічення.
from enum import Enum
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
#Ви можете отримати доступ до конкретного дня за допомогою його імені:
today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY
#Enum члени можуть бути порівняні між собою за допомогою операторів порівняння:
if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")
#Кожен член Enum має властивості name і value, які повертають ім'я та значення члена відповідно:
print(today.name)  
print(today.value)  
#Якщо у вас є значення і ви хочете отримати відповідний член Enum, ви можете використовувати метод Day() з цим значенням:
day_from_value = Day(1)
print(day_from_value)  # Виведе: Day.MONDAY


#Давайте розглянемо наближений до реальності приклад використання Enum, 
# де ми створимо систему управління статусами замовлень для інтернет-магазину
#Перш за все, нам потрібно визначити Enum, який буде представляти різні статуси замовлень.
from enum import Enum, auto
class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
#Тепер створимо клас Order, який буде використовувати 
# наш перелічуваний тип даних OrderStatus для відстеження статусу замовлення.
class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status
    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")
    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")
#Тепер створимо декілька замовлень і покажемо, як можна оновити та відобразити їх статуси.
order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)
order1.display_status()
order2.display_status()
order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)
order1.display_status()
order2.display_status()
#Зміна або додавання нових значень в Enum не впливає на решту коду, що робить зміну та розширення коду простішими. 
# Наприклад, щоб додати новий статус "Відмінений"(CANCELED), ви просто розширите визначення OrderStatus таким чином:
from enum import Enum, auto
class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()



#розглянемо ситуацію, де ми могли б неправильно вирішити використати наслідування. 
# Маємо клас Owner для господаря кішки та клас Cat для самої кішки.
class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def info(self):
        return f"{self.name}: {self.phone}"
class Cat(Owner):
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age
    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"
	def sound(self):
		return "Meow"
cat = Cat('Simon', 4, 'Boris', '+380503002010')
print(cat.info())
print(cat.cat_info())
#Але це не має сенсу, правда? Кішка і господар - це дві різні речі.
# Кішка не може бути господарем. Вона просто має господаря.
#Натомість, ми повинні показати, що кішка "має" господаря
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
    def info(self):
        return f"{self.name}: {self.phone}"
class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner
    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"
    def sound(self):
        return "Meow"
owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info())
print(cat.get_info())



#Композиція ефективно використовується в ситуаціях, 
# де об'єкти мають сильну залежність один від одного, і "частина" не може існувати без "цілого"

#Уявімо, що ми розробляємо програмне забезпечення для управління проектами. 
# У цій системі кожен "Проект" (клас Project), може містити кілька "Задач" (клас Task),
#  і ці задачі не мають сенсу поза контекстом свого проекту. 
# Якщо проект видаляється, то всі його задачі також повинні бути видалені.
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")
class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []
    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))
    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]
    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()
# Створення проекту
my_project = Project("Веб-розробка")
# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")
# Відображення інформації про проект
my_project.display_project_info()
# Видалення задачі
my_project.remove_task("Розробка API")
# Перевірка видалення задачі
my_project.display_project_info()


#Ви можете специфікувати різні типи винятків, які хочете обробити, 
# або використовувати загальний виняток, щоб перехопити будь-яку помилку.
#Наприклад:
try:
    # Код, який може викликати виняток
    result = 10 / 0
except ZeroDivisionError:
    # Обробка винятку ділення на нуль
    print("Ділення на нуль!")
except Exception as e:
    # Обробка будь-якого іншого винятку
    print(f"Виникла помилка: {e}")
else:
    # Виконується, якщо виняток не був викликаний
    print("Все пройшло успішно!")
finally:
    # Виконується завжди, незалежно від того, був виняток чи ні
    print("Блок finally завжди виконується.")

#Створити власний виняток досить легко:
class MyCustomError(Exception):
    """Базовий клас для власних винятків"""
    pass


# Визначення власного класу винятку
#Визначимо власний клас винятку для обробки помилок, пов'язаних з перевіркою віку особи.
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)
# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи менший за 18 років")
if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")

#Наступний приклад, ви очікуєте, що користувач повинен ввести ім'я, 
# і це ім'я не повинно бути коротшим двох символів і починатися з великої літери
class NameTooShortError(Exception):
    pass
class NameStartsFromLowError(Exception):
    pass
def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name
if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)






