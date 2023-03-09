# Задача №45.
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз(перестановка чисел новую
#                          пару не дает).
# Ввод: Вывод:
# 300 220 284

def frindsNumber(number):
    base = 1
    array = []
    while base <= number / 2:
        if number % base == 0:
            array.append(base)
        base += 1
    # print(f'{number}, делители: {array}, сумма: {sum(array)}')
    return sum(array)


# number = int(input())
count = 20000
unic_array = []
while count > 1:
    local_number = frindsNumber(count)
    second_number = frindsNumber(local_number)
    if second_number == count and count != local_number and (count not in unic_array) and (local_number not in unic_array) and (local_number < count):
        print(f'Пара дружественных чисел: {count}, {local_number}')
        print()
    unic_array.append(count)
    
    count -= 1
    
