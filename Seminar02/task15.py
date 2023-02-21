# Задача No15. 
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


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
            print('Failed to recognize the number')
    return arg

arrSize = inputCheck('Введите количество арбузов: ')

arrayTemp = []

for i in range(arrSize):
    number = inputCheck(f'Введите вес арбуза {i + 1}: ')
    arrayTemp.append(number)

arrayTemp.sort()

print()
print(f'Сортированный по возрастанию массив арбузов: {arrayTemp}')
print()
print(f'Самый легкий арбуз весит: {arrayTemp[0]}')
print()
print(f'Самый тяжелый арбуз весит: {arrayTemp[-1]}')
print()