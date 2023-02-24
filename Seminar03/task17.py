# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# Входящий список
list = [1, 1, 2, 0, -1, 3, 4, 4]
print("Input list: ", list)

# Пустой список для уникальных значений
uniqList = []

for i in list:
    if i not in uniqList:
        uniqList.append(i)

# Вывод
print("Массив уникальных элементов: ", uniqList)
print("количество уникальных элементов:", len(uniqList))
