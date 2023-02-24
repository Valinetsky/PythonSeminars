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
