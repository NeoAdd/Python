# Напишите программу вычисления 
# арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. 
# приоритет операций стандартный


list = input('Введите выражение: ')
print(list)
result = 0
if list.find('+') != -1:
    list = list.split("+")   # 2+3*9
    result = int(list[0]) + int(list[1])
elif list.find('-') != -1:
    list = list.split("-")   # 2+3*9
    result = int(list[0]) - int(list[1])
print(result)
