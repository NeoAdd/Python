print('hello')

start = False
while start == False:
    n = int(input('Введите положительное число: '))
    if n >= 1:
        start = True
    else:
        print('Неправильное число')
result = 0
for i in range(1, n + 1):
    result += (1 + 1 / i) ** i
print(round(result, 2))

