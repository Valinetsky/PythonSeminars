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

# 'r', 'w', 'a'

# import os


filename = 'phonebook.txt'
datafile = open(filename, 'a+')
datafile.close

# book_name = 'Bilbo'
# with open(filename, 'a+') as datafile:
#     datafile.write(book_name)
# with open(filename, 'a+') as datafile:
#     datafile.write(book_name)


def get_operation():
    message = '''
    Введите номер операции:
    1 - Вывести справочник на экран
    2 - Добавить запись
    3 - Найти запись
    4 - Выход
    '''

    while True:
        operation = int(input(message))
        if operation in range(1,5):
            return operation

# Функции вызова меню
def run_menu(number):
    if number == 1:
        menu_1()
    if number == 2:
        menu_2()
    if number == 3:
        menu_3()
    if number == 4:
        menu_4()
    
    if number < 1 or number > 4:
        print('Не бывает, но - ОШИБКА')
        return -1


# Функции меню
def menu_1():
    myfile = open(filename, "r+") 
    filecontents = myfile.read() 
    if len(filecontents) == 0: 
        print('Телефонная книга пока пуста') 
    else: 
        print(filecontents) 
    myfile.close
    return filecontents
 
def menu_2():
    newcontact()

def menu_3():
    searchcontact() 

def menu_4():
    print('Спасибо за использование программы. До свидания') 


# Функция создания нового контакта 
def newcontact(): 
    lastname = input_name('Введите фамилию: ') 
    firstname = input_name('Введите имя: ')
    patronymic = input_name('Введите отчество: ') 
    
    phoneNum = input('введите номер телефона: ') 
    
    contactDetails =("[" + lastname + " " + firstname + " " + patronymic + ", " + phoneNum +  "]\n")

    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print('Новая запись:\n ' + contactDetails + '\nдобавлена в телефонную книгу!')


# Функция вводв имени 
def input_name(message): 
    name = input(message)
    remfname = name[1:]
    firstchar = name[0]
    return firstchar.upper() + remfname


# Функция поиска записи        
def searchcontact(): 
    searchname = input("Введите фамилию для ПОИСКА: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print('Найдена запись:', end = ' ') 
            print(line) 
            found = True 
            break 
    if found == False: 
        print('Такой записи в телефонной книге не обнаружено: ', searchname) 



# Главный цикл
run_flag = True
while run_flag:
    menu_status = get_operation()
    if menu_status == 4:
        run_flag = False
    run_menu(menu_status)





