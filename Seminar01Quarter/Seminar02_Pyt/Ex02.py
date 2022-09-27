# Четверти

q = int(input('Input number of Quoter :'))

match q:
    case 1:
        print(' X > 0 and Y > 0')
    case 2:
        print(' X < 0 and Y > 0')
    case 3:
        print(' X < 0 and Y < 0')
    case 4:
        print(' X > 0 and Y < 0')
    case _:
        print('Uncorrect number')


