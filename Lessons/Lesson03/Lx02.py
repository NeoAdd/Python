# Взять данные из файла, найти четные, 
# вывести кортеж и числа взятого и числа **3

path ='/Users/олег/Desktop/Учеба IT/git/Python/Lessons/Lesson03/file1.txt'


f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e,e **2))
print(out)        



