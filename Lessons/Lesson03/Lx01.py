# числа от одного до ста четные
list = []

for i in range(1, 21):
    if(i%2 == 0):
        list.append(i)

print(list)

print('короткое исполнение')

list = [i for i in range(1, 21) if i%2 == 0]
print(list)

print(' кортежи короткое исполнение')

list = [(i, i) for i in range(1, 21) if i%2 == 0]
print(list)

print('делаем действия с функцией')

def f(x):
    return x**3
list = [f(i) for i in range(1, 21) if i%2 == 0]
print(list)

print('кортеж делаем действия с функцией')

def f(x):
    return x**3
list = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
print(list)

