# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


winnie_string = 'пара-ра-рам рам-пам-папам па-ра-па-да'


# Функция пробега по фразе, с подсчетом гласных в словах
def param_param(winnie_string):

    # Функция подсчета гласных в слове
    def symbol_count(word):
        return sum(1 for i in word if i in 'аеёиоуыэюя')

    local_string = winnie_string.lower().split()
    first_word = symbol_count(local_string[0])

    if all([symbol_count(element) == first_word for element in local_string]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(param_param(winnie_string))
