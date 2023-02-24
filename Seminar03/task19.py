# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


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


lst = [1, 2, 3, 4, 5]
print(lst)

shift = inputCheck('Введите размер сдвига списка: ')
shift = - shift % len(lst)

lst = lst[shift:] + lst[:shift]

print(lst)
