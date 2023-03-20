# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# ------------------------------------------


from HomeWorkTask38action import *
from HomeWorkTask38menu import *

filename = 'phonebook.txt'
datafile = open(filename, 'a+')
datafile.close

# Главный цикл
run_flag = True
while run_flag:
    menu_status = get_operation()
    if menu_status == 4:
        run_flag = False
    run_menu(menu_status, filename)
