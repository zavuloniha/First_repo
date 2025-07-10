
from collections import namedtuple
# Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])
# Створення екземпляра Point
p = Point(11, y=22)
# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22


import collections

# Створення іменованого кортежу Person
Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])
# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# Виведення різних атрибутів іменованого кортежу
print(person.first_name)       
print(person.post_index) 
print(person.age)        
print(person[3])         


import collections
Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])
cat = Cat('Simon', 4, 'Krabat')
print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}')



student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1
print(mark_counts)
#то же только с с использованием  спеціального словника Counter
import collections
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)

import collections
student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts.most_common())
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

#підрахувати кількість кожної літери у рядку
from collections import Counter
# Створення Counter з рядка
letter_count = Counter("banana")
print(letter_count)


#підрахунок слів в тексті 
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)
# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")


from collections import defaultdict
# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)
# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

#int як функцію за замовчуванням, що означає, що кожен новий ключ має ініційоване значення 0
d = defaultdict(int)
# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1
print(d)


#у вас є список слів і ви хочете розбити його на декілька списків, залежно від першої літери слова.
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}
for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words)
#Щоб не перевіряти, чи є список на цю літеру в словнику grouped_words, 
#ми можемо скористатися defaultdict із collections та задати значенням за замовчуванням порожній список
from collections import defaultdict
words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = defaultdict(list)
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(dict(grouped_words))



#Проста реалізація команд стеку включає наступні функції:
# Створення стеку
def create_stack():
    return []
# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0
# Додавання елементу
def push(stack, item):
    stack.append(item)
# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")
# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")

#Спочатку створимо стек та додамо декілька елементів:
stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
#Переглянемо верхній елемент:
print(peek(stack))  # Виведе 'c'
#Видалимо верхній елемент:
print(pop(stack))  # Виведе 'c'


#Для великих списків це може бути дуже невигідно.
#Ефективнішим варіантом є використання deque з модуля collections в якості черги.
from collections import deque
# Створення черги
queue = deque()
# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')
print("Черга після додавання елементів:", list(queue))
# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft())
print("Черга після видалення елемента:", list(queue))
# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0])
# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0)
# Size: Розмір черги
print("Розмір черги:", len(queue))

from collections import deque
# Створення пустої двосторонньої черги
d = deque()
# Додаємо елементи в чергу
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')    # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги
# Виведення поточного стану черги
print("Черга після додавання елементів:", list(d))
# Видалення та виведення останнього елемента (з правого кінця)
print("Видалений останній елемент:", d.pop())
# Видалення та виведення першого елемента (з лівого кінця)
print("Видалений перший елемент:", d.popleft())
# Виведення поточного стану черги після видалення елементів
print("Черга після видалення елементів:", list(d))


#Ще однією особливістю deque є можливість обмежити розмір Deque:
from collections import deque
d = deque(maxlen=5)
for i in range(10):
    d.append(i)
print(d)


from collections import deque
# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]
# Ініціалізація черги завдань
task_queue = deque()
# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")
# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")



from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("0.1") + Decimal("0.2"))


#Можна налаштувати загальну точність для всіх обчислень Decimal.
from decimal import getcontext
getcontext().prec = 4
#Тепер будь-які обчислення з Decimal будуть мати точність до чотирьох знаків після коми

from decimal import Decimal, getcontext
getcontext().prec = 6
print(Decimal("1") / Decimal("7"))
getcontext().prec = 8
print(Decimal("1") / Decimal("7"))

from decimal import Decimal, getcontext
getcontext().prec = 6
print(Decimal("233") / Decimal("7"))


#Наприклад, якщо ви хочете округлити число до двох знаків після коми,
#ви використовуєте Decimal об'єкт з двома нулями після коми як шаблон.
from decimal import Decimal, ROUND_DOWN
# Вихідне число Decimal
number = Decimal('3.14159')
# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(rounded_number)


#За замовчуванням округлення описується константою ROUND_HALF_EVEN
import decimal
from decimal import Decimal
number = Decimal("1.45")
# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))
# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))
# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))



def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3

#Щоб кожен раз не використовувати try except для контролю винятку StopIteration найчастіше генератори 
# використовуються безпосередньо в циклах for ..., який буде це виконувати за нас
def count_down(start):
    while start > 0:
        yield start
        start -= 1
for number in count_down(5):
    print(number)

#Один з корисних випадків застосування генератору, це ітерація по файлу
def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()
# Використання генератора для читання рядків з файлу
for line in read_lines("my_file.txt"):
    print(line)






