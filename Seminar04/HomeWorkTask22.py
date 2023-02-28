# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


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
            print('Не удалось распознать число')
    return arg


# Функция ввода целого числа со знаком,
# с аргументом текстового приглашения
def inputCheckSign(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.lstrip("-").isdigit():
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')

    return arg


# Функция ввода массива в цикле
def inputArr(size):
    localArr = []
    for i in range(size):
        localArr.append(inputCheckSign(f'Введите {i + 1} число: '))
    return localArr


# n = inputCheck('Введите размер первого набора чисел: ')
# m = inputCheck('Введите размер второго набора чисел: ')

# print()
# print('Первый набор чисел')
# firstArr = inputArr(n)
firstArr = [5, 4, 3, 2, 1, 11, 6, 2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]


# print()
# print('Второй набор чисел')
# secondArr = inputArr(m)
secondArr = [1, 2, 3, 4, 5, 3, 6, 9, 12, 15, 18]

print(firstArr)
print(secondArr)

result = sorted(set(firstArr) & set(secondArr))

print(result)
