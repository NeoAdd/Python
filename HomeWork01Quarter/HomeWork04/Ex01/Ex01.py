# Вычислить число c заданной точностью d

#Пример:

#- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math
d = input('задайте точность числа в следующем формате ( 0,00001)  :')

len_d = len(d) - 2
print(f"pi = {math.pi:.{len_d}f}")



