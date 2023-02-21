# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N(произведение всех
#                                     чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120


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
            print('Failed to recognize the number')
    return arg


# функция рассчета факториала
def factorio(number):

    result = 1

    if number == 0:
        return result

    while number > 1:
        result = result * number
        number -= 1
    return result


number = inputCheck('Введите число для рассчета факториала: ')
print(f'Факториал равен {factorio(number)}')