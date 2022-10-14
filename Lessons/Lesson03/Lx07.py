# Функция ФИЛЬТР "filter"

from datetime import date


data = [x for x in range(10)]

res = list(filter(lambda x: not x%2, data))
print(res)


#  берет значение из списка и 
# выводит кортеж числа и его квадрата



#    УБРАЛИ функцию WHERE
#def select(f, col):
    #return [f(x) for x in col]

#ef where(f, col):
#    return [x for x in col if (x)]

data = '1 2 3 4 5 6 7 8 15 23 38'.split()  

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))


print(res)


