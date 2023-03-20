# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

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


# book_name = 'Bilbo'
# with open(filename, 'a+') as datafile:
#     datafile.write(book_name)
# with open(filename, 'a+') as datafile:
#     datafile.write(book_name)

from HomeWorkTask38user import *


# Функция получения номера пункта меню
def get_operation():
    message = '''
    Введите номер операции:
    1 - Вывести справочник на экран
    2 - Добавить запись
    3 - Найти запись (редактировать запись)
    4 - Выход
    '''

    result = messageMinMax(message, 1, 4)
    return result


# Функции вызова меню
def run_menu(number, filename):
    if number == 1:
        menu_1(filename)
    if number == 2:
        menu_2(filename)
    if number == 3:
        menu_3(filename)
    if number == 4:
        menu_4(filename)

    if number < 1 or number > 4:
        print('Не бывает, но - ОШИБКА')
        return -1


# Функции меню
def menu_1(filename):
    myfile = open(filename, "r+")
    filecontents = myfile.read()
    if len(filecontents) == 0:
        print('Телефонная книга пока пуста')
    else:
        print(filecontents)
    myfile.close
    return filecontents


def menu_2(filename):
    newcontact(filename)


def menu_3(filename):
    searchcontact(filename)


def menu_4(filename):
    print('Спасибо за использование программы. До свидания')
