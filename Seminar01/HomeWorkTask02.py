# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


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


# Функция суммирования цифр числа
def getSum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum


flag = True
while flag:
    number = inputCheck('Введите трехзначное число: ')
    if number >= 100 and number <= 999:
        flag = False

print(f'Сумма цифр числа {number} = {getSum(number)}')
