#strings and it's methods
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!

# String Method: lower()
lower_string = my_string.lower()
print(lower_string)  # Output: hello, world!
# String Method: upper()
upper_string = my_string.upper()
print(upper_string)  # Output: HELLO, WORLD!
# String Method: strip()
string_with_spaces = "   Hello, World!   "
stripped_string = string_with_spaces.strip()
print(stripped_string)  # Output: Hello, World!
# String Method: replace()
replaced_string = my_string.replace("World", "Python")
print(replaced_string)  # Output: Hello, Python!
# String Method: split()
split_string = my_string.split(", ")
print(split_string)  # Output: ['Hello', 'World!']
# String Method: join()
string_list = ['Hello', 'World!']
joined_string = " ".join(string_list)
print(joined_string)  # Output: Hello World!
# String Method: find()
index_of_world = my_string.find("World")
print(index_of_world)  # Output: 7, the index of the first occurrence of "World"
# String Method: format()
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 25 years old.

# String Method: count()
count_of_l = my_string.count("l")
print(count_of_l)  # Output: 3
# String Method: startswith()
starts_with_hello = my_string.startswith("Hello")
print(starts_with_hello)  # Output: True

# String Method: endswith()
s = "hello.jpg"
ends_with_jpg = s.endswith(".jpg")
print(ends_with_jpg)  # Output: True

# String Method: isdigit(), isalpha(), isspace()
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
print('Hello, {1}. You are {0} years old.'.format(age, name))  #Hello, John. You are 25 years old.

# String slicing
numbers = "0123456789"
print(numbers[2:5])    # Виведе '234' (з індексу 2 до 5, не включно)
print(numbers[:4])     # Виведе '0123' (з початку до індексу 4, не включно)
print(numbers[5:])     # Виведе '56789' (з індексу 5 до кінця)
print(numbers[-3:])    # Виведе '789' (останні три символи)
print(numbers[:-3])    # Виведе '0123456' (усі символи, крім останніх трьох)
print(numbers[::2])    # Виведе '02468' (кожен другий символ)
print(numbers[::-1])   # Виведе '9876543210' (рядок у зворотньому порядку)

'With width {width} and length {length} of the room, its area is equal to {area}'
