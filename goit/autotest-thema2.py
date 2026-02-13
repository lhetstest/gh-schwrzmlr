'''
Docstring for goit.autotest-thema2
'''
# 2
""" work_experience = int(input("Enter your full work experience in years: "))

if work_experience > 1 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

print("You are a " + developer_type + " developer.")

# 3
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 1: #odd це не парне число, тому перевіряємо на остачу від ділення на 2
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"

print(result)

#4

#Створіть програму на Python, яка розраховує суму всіх цілих чисел від 1 до числа, введеного користувачем.
# from ast import operator
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(sum)

#5

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for char in message:
    if char == search: result += 1 # one line if statement
print(result)
"""

#6

"""
Напишіть програму на Python, яка розраховує розмір кожного пакета SMS в кампанії маркетингу, уникаючи помилки поділу на нуль.

Задачі:

Ви маєте змінну pool, яка дорівнює 1000 - кількість SMS, доступних для відправлення.
Запросіть у співробітника маркетингу ввести кількість розсилок quantity.
Обчисліть розмір пакета SMS для кожної розсилки, змінна chunk, поділивши pool на quantity.
Використайте блок try-except для обробки можливої помилки ZeroDivisionError, яка може виникнути, якщо quantity буде дорівнювати 0.
Якщо виникає помилка ZeroDivisionError, виведіть повідомлення про неможливість поділу на нуль.
Очікуваний результат:

Програма має вираховувати розмір пакету SMS для розсилки, або виводити повідомлення про помилку при спробі поділу на нуль.

Підказки:

У блоку try розмістіть код, який може викликати помилку.
У блоку except вкажіть тип помилки, яку ви очікуєте, та дії, які слід виконати у випадку її виникнення.

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
    print("The size of each SMS package is: " + str(chunk))
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero quantity.")


#8
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

# for cycle case:

for i in range(10):
    print(i)
"""

# function zip
list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)


"""
Механізм обробки винятків
"""
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero. Please provide a non-zero divisor.")
else:
    print("The result is: " + str(result))
finally:
    print("This block will always be executed, regardless of exceptions.")

# Наївним розв'язанням цієї проблеми буде повсюдне використання перевірок if на коректність введеного користувачем або іншим застосунком значення. Просунутішим, зручнішим і прозорішим рішенням є використання механізму обробки винятків там, де вони можуть статися через некоректні вхідні дані.

age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")

#Функції, область видимості змінних (LEGB - Local, Enclosing, Global, Built-in)
