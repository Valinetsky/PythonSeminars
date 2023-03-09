# Задача №41.
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5
# 1 2 3 4 5

# 5
# 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

array = [1, 5, 1, 5, 1, 5, 1, 5, 1]
result = 0
for i in range(1, len(array) - 1):
    print(f'i={i}')
    if array[i - 1] < array[i] and array[i + 1] < array[i]:
        print(array[i], i)
        result += 1
print(result)