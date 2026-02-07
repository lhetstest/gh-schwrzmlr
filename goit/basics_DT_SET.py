empty_set = set()
print(empty_set)  # Output: set()
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
my_set.discard(10)  # Не викликає помилку, коли 10 немає в множині
print(my_set)  # Output: {1, 2, 4, 5, 6}
my_set.pop()  # Видаляє і повертає випадковий елемент з множини
print(my_set)  # Output: {2, 4, 5, 6} (елемент 1 був видалений)
my_set.clear()
print(my_set)  # Output: set()

a = set('hello')
print(a)  # Output: {'l', 'o', 'e', 'h'} (унікальні символи з рядка)

b = {1, 2, 3, 4, 5, 3}
print(b)  # Output: {1, 2, 3, 4, 5} (повторювані елементи видаляються)

my_list = [1, 2, 3, 2, 3, 4, 5]
unique_elements = set(my_list)
print(unique_elements)  # Output: {1, 2, 3, 4, 5} (унікальні елементи з списку)

#Methods for set
my_set = {1, 2, 3}
print(len(my_set))  # Output: 3
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
my_set.discard(5)  # Не викликає помилку, коли 5 немає в множині
print(my_set)  # Output: {1, 3, 4}
my_set.pop()  # Видаляє і повертає випадковий елемент з множини
print(my_set)  # Output: {3, 4} (елемент 1 був видалений)
my_set.clear()
print(my_set)  # Output: set()

#Math perations with sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection = set_a.intersection(set_b)
print(intersection)  # Output: {3, 4}
union = set_a.union(set_b)
print(union)  # Output: {1, 2, 3, 4, 5, 6}
difference = set_a.difference(set_b)
print(difference)  # Output: {1, 2}
print(set_a - set_b)  # Output: {1, 2} (різниця множин set_a і set_b)
symmetric_difference = set_a.symmetric_difference(set_b)
print(symmetric_difference)  # Output: {1, 2, 5, 6}

print(set_a & set_b)  # Output: {3, 4} (перетин множин  set_a і set_b)
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5, 6} (об'єднання множин set_a і set_b)
print(set_a ^ set_b)  # Output: {1, 2, 5, 6} (симетрична різниця множин set_a і set_b)

#Заморожені множини в Python, відомі як frozenset, є подібними до звичайних множин set, але з ключовою відмінністю: вони є незмінними. Це означає, що після створення замороженої множини ви не можете додати або видалити елементи з неї.

frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})
simple_list = [1, 2, 3, 4, 5]
frozen_set_from_list = frozenset(simple_list)
print(frozen_set_from_list)  # Output: frozenset({1, 2, 3, 4, 5})
print(len(frozen_set))  # Output: 5
print(3 in frozen_set)  # Output: True
print(6 in frozen_set)  # Output: False
# frozen_set.add(6)  # Це викличе помилку, оскільки frozenset є незмінним
# frozen_set.remove(3)  # Це викличе помилку, оскільки frozenset є незмінним
intersection = frozen_set.intersection(frozenset([3, 4, 5, 6]))
print(intersection)  # Output: frozenset({3, 4, 5})
union = frozen_set.union(frozenset([3, 4, 5, 6]))
print(union)  # Output: frozenset({1, 2, 3, 4, 5, 6})
difference = frozen_set.difference(frozenset([3, 4, 5, 6]))
print(difference)  # Output: frozenset({1, 2})
symmetric_difference = frozen_set.symmetric_difference(frozenset([3, 4, 5, 6]))
print(symmetric_difference)  # Output: frozenset({1, 2, 6})

