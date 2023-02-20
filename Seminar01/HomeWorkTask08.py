# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


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


numberX = inputCheck('Введите ширину шоколадки: ')
numberY = inputCheck('Введите длину шоколадки: ')
chokoPart = inputCheck('Введите число долек на отлом: ')

if chokoPart < numberX * numberY and ((chokoPart % numberX == 0) or (chokoPart % numberY == 0)):
    print('Можно отломить')
else:
    print('Не получится отломить')
