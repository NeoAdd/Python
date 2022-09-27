# ищем символы в строке


string = " Посчитайте сколько раз символы встречаются в строке "
res = 0
simb = "а"
for i in string:
    if i ==simb:
        res+=1
print(res)

