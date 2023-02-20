# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


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


number = inputCheck('Введите количество журавликов: ')

# Число журавликов кратно 6
magicNumber = 6
# А Катя — молодец на производстве
magicNumberKate = 4

resultFloat = number / magicNumber

resultInt = number // magicNumber

if resultFloat == resultInt:
    print(f'Петя сделал: {resultInt}')
    print(f'Сережа сделал: {resultInt}')
    print(f'Катя сделала: {resultInt * magicNumberKate}')

if resultFloat != resultInt:
    print('Задача не имеет решения в целых числах')
