# Лекция 1 Знакомство Python

# типы данных и переменная
# int, float, boolean, str, list, None

value = None # переменная только в таком виде

a = 123
b = 1.23

print(a)
print(b)

value = 12345
print(value)


print(type(a)) #Определим тип данных type (int)
print(type(b)) # (float)
print(type(value))# (int)

# Объявляем строку
s = 'hello world'
s1 = "'hello world'"
s2 = "'hello \'world'"
s3 = "'hello \nworld'"
print(s) # вывод строки
print(s1) # вывод строки с ковычками
print(s2) # вывод строки Esc последовательность
print(s3) # вывод строки переход на новую строку

# Интерполяция - преобразованный, нахождение неизвестных промежуточных значений

print(a, b, s)
print(a, '-',b, '-' ,s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')
print('{1} - {2} - {0}'.format(a, b, s)) # можно поменять порядок


#Логическая переменная
t = True
f = False
print(True)
print(False)


#Списки (вместо массива)
list = [1, 2]
list2 = ['1', '2', '3', 'hello', 1, 2, 4, 5, True]  #динамическая типизация
print(list)
print(list2)


# Ввод и вывод данных

print('Введите a');
a = input ()
print('Введите b');
b = input ()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

print(a, ' + ' , b, ' = ', a+b ) #не считает а выводит


#Операции с input print

print('Введите a');
a = int (input())  # целые значения 
print('Введите b');
b = int (input())
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

print(a, ' + ' , b, ' = ', a+b ) # считает и выводит


#Арефметические операции
#  +,-,*,/,%,//,**

#Унарный плюс/минус
a = 123
b = 321
c=a+b
print(c)

# деление с выводом вещественного ответа
a = 12
b = 8
c=a/b
print(c)

# деление с выводом целого ответа
a = 12
b = 8
c=a//b
print(c)

# Получить остаток от деления
a = 12
b = 8
c=a%b
print(c)

# Возведение в степень **
a = 12
b = 8
c=b
print(c)


