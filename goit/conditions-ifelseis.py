a = [1,2,3]
b = a
c = [1,2,3]

print(a is b) #True, тому що a і b посилаються на один і той же об'єкт у пам'яті
print(a is c) #False, тому що a і c посилаються на різні об'єкти у пам'яті, навіть якщо вони мають однакові значення
print(a == c) #True, тому що оператор == порівнює значення об'єктів, і a і c мають однакові значення [1, 2, 3]

#Boolean values
num = int(input("Введіть число: "))

length = len(str(num))

if length == 2 and num % 2 == 0: #Перевіряємо, чи є число двозначним і парним
    print("Парне двозначне число")
else:
    print("Ні")

#operator AND
print(True and True)   # Output: True
print(True and False)  # Output: False
print(False and True)  # Output: False
print(False and False) # Output: False

#operator OR
print(True or True)    # Output: True
print(True or False)   # Output: True
print(False or True)   # Output: True
print(False or False)  # Output: False

#operator NOT
print(not True)  # Output: False
print(not False) # Output: True

a = not 2 < 0  # True

# Задаємо конкретне число
num = int(input())

# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0: # Якщо число кратне і 3, і 5
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# Блоки та тернарний оператор
x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x

# Використання тернарного оператора для визначення знаку результату
sign = "positive" if result > 0 else "negative" if result < 0 else "zero"
print(f"The result is {result} and it is {sign}.")

# another example of ternary operator
is_nice = True
state = "nice" if is_nice else "not nice"
print(f"The state is {state}.")

# Використання логічного оператора OR для надання значення за замовчуванням
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)
# Зверніть увагу, що для скороченої форми використовується саме оператор or (АБО).

# operator match
command = input("Enter a command: ")
match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "pause":
        print("Pausing the engine...")
    case _: # symbol _ використовується для позначення випадку за замовчуванням, коли жоден з попередніх випадків не збігається
        print("Unknown command.")

#оператор має більш розширену сферу використання. Наприклад, використання змінних у шаблонах. Розглянемо приклад:
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

# cycle for
fruit = 'apple'
for char in fruit:
    print(char)
# Output:
# a
# p
# p
# l
# e

# cycle while
while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break

# cycle while  with continue
a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)

# цикл for з оператором break
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(1, 10):
    if i % 2 == 0:
        print(f"{i} є парним числом.")
    else:
        print(f"{i} є непарним числом.")
