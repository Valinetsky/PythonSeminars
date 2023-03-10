# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


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


array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_number = inputCheck('Введите нижнюю границу диапазона: ')
max_number = inputCheck('Введите верхнюю границу диапазона: ')

if min_number > max_number:
    min_number, max_number = max_number, min_number
    print('Скорректированы значения диапазона')

result_array = []

for count, element in enumerate(array):
    if min_number <= element <= max_number:
        result_array.append((count, element))
print(result_array)
