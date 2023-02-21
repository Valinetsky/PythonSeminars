# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n) = A. Если А не
# является числом Фибоначчи, выведите число - 1.
# Input: 5
# Output: 6


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
            print('Failed to recognize the number')
    return arg


# Функция генерации следующего числа Фибоначчи
def fibo(number):
    start = 1
    next = 1
    counter = 4

    while True:
        current = start + next
        if current == number:
            return counter
        if current > number:
            return -1

        start = next
        next = current
        counter += 1


number = inputCheck('Введите число: ')

result = fibo(number)

if result != -1:
    print(f'Число {number} в последовательности Фибоначчи на позиции {result}')

if result == -1:
    print(f'Число {number} не является членом последовательности Фибоначчи')
