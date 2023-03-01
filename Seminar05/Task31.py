# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
# = 0, a1
# = 1, ak
# = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


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


# Функция поиска числа Фибоначчи
def Fibo(number):
    if number == 2 or number == 1:
        return 1
    return Fibo(number - 1) + Fibo(number - 2)


number = inputCheck('Введите номер числа в последовательности Фибоначчи: ')

print(Fibo(number))
