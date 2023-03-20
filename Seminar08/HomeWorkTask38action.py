# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# ------------------------------------------



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

    contactDetails = (lastname + " " + firstname +
                      " " + patronymic + " " + str(phoneNum) + "\n")

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
            editcontact(filename, line)
            break
    if found == False:
        print('Такой записи в телефонной книге не обнаружено: ', searchname)


# Функция редактирования контакта
def editcontact(filename, line):
    message = 'Хотите отредактировать запись?\n1 - режим редактирования\n2 - возврат в главное меню\n'
    number = messageMinMax(message, 1, 2)
    if number == 2:
        return

    print('-------------------------------------')
    print(line)
    new_line = line.split()

    message = 'Поле для редактирования:\n1 - фамилия\n2 - имя\n3 - отчество\n4 - номер телефона\n\n5 - удалить строку\n'
    number = messageMinMax(message, 1, 5)
    if number < 5:
        if number == 1:
            change_element = input_name('Введите фамилию: ')
        if number == 2:
            change_element = input_name('Введите имя: ')
        if number == 3:
            change_element = input_name('Введите отчество: ')
        if number == 4:
            change_element = str(inputCheck('введите номер телефона: '))
        new_line[number - 1] = change_element
        new_line_str = (' ').join(new_line) + '\n'
    if number == 5:
        new_line_str = ''
        print(f'Строка {line}удалена')

    changeFile(filename, line, new_line_str)
    


# Функция вывода сообщения и запроса номера (например, пункта меню)
def messageMinMax(message, min, max):
    while True:
        operation = int(inputCheck(message))
        if operation in range(min, max + 1):
            return operation


# Функция замены строки в файле
def changeFile(filename, line, new_line_str):
    myfile = open(filename, 'rt')
    filecontents = myfile.read()
    filecontents = filecontents.replace(line, new_line_str) 
    myfile.close() 
    myfile = open(filename, 'wt') 
    myfile.write(filecontents) 
    myfile.close()
