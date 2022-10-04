from multiprocessing import current_process


print('hello')

#Напишите программу, в которой 
# пользователь будет задавать 
# две строки, а программа - определять 
# количество вхождений одной строки в другой.

my_text = 'привет мир привет друзья'
my_text_1 = 'привет'
my_list = my_text.split(" ")
current_e = 0
for i in my_list:
    if i == my_text_1:
        current_e += 1
print(current_e)




