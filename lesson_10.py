
class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'
bill = Human('Bill')
print(bill.say_hello())
print(bill.age)
jill = Human('Jill', 20)
print(jill.say_hello())
print(jill.age)

#Додамо перевірку віку, щоб встановити, чи є людина повнолітньою, і відповідне поле is_adult, 
#а також використаємо метод __init__ для виклику іншого методу класу під час ініціалізації.
class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()  
                # Приклад логування
        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}")
    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'
    def __check_adulthood(self) -> bool:
        return self.age >= 18
bill = Human('Bill')
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")
jill = Human('Jill', 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")


#коли ми хочемо у випадках, коли застосунок повинен відобразити об'єкт, виводити якусь корисну інформацію, 
# ми повинні модифікувати цей метод. Наприклад, клас точки на площині в Декартових координатах:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)

#Розглянемо наступний приклад з нашим класом Point:
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
original_point = Point(2, 3)
print(repr(original_point))  
# Використання рядка, повернутого __repr__, для створення нового об'єкта
new_point = eval(repr(original_point))
print(new_point)


#важливо визначити метод __str__ у ваших класах:
#щоб надати інтуїтивно зрозуміле та зручне для читання представлення ваших об'єктів.
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    def __repr__(self):
        return f"Human({self.name}, {self.age})"
human = Human("Alice", 30)
print(human)


#Розглянемо клас SimpleDict, який імітує поведінку словника:
class SimpleDict:
    def __init__(self):
        self.__data = {}
    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")
    def __setitem__(self, key, value):
        self.__data[key] = value
# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age'])  


#Наприклад, ми працюємо над програмою для керування температурою в приміщенні,
#де значення температури повинні бути обмежені мінімальним та максимальним порогом
class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []
    def __getitem__(self, index: int):
        return self.__data[index]
    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value
    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"
    def __str__(self):
        return str(self.__data)
if __name__ == '__main__':
    temperatures = BoundedList(18, 26)
    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)
    print(temperatures)

#Ми можемо об'єднати нашу реалізацію з можливостями класу UserList
from collections import UserList

class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()
    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)
    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")
    def append(self, item):
        self.__validate_item(item)
        super().append(item)
    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)
    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)
    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"
    def __str__(self):
        return str(self.data)
if __name__ == '__main__':
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)
    for el in [20, 22, 25, 27]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)
    print(temperatures)
#можна додати логування
def __getitem__(self, index):
        # Додати спеціальну логіку тут, наприклад, логування або перевірку
        print(f"Accessing item at index {index}")
        # Викликати оригінальний метод __getitem__
        return super().__getitem__(index)  


#Перевизначення математичних операторів може стати зручним інструментом. 
#Наприклад, створимо клас словників, які підтримують операції додавання та віднімання:
from collections import UserDict
class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)
    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)
if __name__ == '__main__':
    d1 = MyDict({1: 'a', 2: 'b'})
    d2 = MyDict({3: 'c', 4: 'd'})
    d3 = d1 + d2
    print(d3)
    d4 = d3 - d2
    print(d4)


#ще один приклад та створимо клас ComplexNumber для представлення
#комплексних чисел, з перевизначенням деяких арифметичних операторів:
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Сума: {num1 + num2}")
    print(f"Різниця: {num1 - num2}")
    print(f"Добуток: {num1 * num2}")


# Для прикладу реалізуємо векторне множення, де результатом є скалярний добуток векторів.
from collections import UserList
class MulArray(UserList):
    def __init__(self, *args):
        self.data = list(args)
    def __mul__(self, other):
        return self.__scalar_mul(other)
    def __rmul__(self, other):
        return self.__scalar_mul(other) 
    def __scalar_mul(self, other):
        result = 0
        for i in range(min(len(self.data), len(other))):
            result += self.data[i] * other[i]
        return result
if __name__ == '__main__':
    vec1 = MulArray(1, 2, 3)
    vec2 = MulArray(3, 4, 5)
    print(vec1 * vec2)
    print(vec1 * [1, 2, 3])
    print([1, 1, 1] * vec2)


#Розглянемо клас Rectangle, який представляє прямокутник з двома властивостями: шириною width і висотою height.
#Ми хочемо порівнювати прямокутники на основі розміру їх площі.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)
    print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
    print(rect1 == rect3)  # True: площі рівні
    print(rect1 != rect2)  # True: площі не рівні
    print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
    print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
    print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
    print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3


#Реалізуємо клас Point, який представляє точку в двовимірному просторі з координатами x та y. 
# Основна мета прикладу показати можливість 
# порівнювати точки за їхніми координатами за допомогою стандартних операторів порівняння (==, !=, <, >, <=, >=).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y
    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y
    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y
    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y
if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True



class Person:
    def __init__(self, age):
        self.__age = age  # Пряме присвоєння значення атрибуту в конструкторі
    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля
    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  
if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    person.age = -5
#ле є одна проблема. Якщо ми виконаємо наступний код
person = Person(-10)
print(person.age)
#То ми не отримаємо ніякого сповіщення про помилку, а буде виведення: -10
#Виправимо цей недолік. Необхідно в конструкторі класу спочатку значення __age встановити в None,
#  а потім встановити в передане значення age через сетер.
class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age
    @property
    def age(self):
        # Геттер повертає значення приватного поля
        return self.__age
    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")
        # Присвоєння валідного значення приватному полю
        self.__age = value
if __name__ == "__main__":
    person = Person(-10)
    print(person.age)



#Тепер, озброївшись цими знаннями, давайте перепишемо приклад інкапсуляції 
# з минулого модуля, через сетери та гетери.
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin
    @property
    def is_active(self):
        return self._is_active
    @is_active.setter
    def is_active(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self._is_active = value
    @property
    def is_admin(self):
        return self.__is_admin
    @is_admin.setter
    def is_admin(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = value
    def greeting(self):
        return f"Hi {self.name}"
if __name__ == "__main__":
    p = Person("Boris", 34, True, False)
    print(p.is_admin)  # Використовуємо геттер
    p.is_admin = True  # Використовуємо сеттер
    print(p.is_admin)


class Geometry:
    PI = 3.14159
    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius ** 2
print(Geometry.area_of_circle(5))  # 78.53975

#якщо ми маємо клас Employee, ми можемо використати класовий метод для створення
# екземплярів класу на основі інформації, отриманої з рядка або файлу.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)
employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)
print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager




