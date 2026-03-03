# *args in functions allows you to pass a variable number of arguments to a function.
# result of the function will be a tuple of all the arguments passed to it.
def my_function(*args):
    return args
result = my_function(1, 2, 3, "hello", [1, 2, 3])
print(result) # Output: (1, 2, 3, 'hello', [1, 2, 3])

# позиційні аргументи - це аргументи, які передаються функції в певному порядку. Вони визначаються за допомогою позиції, в якій вони передаються при виклику функції. Наприклад:
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."
print(greet("Alice", 30)) # Output: Hello, Alice! You are 30 years old.

def print_all_args(*args):
    for arg in args:
        print(arg)

print_all_args(1, 'hello', True)

def concatenate(*args) -> str:
    result = ""
    for arg in args:
        result += arg
    return result
print(concatenate("Hello", " ", "world", "!")) # Output: Hello world!

#Під час виклику функції, всі позиційні аргументи, передані після останнього визначеного аргументу, будуть упаковані в кортеж під ім'ям, що йде після символу * і зазвичай це ім'я args, але може й бути будь-яке інше ім'я. Наступний приклад теж працюватиме, але загально прийнято називати цей параметр args:

def concatenate(*strings) -> str:
    result = ""
    for arg in strings:
        result += arg
    return result

#Параметр **kwargs використовується у визначенні функції для вказівки на те, що функція може приймати довільну кількість ключових аргументів. Назва kwargs пішла від keyword arguments та дозволяє передавати в функцію іменовані аргументи у вигляді словника.
# **kwargs in functions allows you to pass a variable number of keyword arguments to a function.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

person_info = {"name": "Alice", "age": 25}

greet(**person_info)
# Output: Hello Alice, you are 25 years old.
print("========================================")
print("==== Now used both ARGS and KWARGS ====")
print("========================================")
def example_function(*args, **kwargs):
    print("Позиційні аргументи:", args)
    print("Ключові аргументи:", kwargs)

example_function(1, 2, 3, name="Alice", age=25)

# Розпакування словників часто використовується для передачі іменованих аргументів у функції, особливо коли кількість аргументів або їхні імена не відомі заздалегідь.
my_list = [1, 2, 3]
a, b, c = my_list
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Якщо вам потрібно ігнорувати деякі з елементів списку під час розпакування, можна використовувати _:
a, _, c = my_list
print(a)  # Output: 1
print(c)  # Output: 3

# Можна також розпакувати частину списку, використовуючи *:

a, *rest = my_list
print(a)    # Output: 1
print(rest) # Output: [2, 3]



def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
person_info = {"name": "Alice", "age": 25}
greet(**person_info) # Output: Hello Alice, you are 25 years old.