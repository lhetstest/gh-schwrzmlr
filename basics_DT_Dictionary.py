my_dict = {}

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
# {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict["name"])  # Виведе 'Alice'
my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)
# {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
del my_dict["city"]  # Видаляє пару ключ-значення з ключем 'city'
print(my_dict)
# {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
print(my_dict.keys())  # Виведе dict_keys(['name', 'age', 'email'])
print(my_dict.values())  # Виведе dict_values(['Alice', 26, 'alice@example.com'])

#dictionary method update()
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"age": 26, "city": "New York"})
print(my_dict)
# {'name': 'Alice', 'age': 26, 'city': 'New York'}

print("name" in my_dict)
print("city" in my_dict)
# True
# False

my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику

# Dictionary method pop()
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
age = my_dict.pop("age")  # Поверне 25 і видалить пару ключ-значення з ключем 'age'
print(age)  # 25
print(my_dict)
# {'name': 'Alice', 'city': 'New York'}

