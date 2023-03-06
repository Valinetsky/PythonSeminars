# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# Функция ввода целого числа со знаком,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.lstrip("-").isdigit():
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


# Функция рекурсивного возведения А в степень Б
def Steps(a, b):
    if b == 1:
        return a
    else:
        b -= 1
        return a * (Steps(a, b))


# Функция проверки знака степени
def StepsSign(a, b):
    if b == 0:
        return 1
    if b > 0:
        return Steps(a, b)
    if b < 0:
        b = -b
        return 1 / Steps(a, b)


# -------------------- ПОЕХАЛИ!!! ------------------
a = inputCheck('Введите число А: ')

flag = True
while flag:
    b = inputCheck('Введите число Б: ')
    if a != 0 or b >= 0:
        flag = False
    if b < 0 and a == 0:
        print(f'Выражение {a} в степени {b}: не имеет смысла')

print(f'Число {a} в степени {b}: {StepsSign(a, b)}')
