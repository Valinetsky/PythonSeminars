# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12


# Функция проверяющая, лежат ли все введенные символы внутри диапазона
def symbolCheck(text, start, end):
    if len(text) < 1:
        return False
    localText = text.upper()
    for letter in localText:
        if letter < start or letter > end:
            return False
    return True


# Функция проверяющая, соответствует ли слово одному из двух языков
def langCheck(word, langEn, langRu):
    if langEn == False and langRu == False:
        print('Введеная строка содержит небуквенные символы, или смесь букв из разных языков')
        return False
    if langEn:
        print('Слово на английском языке')
        return True
    print('Слово на русском языке')
    return True


# Функция, считающая суммарный вес слова
def countScore(word):

    # caseLetter01 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
    # caseLetter02 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
    # caseLetter03 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
    # caseLetter04 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
    # caseLetter05 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
    # caseLetter08 = {'J', 'X', 'Ш', 'Э', 'Ю'}
    # caseLetter10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}


    price = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 
             'T': 1, 'R': 1, 'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 
             'Р': 1, 'С': 1, 'Т': 1,
             'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 
             'Т': 1,

             'D': 2, 'G': 2, 
             'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,

             'B': 3, 'C': 3, 'M': 3, 'P': 3, 
             'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,

             'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 
             'Й': 4, 'Ы': 4,

             'K': 5, 
             'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,

             'J': 8, 'X': 8, 
             'Ш': 8, 'Э': 8, 'Ю': 8,

             'Q': 10, 'Z': 10, 
             'Ф': 10, 'Щ': 10, 'Ъ': 10
    }
    
    counter = 0

    localWord = word.upper()

    # for letter in localWord:
    #     if letter in caseLetter01:
    #         counter += 1
    #     if letter in caseLetter02:
    #         counter += 2
    #     if letter in caseLetter03:
    #         counter += 3
    #     if letter in caseLetter04:
    #         counter += 4
    #     if letter in caseLetter05:
    #         counter += 5
    #     if letter in caseLetter08:
    #         counter += 8
    #     if letter in caseLetter10:
    #         counter += 10
    
    # return counter

    for letter in localWord:
        counter += price[letter]
    
    return counter



word = input('Введите слово: ')

langEn = symbolCheck(word, 'A', 'Z')
langRu = symbolCheck(word, 'А', 'Я')

if langCheck(word, langEn, langRu):
    print(f'Очков за слово {word}: {countScore(word)}')        