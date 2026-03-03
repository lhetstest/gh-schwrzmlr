#Необхідно створити функцію discount_price на Python, яка розраховує кінцеву ціну товару після застосування знижки.

#Задачі:

#Створіть функцію discount_price, яка приймає два аргументи: price - початкова ціна товару та discount - знижка як дійсне число від 0 до 1.
#Усередині функції discount_price створіть вкладену функцію apply_discount, яка використовує nonlocal для доступу та модифікації змінної price.
#Функція apply_discount має обчислити знижену ціну, помноживши price на (1 - discount).
#Викличте apply_discount всередині discount_price, а потім поверніть оновлену ціну.
#Очікуваний результат: Функція повинна повертати ціну товару після застосування знижки.
# Підказки:

#Використання nonlocal дозволяє функції apply_discount модифікувати змінну price, оголошену у зовнішній функції discount_price.
#Для розрахунку зниженої ціни використовуйте формулу price * (1 - discount).
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price *= (1 - discount)
    apply_discount()
    return price

#10
def get_fullname (first_name, last_name, middle_name = ""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

#11
"""
Напишіть функцію format_string, яка центрує рядок у рамках заданої довжини length.

Задачі:

Створіть функцію format_string, яка приймає два аргументи: string рядок, який потрібно форматувати та length довжина, у межах якої потрібно центрувати рядок.
Якщо довжина string більша або дорівнює length, поверніть рядок без змін.
Якщо довжина string менша за length, додайте перед рядком пробіли, для того, щоб рядок був центрований у рамках length. Кількість пробілів визначте за формулою (length - len(string)) // 2.
Поверніть з функції відформатований рядок, що центрується у межах length.
Очікуваний результат:

Функція format_string повертає відформатований рядок відповідно до заданих правил.

Підказки:

Використовуйте len() для визначення довжини рядка.
Для створення рядка з пробілів використовуйте " " * кількість_пробілів.
"""
def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        return " " * spaces + string


