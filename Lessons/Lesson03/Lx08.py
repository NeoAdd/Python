#   Функция    zip
#  применяется к набору интерируемых 
# объектов и возвращает интератор с 
# кортежами из элементов входных данных

user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 2, 3, 4, 5]

data = list(zip(user, ids))
print(data)

# Добавили еще один набор
user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 2, 3, 4, 5]
iidd = [111, 222, 333]

data = list(zip(user, ids, iidd))
print(data)


# функция enumerate просто нумерует от 0

user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 2, 3, 4, 5]
iidd = [111, 222, 333]

data1 = list(enumerate(user))

print(data1)


data2 = list(enumerate(ids))

print(data2)

