# Задача №3.
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32


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
            print('Не удалось распознать число')
    return arg


Classes = []
for i in range(1, 4):
    Classes.append(inputCheck(f'Сколько учеников в Классе {i}: '))

deskCapacity = 2

summ = 0

for i in Classes:
    summ = summ + i // deskCapacity
    if i % deskCapacity > 0:
        summ += 1

print(f'Количество парт: {summ}')
