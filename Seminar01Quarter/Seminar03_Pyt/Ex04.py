print('hello')

text_1 = ["5", "8", "32", "55", "7", "8"]
num = 8
def find_digit(new_text, num):
    for i in range(len(new_text)):
        if new_text[i].isdigit():
            if int(new_text[i]) == num:
                print(i)
find_digit(text_1, num)

