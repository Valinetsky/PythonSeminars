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


def calculate(b, c):
    D = b * b - 4 * c  # считаем дискриминант
    if D > 0:  # если дискриминанат > 0 - два корня
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq

        print(x1)
        print(x2)

        return x1 if x1 >= 0 else x2

    if D == 0:
        return b/2

    if D < 0:
        return -1


numbersSum = inputCheck('Введите сумму чисел: ')
numbersMul = inputCheck('Введите произведение чисел: ')


numberOne = calculate(numbersSum, numbersMul)


print()
print(f'Первое число: {numberOne}')
print()
print(f'Второе число: {numbersSum - numberOne}')
print()
