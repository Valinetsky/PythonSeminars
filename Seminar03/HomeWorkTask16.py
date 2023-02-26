# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 3
# -> 1


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


# Функция подсчета вхождений числа в список
def countNumberInList(list, number):
    counter = 0
    for element in list:
        if element == number:
            counter += 1
    return counter


# Входящий список
# list = [1, 1, 2, 0, -1, 3, 4, 4]
list = []

listsize = inputCheckPositive('Введите размер списка: ')

for i in range(listsize):
    list.append(inputCheck(f'Введите элемент {i + 1} списка: '))

print('Исходный массив')
print(list)

number = inputCheck('Введите число для поиска в массиве: ')

result = countNumberInList(list, number)

print(f'Число {number} есть в списке. Количество вхождений: {result}') if result > 0 else print(
    f'Числа {number} нет в списке.')
