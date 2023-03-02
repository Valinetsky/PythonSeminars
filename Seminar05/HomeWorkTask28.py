# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только + 1 и - 1.
# Также нельзя использовать циклы.
# 2 2
# 4


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and int(arg) >= 0:
            arg = int(arg)
            flag = False
        if flag:
            print('Не удалось распознать число')
    return arg


# Функция рекурсивного сложения чисел А и Б
def SummRecursive(a, b):
    if b == 0:
        return a
    else:
        b -= 1
        return SummRecursive(a, b) + 1


# -------------------- ПОЕХАЛИ!!! ------------------
a = inputCheck('Введите число А: ')
b = inputCheck('Введите число Б: ')
print(f'Сумма чисел {a} и {b} равна: {SummRecursive(a, b)}')
