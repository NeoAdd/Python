print('Игра с конфетами. ЧЕЛОВЕК / БОТ')


sweet = 2021
while sweet >= 0:
    pleer = int(input('Бери конфеты, но не более 28 штук :  '))
    if pleer > 28 or pleer > sweet:
        print('нарушение правил! Начинай сначала')
        break
    else:    
        sweet -= pleer
        print('Осталось конфет')
        print(sweet)
                
        if sweet == 0:
            print('Победил Человек')
            break
        else:
                print('Теперь ходит БОТ')
                sweet = sweet -1
                print('Осталось конфет')
                print(sweet)
                if sweet == 0:
                    print('Победил БОТ')
                    break


