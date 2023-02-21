# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


from math import sqrt

# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения


def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and (int(arg) > 0 and int(arg) < 1000):
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


# Функция расчета дискриминанта
def calculate(b, c):
    D = b * b - 4 * c
    if D > 0:
        sq = sqrt(D) / 2
        p = b/2
        return p + sq

    if D == 0:
        return b/2

    return -1


numbersSum = inputCheck('Введите сумму чисел: ')
numbersMul = inputCheck('Введите произведение чисел: ')

numberOne = calculate(numbersSum, numbersMul)
numberTwo = numbersSum - numberOne

if numberOne < 0 or numberTwo < 0:
    print('Нет таких натуральных чисел')

if numberOne > 0 and numberTwo > 0:
    print()
    print(f'Загаданные числа: {int(numberOne)}, {int(numberTwo)}')
    print()
