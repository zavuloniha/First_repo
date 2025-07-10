class Person:
    pass  # Порожній блок для тіла класу
p = Person()


class User:
    name = 'Anonymous'
    age = 15
user1 = User()
print(user1.name)
print(user1.age)
user2 = User()
user2.name = "John"
user2.age = 90
print(user2.name)
print(user2.age)


class MyClass:
    class_attribute = "I am a class attribute" 


class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу
obj1 = MyClass(5)
obj2 = MyClass(10)


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')
    def set_age(self, age: int) -> None:
        self.age = age
bob = Person('Boris', 34)
bob.say_name()
bob.set_age(25)
bob.say_name()


class Person:
    count = 0
    def __init__(self, name: str):
        self.name = name
        Person.count += 1
    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")
first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()


class Person:
    count = 0
    def __init__(self):
        pass
person = Person()
print(person.count)  # 0
#В цьому прикладі ми маємо доступ до змінної класу count, а у наступному прикладі вже ні.
class Person:
    count = 0
    def __init__(self):
        self.count = 10
person = Person()
print(person.count)  # 10
#Як бачимо person.count повертає 10. Це значення поля.
#Але ми завжди маємо доступ до змінної класу через ім'я класу: Person.count
class Person:
    count = 0
    def __init__(self):
        self.count = 10
person = Person()
print(person.count)  # 10
print(Person.count)  # 0


class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health
    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")
    def dodge(self):
        print(f"{self.name} dodged the attack!")
    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form
# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)
# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
    def greeting(self):
        return f"Hi {self.name}"
p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)
print(p.greeting())
#Якщо ми хочемо взаємодіяти з захищеними полями об'єкту ззовні, 
# необхідно впровадити правильний підхід до інкапсуляції у класі Person 
# та слід використовувати методи для взаємодії з такими атрибутами об'єкту
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
    def greeting(self):
        return f"Hi {self.name}"
        def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())


class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True, False)
print(p.__is_admin)
#Як видно з цього прикладу, доступу за допомогою p.__is_admin немає.

#Насправді було лише змінене ім'я поля, щоб запобігти випадковому доступу до нього,
#  але воно все одно доступно ззовні класу. 
# Змінене ім'я формується як знак підкреслювання, ім'я класу та ім'я змінної.
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
p = Person("Boris", 34, True, False)
print(p._Person__is_admin)

#Щоб реалізувати методи доступу до приватного поля __is_admin у класі Person, 
# ми можемо використати той самий підхід, що і до захищеного поля _is_active
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin
    def greeting(self):
        return f"Hi {self.name}"
    def is_active(self):
        return self._is_active
    def set_active(self, active: bool):
        self._is_active = active
    def get_is_admin(self):
        return self.__is_admin
    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())


#ООП

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"
class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"
class Cow(Animal):  
    def make_sound(self):
        return "Moo"
my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)
print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"
#Розширимо наш приклад, додавши унікальну властивість до класу Dog - поле breed (порода).
class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість
    def make_sound(self):
        return "Woof"
#Наприклад, додамо метод chase_tail() до класу Dog.
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість
    def make_sound(self) -> str:
        return "Woof"
    def chase_tail(self) -> str:
        return f"{self.name} is chasing its tail!"
my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"
#Повний код виглядатиме тепер так:
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"
class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість
    def make_sound(self) -> str:
        return "Woof"
    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"
class Cow(Animal):
    def make_sound(self):
        return "Moo"
my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)
print(my_cat.make_sound())  # Виведе "Meow"
print(my_cow.make_sound())  # Виведе "Moo"
my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"


#Уявімо, що ми маємо клас Bird і хочемо створити клас Parrot, який наслідує від Bird. 
#Але потім ми вирішуємо створити новий клас TalkingParrot, який наслідується вже від Parrot.
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    def make_sound(self):
        pass
class Bird(Animal):
    def make_sound(self):
        return "Chirp"
class Parrot(Bird):
    def can_fly(self):
        return True
class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"
my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))


#Ви можете переглянути MRO для будь-якого класу використовуючи метод mro() або атрибут __mro__. Наприклад:
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
print(D.mro())  # Виведе порядок розв'язання методів для класу D


class A:
    name = "Я клас A"
class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"
class C(A, B):
    property = "Я знаходжусь в класі C"
c = C()
print(c.name)
print(c.property)


#Коли ми розглядали наслідування у прикладі з тваринами, ми вже бачили динамічний поліморфізм:
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self):
        return "Meow"
class Dog(Animal):
    def make_sound(self):
        return "Woof"
def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())
animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)


#Інтерпретатор не перевіряє, що у функцію або метод був переданий об'єкт потрібного або дочірнього класу,
# достатньо щоб в об'єкта були потрібні методи і все буде працювати.
class Duck:
    def quack(self):
        print("Quack, quack!")
class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")
def make_it_quack(duck):
    duck.quack()
duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)


#У цьому прикладі, качина типізація дозволяє нам передавати будь-який об'єкт,
#який має метод speak, у функцію make_it_speak, не зважаючи на його конкретний клас
class Dog:
    def speak(self) -> str:
        return "Woof"
class Cat:
    def speak(self) -> str:
        return "Meow"
class Robot:
    def speak(self) -> str:
        return "Beep boop"
def make_it_speak(speaker) -> None:
    print(speaker.speak())
dog = Dog()
cat = Cat()
robot = Robot()
make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
#Але, що стосується типу параметру speaker для функції make_it_speak? 
#Щоб занотувати тип параметра функції speaker ми можемо використати typing.Protocol, 
# який визначає набір методів, які цей параметр має виконувати, не прив'язуючись до конкретного класу.
from typing import Protocol
class Speaker(Protocol):
    def speak(self) -> str:
        pass
class Dog:
    def speak(self) -> str:
        return "Woof"
class Cat:
    def speak(self) -> str:
        return "Meow"
class Robot:
    def speak(self) -> str:
        return "Beep boop"
def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())
dog = Dog()
cat = Cat()
robot = Robot()
make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop
#Результат буде той самий але статична типізація за допомогою typing.Protocol використовується для вказівки,
#що параметр speaker повинен відповідати інтерфейсу, який має метод speak.






