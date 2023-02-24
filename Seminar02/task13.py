# Задача No13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


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


sizeMin = 1
sizeMax = 100

size = inputCheck(
    f'Введите количество дней (от {sizeMin} до {sizeMax}): ', sizeMin, sizeMax)


tempMin = -50
tempMax = 50

limit = 0

count = 0
countMax = 0

arrayTemp = []

for i in range(size):
    number = inputCheck(
        f'День {i + 1}. Введите температуру (от {tempMin}˚C до {tempMax}˚C): ', tempMin, tempMax)
    if number > limit:
        count += 1
        if countMax < count:
            countMax = count
    if number <= limit:
        count = 0
    arrayTemp.append(number)

print()
print(f'Массив температур: {arrayTemp}')
print()
print(
    f'Максимум дней подряд, когда температура была выше {limit}˚C: {countMax}')
print()
