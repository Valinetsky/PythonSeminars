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

# printing the heading of the program 
print( "WELCOME TO THE PHONEBOOK DIRECTORY") 
 
# creating a .txt file to store contact details 
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 
 
# defining main menu 
def main_menu(): 
    print( "\nMAIN MENU\n") 
    print( "1. Show all existing Contacts") 
    print( "2. Add a new Contact") 
    print( "3. Search the existing Contact") 
    print( "4. Exit") 
    choice = input("Enter your choice: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "There is no contact in the phonebook.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Press Enter to continue ...") 
        main_menu() 
    elif choice == "4": 
        print("Thank you for using Phonebook!") 
    else: 
        print( "Please provide a valid input!\n") 
        enter = input( "Press Enter to continue ...") 
        main_menu() 
 
# defining search function         
def searchcontact(): 
    searchname = input( "Enter First name for Searching contact record: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Your Required Contact Record is:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "The Searched Contact is not available in the Phone Book", searchname) 
 
# first name 
def input_firstname(): 
    first = input( "Enter your First Name: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# last name 
def input_lastname(): 
    last = input( "Enter your Last Name: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# storing the new contact details 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "Enter your Phone number: ") 
    emailID = input( "Enter your E-mail Address: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "The following Contact Details:\n " + contactDetails + "\nhas been stored successfully!") 
 
main_menu() 