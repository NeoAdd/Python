#3) Задайте список из n чисел последовательности 
# (1+ (1/n))^n и выведите на экран их сумму.

#Пример:

#Для n = 5: сумма = 11,55


from cgitb import reset


a = False
while a == False:
    n = int(input("Введи число для нахождения (1+ (1/n))^n: "))
    if n >= 1:
        a = True
    else:
        print('ошибка')
bank = 0
for i in range(1, n + 1):
    bank += (1 + 1 / i) **i
print(round(bank, 2))


