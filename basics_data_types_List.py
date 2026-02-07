#List Method: pop()
simple_list = [1, 2, 3, 4, 5]

simple_list.pop(1)
print(simple_list)

#python3 basics_data_types.py
#[1, 3, 4, 5]

#List Method: pop() without index
simple_list = [1, 2, 3, 4, 5]
simple_list.pop()
print(simple_list)
#[1, 2, 3, 4]

#List Method: append()
simple_list = [1, 2, 3, 4, 5]
simple_list.append(6)
print(simple_list)
#[1, 2, 3, 4, 5, 6]

#List Method: insert()
simple_list = [1, 2, 3, 4, 5]
simple_list.insert(2, 2.5)
print(simple_list)
#[1, 2, 2.5, 3, 4, 5]

#List Method: remove()
simple_list = [1, 2, 3, 4, 5]
simple_list.remove(3)
print(simple_list)
#[1, 2, 4, 5]

#List Method: sort()
simple_list = [3, 1, 4, 5, 2]
simple_list.sort()
print(simple_list)
#[1, 2, 3, 4, 5]

#List Method: reverse()
simple_list = [1, 2, 3, 4, 5]
simple_list.reverse()
print(simple_list)
#[5, 4, 3, 2, 1]

#List Method: index()
simple_list = [1, 2, 3, 4, 5]
index_of_3 = simple_list.index(3)
print(index_of_3)
#2
#List Method: count()
simple_list = [1, 2, 3, 2, 4, 2, 5]
count_of_2 = simple_list.count(2)
print(count_of_2)
#3
#List Method: extend()
simple_list = [1, 2, 3]
simple_list.extend([4, 5, 6])
print(simple_list)
#[1, 2, 3, 4, 5, 6]

#List Method: clear()
simple_list = [1, 2, 3, 4, 5]
simple_list.clear()
print(simple_list)
#[]

#List Method: len()
simple_list = [1, 2, 3, 4, 5]
length_of_list = len(simple_list)
print(length_of_list)
#5

#List Method: sort() with key, where key = len means sorting by length of the string
words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']
