# Напишите программу каторая секунды 
# переводит в дни часы минуты секунды

sec = int(input('вапваымп'))
min, sec = sec // 60, sec % 60
hour, min = min // 60, min % 60
day, hour = hour // 24, hour % 24
print(f"{day}:{hour}:{min}:{sec}")
