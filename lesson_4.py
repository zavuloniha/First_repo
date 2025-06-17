
this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string# True

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

one_line_text = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

("spam " "eggs") == "spam eggs"  # True

one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")


#Виведення буде слово після символу \n з нового рядка
print("Hello\nWorld")

#горизонтальна табуляція \t (tab)
print("Hello\tWorld")

#Приклад для повернення каретки \r (carriage return)
#Виведення відбувається наступним чином: коли ми зустрічаємо символ \r, 
# то повертаємося на початок рядка і продовжуємо виведення. Це перезаписує попередній вивід
print("Hello my little\rsister")

#Керувальний символ \b забій (backspace)
# Виведення здійснюється на один символ вліво та виконує вивід залишку після керувального символу
print("Hello\bWorld")

#Також якщо нам треба виконати виведення зворотної косої риски.
print("Hello\\World")

#Щоб екранувати одинарні та подвійні лапки та дозволити 
# використовувати лапки всередині рядкових літералів.
print('It\'s a beautiful day')
print("He said, \"Hello\"")


s = "Hi there!"
start = 0
end = 7
print(s.find("er", start, end)) # 5
print(s.find("q")) # -1


s = 'Some words'
print(s.find("o"))
print(s.rfind('o'))

s = 'Some words'
print(s.index("o"))
print(s.rindex('o'))


str.split(separator=None, maxsplit=-1)

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']


string.join(iterable)
list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'


clean = '   spacious   '.strip()
print(clean) # spacious


str.replace(old, new, count=-1)

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))


url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)


number = "12345"
print(number.isdigit())  # Виведе: True
text = "Number123"
print(text.isdigit())  # Виведе: False


user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "This is string example"
print(str.translate(trantab))


intab = "aeiou"
trantab = str.maketrans('', '', intab)
str = "This is string example"
print(str.translate(trantab))


symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]
MAP = {}
for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c
result = "34 DF 56 AC".translate(MAP)
print(result)


morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}
# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v
string = "Hello world"
result = ""
for ch in string:
    result = result + ch.upper().translate(table_morze_dict)
print(result)


for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)


price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total)


width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')

name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)


completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)


import re

re.search(pattern, string)


#виконаємо пошук слова "Python" у рядку
import re
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)
if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


#виконаємо пошук слова, що починається на "в" та закінчується на "м"
import re
text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Знайдено:", match.group())


#Розглянемо простеньку задачу - знаходження електронної адреси в рядку
import re
text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Електронна адреса:", match.group())

#вилучити ім'я користувача та домен цієї електронної адреси окремо.
import re
email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)
if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)


import re
matches = re.findall(pattern, string)

#Необхідно знайти всі числа у рядку
import re
text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)
print(matches)

#Необхідно зробити вибірку всіх слів в тексті
import re
text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)
print(matches)  # Виведе список всіх слів у рядку


#приклад знаходження електронних адрес
import re
text = "Контакти: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)
print(matches)  # Виведе всі знайдені електронні адреси


import re
modified_string = re.sub(pattern, repl, string)

#Замінити всі пробільні символи на підкреслення
import re
file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)
print(formatted_name)  

#Видалимо всі пунктуаційні знаки з рядка.
import re
text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)
print(modified_text)  

#форматування телефонних номерів. Нам необхідно змінити формат телефонних номерів
import re
phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)
print(formatted_phone)


import re
list_of_elements = re.split(pattern, string)

#розділимо рядок на слова, використовуючи пробіли як роздільники.
import re
text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)
print(words)  # Виведе список слів у рядку

#Спробуємо розділити рядок на частини, використовуючи пунктуаційні знаки як роздільники
import re
text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)
print(elements)  # Виведе список частин, розділених пунктуацією

#Виконаємо, ще один розділ рядка за шаблоном, що містить кілька можливих роздільників
import re
text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)
print(fruits)





