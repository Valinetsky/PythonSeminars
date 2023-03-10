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
        if arg.isdigit() and (int(arg) > 0 and int(arg) <= 1000):
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


# Функция расчета дискриминанта
def calculate(b, c):

    D = b * b - 4 * c

    if D >= 0:
        sq = sqrt(D) / 2
        p = b / 2
        x1 = p - sq
        x2 = p + sq
        return [x1, x2]

    return [-1, -1]


numbersSum = inputCheck('Введите сумму чисел (n > 0): ')
numbersMul = inputCheck('Введите произведение чисел (n > 0): ')

secret = calculate(numbersSum, numbersMul)

if secret[0] != int(secret[0]) or secret[0] == -1:
    print('Нет таких целых положительных чисел')
else:
    print()
    print(f'Загаданные числа: {[int(num) for num in secret]}')
    print()
