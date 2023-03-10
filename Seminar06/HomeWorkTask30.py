# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# ПРОСТОЙ СПОСОБ ----------------------------------
# a = 7
# d = 2
# n = 10

# array = []

# for i in range(n):
#     array.append(a + i * d)

# print(array)
# -------------------------------------------------



# СЛОЖНЫЙ СПОСОБ С РЕКУРСИВНЫМ ВЫЧИСЛЕНИЕМ СЛЕДУЮЩЕГО ЭЛЕМЕНТА
# Видимо, я перепутал темы семинаров. Но тоже работает.

# Функция рекурсивного вычисления элемента арифметической прогрессии 
def progression(a, d, n):
    if n == 1:
        return a
    else:
        return progression(a + d, d, n - 1)
    

a = 7
d = 2
n = 10

array = []

for i in range(1, n + 1):
    array.append(progression(a, d, i))

print(array)