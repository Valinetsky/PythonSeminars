# Задача 14: Требуется вывести все целые степени двойки(т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8


import math


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and int(arg) > 0:
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


n = inputCheck('Введите число N (N >= 1): ')

base = 2

result = math.log(n, base)

for k in range(int(result + 1)):
    print(f'{base} в степени {k} = {base ** k}')

print(f'N = {n}, log({n}, 2) = {result}')

# Или совсем просто:
# print(1)
# while base < n:
#     print(base)
#     base *= 2
