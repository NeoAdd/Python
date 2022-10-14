from turtle import color
from unittest.mock import patch


s = 'Работа с файлами читать, записывать, добавление'

print(s) # вывод строки

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')  
# a- открытие для добавление данных
# r- открытие для чтение данных
# w- открытие для записи данных

#data.writelines(colors) # разделителя не будет
data.write('\nLINE 12\n')
data.write('\nLINE 13\n')
data.close()

exit()
patch = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


