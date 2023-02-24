# # Функции ввода числа, допускающие знак и десятичную точку
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if is_number(arg):
            arg = float(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
