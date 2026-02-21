import datetime

yr = datetime.datetime.now().year
print(yr)
## 2026

import datetime
now = datetime.datetime.now()
print(now)
# 2026-02-15 23:29:08.003763

from datetime import datetime

from datetime import datetime

current_datetime = datetime.now()

print("Year: ", current_datetime.year)
print("Month: ", current_datetime.month)
print("Day: ", current_datetime.day)
print("Hour: ", current_datetime.hour)
print("Minute: ", current_datetime.minute)
print("Second: ", current_datetime.second)
print("Microsecond: ", current_datetime.microsecond)
print("TimeZone: ", current_datetime.tzinfo)

# В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):
print("Date: ", current_datetime.date())
print("Time: ", current_datetime.time())

# зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування об'єктів date та time. Це дозволяє створювати точний момент часу, вказуючи дату та час окремо, а потім об'єднуючи їх.
# datetime.datetime.combine(date_object, time_object)

from datetime import datetime, date, time

# Example of using datetime.combine
today = date.today()
current_time = time(12, 30, 45)  # 12:30:45

combined_datetime = datetime.combine(today, current_time)
print("Combined DateTime:", combined_datetime)

print("=============================")
print("==== Example from theory ====")
print("=============================")

import datetime

# Створення об'єктів date і time
date_part = datetime.date(2026, 2, 15)
time_part = datetime.time(12, 38, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Для створення об'єкта datetime з певною датою:

specific_datetime = datetime.datetime(2026, 2, 15, 12, 38, 15)
print(specific_datetime)  # Виведе "2026-02-15 12:38:15"


# Створення об'єкта datetime з конкретною датою
specific_date = datetime.datetime(year=2020, month=1, day=7)
print(specific_date)  # Виведе "2020-01-07 00:00:00"

from datetime import datetime

# Створення об'єкта datetime
now_wd = datetime.now()

# Отримання номера дня тижня
day_of_tweek = now_wd.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_tweek}")


# work with timestamps

from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime

# Парсинг дати із рядка

# Коли потрібно відобразити дату та час у зрозумілому для людини форматі, ми використовуємо метод strftime. Він застосовується при записуванні часових міток у файли логування, при відображанні дати та часу на вебсторінках або в інтерфейсах користувача, а також при форматуванні дат для збереження в базах даних.

# Отже, метод strftime використовується для форматування об'єктів дати та часу datetime у рядки за допомогою специфічних форматних кодів. Цей метод дає можливість представити дату та час у зручному для читання форматі або в форматі, що відповідає специфічним вимогам.

datetime_object.strftime(format)


