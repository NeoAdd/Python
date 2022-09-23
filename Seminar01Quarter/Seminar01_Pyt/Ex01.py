# По двум заданным числам проверить является ли одно квадратом второго
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(a ** 2 == b or b ** 2 == a)


# Найти максимальное из пяти чисел
# lst = [1, 3, 5, -1, 22]3
#lst = []
#for i in range(5):
    #num = int(input("Введите число: "))
    #lst.append(num)

#res = lst[0]
#for i in range(1, 5):
    #if lst[i] > res:
        #res = lst[i]
#print(res)


#вывести данные от до
#n = int(input("Введите число: "))
#for i in range(-n, n + 1):
#print(i)


# Напишите программу, которая будет 
# принимать на вход дробь и показывать первую цифру дробной части числа

#number - float(input("введите число"))
#for i in range (-n, n+1):
#    print(i, end -" ")

#Напишите программу, которая принимает 
#на вход число и проверяет, кратно ли 
#оно 5 и 10 или 15, но не 30.

#n - float(input("введите число"))
#if n % 5==0 and n%10==0 or n%15==0 and n%30==0:


Напишите программу для. 
проверки истинности 
утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'{x,y,z} : {(not(x or y or z)) == (not x and not y and not z)}')


# Сложить числа вещественного числа
n = input("Введите число: ")
res = 0
for i in n:
    if i != "." and i != ",":
        res += int(i)
print(res)


# Полидром

