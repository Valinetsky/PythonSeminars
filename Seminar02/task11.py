# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n) = A. Если А не
# является числом Фибоначчи, выведите число - 1.
# Input: 5
# Output: 6


# Функция ввода целого неотрицательного числа,
# с аргументом текстового приглашения
def inputCheck(message):
    flag = True
    while flag:
        arg = input(message)
        if arg.isdigit() and int(arg) > 1:
            arg = int(arg)
            flag = False
        if flag:
            print('Failed to recognize the number')
    return arg


# Функция генерации следующего числа Фибоначчи
def fibo(number):
    start = 1
    next = 1
    counter = 4

    while True:
        current = start + next
        if current == number:
            return counter
        if current > number:
            return -1

        start = next
        next = current
        counter += 1


number = inputCheck('Введите число: ')

result = fibo(number)

if result != -1:
    print(f'Число {number} в последовательности Фибоначчи на позиции {result}')

if result == -1:
    print(f'Число {number} не является членом последовательности Фибоначчи')


n = int(input('Введите число: '))

count = 1
factorial = 1
while count <= n:
    factorial *= count
    count += 1

print(factorial)
def fibo(number):
    start = 1
    next = 1
    counter = 4

    while True:
        current = start + next
        if current == number:
            return counter
        if current > number:
            return -1

        start = next
        next = current
        counter += 1


n = int(input('Введите число: '))

print(fibo(n))


# n = int(input('Введите число: '))

# count = 0
# number = 3
# result = 0
# while result < n:
#     count +=1
#     result = number ** count

# print(count)
# a = 4
# b = 8
# c = 2

# sum = 0
# count1 = 0
# while sum <= a:
#     sum += c
#     if sum <= a:
#         count1 += 1
#     else: break

# print(count1)

# count2 = 0
# sum = 0
# while sum <= b:
#     sum += c
#     if sum <= b:
#         count2 += 1
#     else: break
# print(count2)

# counter = 0
# while count1 > 0:
#     while count2 > 0:
#         counter += 1
#         count2 -= 1
#     count1 -= 1

# print(counter)