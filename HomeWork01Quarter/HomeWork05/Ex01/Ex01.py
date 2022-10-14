print('Игра с конфетами.')


sweet = 2021
while sweet >= 0:
    pleer = int(input('Бери конфеты, но не более 28 '))
    if pleer > 28 or pleer > sweet:
        print('нарушение правил! Начинай сначала')
        break
    else:    
        sweet -= pleer
        print('Осталось конфет')
        print(sweet)
        if sweet == 0:
            print('Победил игрок забравший последнию конфету')
            break

