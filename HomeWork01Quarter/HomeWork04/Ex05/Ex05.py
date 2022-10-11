# Задана натуральная степень k. 
# Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.


import random
x1 = open("result.txt", "w")
k = int(input("Введите число:   "))
lst = [random.randint(0,100) for i in range(k + 1)]
print(lst)
x = ""
for i in range(k + 1):
    if i < k:
        x += str(lst[i]) + "*x^" + str(k-i)  +  " + " 
    else:
        x += str(lst[i])
print(x)

x1.write(f'{x}  \n')
x1.close()
