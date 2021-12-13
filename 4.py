import random
a = [26, 74, 85, 12, 1, 20]
b = int(input("Введите предпологаемое число из 26, 74, 85, 12, 1, 20:"))
a = random.random(a)
if a!=b:
    print("Угадал")
else:
    print("Не угадал")
