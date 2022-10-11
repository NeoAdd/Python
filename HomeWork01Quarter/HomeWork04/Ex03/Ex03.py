# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов исходной 
# последовательности.


import random

def fill_number_list(n=20, min=10, max=99) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def filt_values_list(user_list) -> list:
    new_list = [user_list[0]]
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                break
            elif j == len(new_list)-1:
                new_list.append(user_list[i])
    return new_list

first_list = fill_number_list(20, 10, 50)
filt_list = filt_values_list(first_list)
print(f'Первый список {first_list} -> отфильтрованные значения (без дубликата)')
print(filt_list)
