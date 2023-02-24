# Функция ввода целого числа со знаком,
# с аргументом текстового приглашения
def inputCheck(message, min, max):
    flag = True
    while flag:
        arg = input(message)
        if arg.lstrip("-").isdigit():
            arg = int(arg)
            if arg >= min and arg <= max:
                flag = False
        if flag:
            print('Failed to recognize the number')

    return arg
