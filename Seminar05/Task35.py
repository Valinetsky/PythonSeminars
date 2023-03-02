# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and int(arg) > 1:
            arg = int(arg)
            flag = False
        if flag:
            print('Не удалось распознать число')
    return arg


# Функция определения, является ли введенное число простым
def Prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    start = 1
    while start * start < number:
        start += 2
        print(
            f'Проверяем делимость {number} на {start}. Остаток: {number % start}')
        if number % start == 0:
            return False
    return True


number = inputCheck('Введите число, для проверки на простоту: ')

print(f'Число {number} — простое') if Prime(
    number) else print(f'Число {number} — составное')
