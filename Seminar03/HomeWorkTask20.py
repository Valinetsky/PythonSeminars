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
    caseLetter01 = {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'}
    caseLetter02 = {'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'}
    caseLetter03 = {'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'}
    caseLetter04 = {'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'}
    caseLetter05 = {'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'}
    caseLetter08 = {'J', 'X', 'Ш', 'Э', 'Ю'}
    caseLetter10 = {'Q', 'Z', 'Ф', 'Щ', 'Ъ'}
    
    counter = 0

    localWord = word.upper()

    for letter in localWord:
        if letter in caseLetter01:
            counter += 1
        if letter in caseLetter02:
            counter += 2
        if letter in caseLetter03:
            counter += 3
        if letter in caseLetter04:
            counter += 4
        if letter in caseLetter05:
            counter += 5
        if letter in caseLetter08:
            counter += 8
        if letter in caseLetter10:
            counter += 10
    
    return counter



word = input('Введите слово: ')

langEn = symbolCheck(word, 'A', 'Z')
langRu = symbolCheck(word, 'А', 'Я')

if langCheck(word, langEn, langRu):
    print(f'Очков за слово {word}: {countScore(word)}')        