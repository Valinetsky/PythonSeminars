# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheckPositive(message):
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


# Функция поиска числа в списке, максимально близкого к введенному
def minimumDifferenceNumberInList(arr, number):

    if number in arr:
        return number

    localArr = list(set(arr))

    if len(localArr) < 2:
        return localArr[0]

    diff = abs(localArr[0] - number)
    outElement = localArr[0]

    for element in localArr[1:]:
        localDiff = abs(element - number)
        if diff > localDiff:
            diff = localDiff
            outElement = element

    return outElement


# Входящий список
arr = [12, 0, -1, 1, 1, 2, -4, 51, 51, 51, 12]

# arr = []

# listsize = inputCheckPositive('Введите размер списка: ')

# for i in range(listsize):
#     arr.append(inputCheck(f'Введите элемент {i + 1} списка: '))

print('Исходный список')
print(arr)

number = inputCheck('Введите число для поиска в списке: ')

result = minimumDifferenceNumberInList(arr, number)

print(f'Число в списке, максимально близкое к введенному: {result}')
