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

print(text)
print(song)

one_line_text1 = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print(one_line_text1)
# Щоб структурувати код і не додавати зайвих перенесень, ви можете розбити одну рядкову змінну на декілька частин:
one_line_text2 = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print(one_line_text2)
("spam " "eggs") == "spam eggs"  # True
# Ця особливість часто використовується для зручності, особливо при написанні довгих рядків і тому змінну one_line_text можна записати наступним чином:

one_line_text3 = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")
print(one_line_text3)

# Неявна конкатенація рядків — це корисна особливість мови Python, яка дозволяє писати чистіший і читабельний код, особливо коли працюєте з довгими рядками або рядками, що формуються на основі декількох частин.
#  це дуже допомагає при створенні SQL-запитів до бази даних:
query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")
print(query)

# Symbols:
print("Hello\nWorld")
print("Hello\tWorld")
print("This is a backslash: \\")
print("She said, \"Hello!\"")
print('It\'s a nice day!')
print("Hello my little\rsister")
print("Hello\bWorld")
print("This is a form feed:\fEnd of line")
print("This is a vertical tab:\vEnd of line")

# String methods:
s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1
# Метод find() повертає індекс першого входження підрядка в рядок. Якщо підрядок не знайдено, він повертає -1. Ви можете також вказати початковий і кінцевий індекси для пошуку, щоб обмежити область пошуку.
# Метод index() працює аналогічно, але якщо підрядок не знайдено, він викликає помилку ValueError замість повернення -1. Тому, якщо ви не впевнені, що підрядок існує в рядку, краще використовувати find(), щоб уникнути потенційної помилки.
print(s.index("er", start, end)) # 5
# print(s.index("q")) # ValueError: substring not found

# І «правий» аналог index — rindex - шукає останнє входження підрядка в рядок і повертає його індекс. Якщо підрядок не знайдено, він також викликає помилку ValueError. Метод rfind() працює аналогічно, але повертає -1, якщо підрядок не знайдено.
s2 = " Some words and some more words. "
print(s2.rindex("e")) # 27
print(s2.index("e")) # 5

# Поділ та об'єднання рядків: str.split(separator=None, maxsplit=-1), separator - це рядок, який використовується для розділення рядка на частини. Якщо separator не вказано або None, рядок буде розділений за допомогою будь-якого пробільного символу (пробіл, табуляція, новий рядок і т.д.). maxsplit визначає максимальну кількість разів, які рядок буде розділений. Якщо maxsplit не вказано або -1, рядок буде розділений на всі можливі частини.

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']
text = "apple,banana,cherry"
result = text.split(",")
print(result)  # Виведе: ['apple', 'banana', 'cherry']

# Метод join() у Python використовується для об'єднання послідовності рядків (наприклад, списку або кортежу) в один рядок з використанням вказаного роздільника. Цей метод викликається на рядковому об'єкті, який служить роздільником:
# Синтаксис методу join()
# string.join(iterable)

separator = ", "
words = ["apple", "banana", "cherry"]
result = separator.join(words)
print(result)  # Виведе: "apple, banana, cherry"

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

# Якщо потрібно видалити зайві пробіли на початку і в кінці рядка, є спеціальний метод strip:

clean = '   spacious   '.strip()
print(clean) # spacious

# lstrip() видаляє пробіли зліва, а rstrip() видаляє пробіли справа:
left_clean = '   spacious   '.lstrip()
print(left_clean) # 'spacious   '
right_clean = '   spacious   '.rstrip()
print(right_clean) # '   spacious'

# replace() замінює всі входження підрядка на інший рядок:
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)  # Виведе: "Hello Python"

# str.replace(old, new, count=-1) - замінює всі входження підрядка old на new. Якщо вказано count, замінює лише перші count входжень.
text = "banana"
new_text = text.replace("a", "o", 2)
print(new_text)  # Виведе: "bonona" (замінює лише перші 2 входження "a" на "o")

# Метод replace() також застосовують для видалення підрядків, замінюючи їх на порожній рядок:
text = "Hello world"
new_text = text.replace("world", "")
print(new_text)  # Виведе: "Hello "(зверніть увагу на пробіл після "Hello")

# removeprefix() и removesuffix() - видаляють вказаний префікс або суфікс з рядка, якщо він там є. Якщо рядок не починається с префіксом або не закінчується суфіксом, то повертається оригінальний рядок без змін.

print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook
print('TestHook'.removesuffix('Hook')) # Test
print('TestHook'.removesuffix('Test')) # TestHook

# Розглянемо наступну задачу та використаємо основні інструменти для роботи з рядками — методи split() та replace(). Ви маєте URL пошукового запиту, і ваше завдання — видобути та обробити параметри цього запиту.

# Наприклад пошуковий запит «Cat and dog»:
# <https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>
# Нам треба написати код, який обробляє URL пошукового запиту, щоб видобути параметри запиту та перетворити їх у формат, з яким легше працювати в Python. Коли ви вводите пошуковий запит у браузері, він формує URL, де ваш запит та інші налаштування кодуються як ряд параметрів. Наш код повинен «розпаковувати» ці параметри, перетворюючи їх на словник Python, де ми можемо легко отримати доступ до кожного параметра за його ім'ям.
url = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"
# Розділяємо URL на дві частини: базовий URL та параметри
_, params = url.split('?', 1)
# Змінна url_search — це наш початковий URL. Далі операція url_search.split('?') розділяє URL на дві частини: до знаку ? та після. Оскільки нас цікавить лише частина після ?, ми використовуємо символ _ для ігнорування частини URL до ?. Та отримуємо змінну query яка рядок, що містить необхідні нам параметри запиту.
print(params)
param_pairs = params.split('&') # ['q=Cat+and+dog', 'ie=utf-8', 'oe=utf-8', 'aq=t']
print(param_pairs)
# Далі ми додамо до нашого коду обробку параметрів запиту:

obj_query = {}
for el in params.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

# В середині циклу, кожен параметр el містить ключ та значення, розділені символом =. Спочатку ми розділяємо кожен параметр el на ключ та значення key, value = el.split('=').
# Потім ми оновлюємо словник obj_query, додаючи нову пару ключ-значення. При цьому ми замінюємо символ + на пробіл у значенні, оскільки в URL-ах пробіли кодуються як +.

# метод isdigit() повертає True, якщо всі символи в рядку є цифрами, і False в іншому випадку. Це корисно для перевірки, чи рядок може бути перетворений на число.
print("12345".isdigit())  # Виведе: True
print("123a5".isdigit())  # Виведе: False
print("".isdigit())       # Виведе: False (порожній рядок не містить цифр)

user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


#method translate() використовується для заміни символів у рядку на основі заданої таблиці перекладу. Ця таблиця створюється за допомогою методу str.maketrans(), який приймає два рядки: перший містить символи, які потрібно замінити, а другий містить символи, на які потрібно замінити.
intab = "aeiou"
outtab = "12345"

str = "This is string example"

trantab = str.maketrans(intab, outtab)
print(str.translate(trantab)) # Th3s 3s str3ng 2x1mpl2

intab2 = "aeiou"
trantab2 = str.maketrans('', '', intab2)

str = "This is string example"
print(str.translate(trantab2)) # Ths s strng xmpl2

'''
Метод може бути використаний для різноманітних завдань з обробки тексту. Нормалізація тексту, це коли треба замінити або видалити специфічні символи. Операції кодування та декодування — створення простих кодувань шляхом заміни символів. Фільтрація тексту шляхом видалення небажаних символів, наприклад, пунктуації або цифр.
Перетворення шістнадцяткових у двійкові рядки:
'''

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
print(result) # Виведе: 00110100001111010001010110101100
print(MAP) # Виведе: {48: '0000', 49: '0001', 50: '0010', 51: '0011', 52: '0100', 53: '0101', 54: '0110', 55: '0111', 56: '1000', 57: '1001', 65: '1010', 66: '1011', 67: '1100', 68: '1101', 69: '1110', 70: '1111', 97: '1010', 98: '1011', 99: '1100', 100: '1101', 101: '1110', 102: '1111'}

# Де ключ — це Unicode для символів "0123456789ABCDEF" в верхньому та нижньому регістрі, а значення відповідні елементи списку code.

# Pозробити програму, яка перетворює вхідний текстовий рядок на відповідний код мови Морзе.

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

'''
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

Цикл for проходить по кожному елементу словника morze_dict та для кожного ключа словника morze_dict використовуючи функцію ord(k) додає до словника table_morze_dict Unicode ключі та відповідні коди Морзе — значеннями.

'''

# String Formatting:
# Наприклад, вивести числа від 1 до 15 в десятковому, шістнадцятковому, вісімковому і двійковому представленні можна наступним чином:

for i in range(16):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)
# Result:
# int: 0;  hex: 0x0;  oct: 0o0;  bin: 0b0
# int: 1;  hex: 0x1;  oct: 0o1;  bin: 0b1
# int: 2;  hex: 0x2;  oct: 0o2;  bin: 0b10
# int: 3;  hex: 0x3;  oct: 0o3;  bin: 0b11
# int: 4;  hex: 0x4;  oct: 0o4;  bin: 0b100
# int: 5;  hex: 0x5;  oct: 0o5;  bin: 0b101
# int: 6;  hex: 0x6;  oct: 0o6;  bin: 0b110
# int: 7;  hex: 0x7;  oct: 0o7;  bin: 0b111
# int: 8;  hex: 0x8;  oct: 0o10;  bin: 0b1000
# int: 9;  hex: 0x9;  oct: 0o11;  bin: 0b1001
# int: 10;  hex: 0xa;  oct: 0o12;  bin: 0b1010
# int: 11;  hex: 0xb;  oct: 0o13;  bin: 0b1011
# int: 12;  hex: 0xc;  oct: 0o14;  bin: 0b1100
# int: 13;  hex: 0xd;  oct: 0o15;  bin: 0b1101
# int: 14;  hex: 0xe;  oct: 0o16;  bin: 0b1110
# int: 15;  hex: 0xf;  oct: 0o17;  bin: 0b1111



# Форматування за допомогою виразів у f-рядках дозволяє не тільки вставляти значення змінних у рядок, а й форматувати ці значення за допомогою спеціальних вказівок.

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total) # Виведе: Total: 59.97

"""
У виразі :.2f:
: вводить специфікацію формату.
.2 означає, що після десяткової крапки має бути виведено дві цифри.
f вказує на формат дійсного числа.

при створенні рядків буває корисним відформатувати рядок так, щоб знаки на різних рядках були один під одним (додати пробілів), додати заповнення в рядки для того, щоб результат був завжди однієї й тієї самої довжини. Або вивести квадрати та куби чисел до 4 у вигляді таблиці, відцентрувавши значення у стовпцях по 8 символів шириною:
"""

width = 5
for num in range(4):
    print(f'{num:^8} {num**2:^8} {num**3:^8}')
# Результат:
#    0         0         0
#    1         1         1
#    2         4         8
#    3         9        27

"""
Вирівнювання визначає, як вміст буде вирівняний всередині вказаної ширини поля. Можливі варіанти вирівнювання:

<: Вирівнювання вмісту по лівому краю.
>: Вирівнювання вмісту по правому краю.
^: Вирівнювання вмісту по центру.
=: Використовується для вирівнювання чисел, при цьому знак (якщо він є) відображається зліва, а число — по правому краю поля.

"""

name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)
formatted = f"{name:<10}"
print(formatted)  # Виведе: 'Alice     ' (вирівнювання ліворуч)
formatted = f"{name:^10}"
print(formatted)  # Виведе: '  Alice   ' (вирівнювання по центру)
formatted = f"{name:=<10}"
print(formatted)  # Виведе: '=====Alice' (вирівнювання зліва для знака, якщо він є)

"""
Форматування відсотків у f-рядках виглядає так:

f"{value:<ширина>.<точність>%}"

де:

value — значення, яке потрібно перетворити у відсотки.
<ширина> — загальна ширина поля; необов'язково.
<точність> — кількість знаків після десяткової крапки; необов'язково.

"""

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted)
# Виведе: '50%'
