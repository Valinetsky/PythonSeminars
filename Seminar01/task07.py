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


year = inputCheck('Введите год: ')

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Год високосный.')
else:
    print('Год не високосный.')


# # Високосный ли год
# def isLeap(year):
#     if ((year & 3) == 0 and ((year % 25) != 0 or (year & 15) == 0)):
#         return True
#     return False


# print('Високосный год') if isLeap(year) else print('Год не високосный.')
