# Задача №29.
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем(число 0 не входит в
#                     последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.


n = int(input('Ванино решение: '))
max_number = 1000
while n != 0:
    n = int(input())
    if max_number > n:
        max_number = n
print(f'Ванино решение (финал):')
print(max_number)


print()


n = int(input('Петино решение: '))
max_number = -1
while n < 0:
    n = int(input())
    if max_number < n:
        n = max_number
print(f'Петино решение (финал):')
print(n)


print()


# Функция ввода целого числа >= 0,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and int(arg) >= 0:
            arg = int(arg)
            flag = False
        if flag:
            print('Не удалось распознать число')
    return arg


max_number = 0
flag = True
while flag:
    number = inputCheck('Введите число (0 — конец последовательности): ')
    if number == 0:
        flag = False
    if max_number < number:
        max_number = number
print(f'Максимальное число во введенной последовательности: {max_number}')
