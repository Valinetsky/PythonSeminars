# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# ------------------------------------------

# Задача No49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


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


# Функция создания нового контакта
def newcontact(filename):
    lastname = input_name('Введите фамилию: ')
    firstname = input_name('Введите имя: ')
    patronymic = input_name('Введите отчество: ')

    phoneNum = inputCheck('введите номер телефона: ')

    contactDetails = ("[" + lastname + " " + firstname +
                      " " + patronymic + ", " + str(phoneNum) + "]\n")

    myfile = open(filename, "a")
    myfile.write(contactDetails)
    print('Новая запись:\n ' + contactDetails +
          '\nдобавлена в телефонную книгу!')


# Функция вводв имени
def input_name(message):
    name = input(message)
    remfname = name[1:]
    firstchar = name[0]
    return firstchar.upper() + remfname


# Функция поиска записи
def searchcontact(filename):
    searchname = input(
        "Введите первые буквы фамилии, имени или отчества, \nили начальные цифры телефона для ПОИСКА: ")
    remname = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + remname
    myfile = open(filename, "r+")
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print('Найдена запись:', end=' ')
            print(line)
            found = True
            break
    if found == False:
        print('Такой записи в телефонной книге не обнаружено: ', searchname)


# Функция вывода сообщения и запроса номера (например, пункта меню)
def messageMinMax(message, min, max):
    while True:
        operation = int(inputCheck(message))
        if operation in range(min, max + 1):
            return operation


# Функция редактирования контакта
def editcontact(filename, line):
    message = 'Хотите отредактировать запись?\n1 - режим редактирования\n2 - возврат в главное меню'
    number = messageMinMax(message, 1, 2)
    if number == 2:
        return

    message = 'Поле для редактирования:\n1 - фамилия\n2 - имя\n3 - отчество\n4 - номер телефона'
    number = messageMinMax(message, 1, 4)
