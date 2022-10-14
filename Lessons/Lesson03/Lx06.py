#  берет значение из списка и 
# выводит кортеж числа и его квадрата

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if (x)]

data = '1 2 3 4 5 6 7 8 15 23 38'.split()  

res = map(int, data)
res = where(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))


print(res)
