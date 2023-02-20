# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit():
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


# Функция суммирования цифр числа
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


flag = True
while flag:
    number = inputCheck('Введите шестизначное число: ')
    if number <= 999999:
        flag = False

cut3digit = 1000
partLeft = number // cut3digit
partRight = number - partLeft * cut3digit

partLeft = getSum(partLeft)
partRight = getSum(partRight)

if partLeft == partRight:
    print('Счастливый билет')

if partLeft != partRight:
    print('Обычный билет')
