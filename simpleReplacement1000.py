strAlphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»— -'


def switchCase(unit):
    f = open('D:/aucheba/python/crypto2/text.txt', 'r', encoding='UTF-8')
    text = f.read()
    file = open('D:/aucheba/python/crypto2/decode.txt', 'r', encoding='UTF-8')
    text2 = file.read()
    if unit == '1':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):

            encodeATBASH(text)
        else:

            encodeATBASH(text2)
    if unit == '2':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):

            print('Введите сдвиг')
            shift = int(input())
            encodeCesar(text, shift)
        else:

            print('Введите сдвиг')
            shift = int(input())
            decodeCesar(text2, shift)
    if unit == '3':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):
            print('Введите текст')
            encodePolybius(text)
        else:
            print('Введите шифртекст')
            decodePolybius(text2)


def encodeATBASH(text):
    res = ''
    for i in text:
        res += strAlphabet[len(strAlphabet) - strAlphabet.find(i) - 1]
    print(res)
    return res


def encodeCesar(text, shift):
    res = ''
    for i in text:
        res += strAlphabet[(strAlphabet.find(i) + (shift % 74)) % 74]
    print(res)
    # fileCesar = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # fileCesar.write(res)
    return res

def decodeCesar(text, shift):
    res = ''
    for i in text:
        res += strAlphabet[(strAlphabet.find(i) - (shift % 74)) % 74]
    print(res)
    return res

def encodePolybius(text):
    res = ''
    for i in text:
        res += str(strAlphabet.index(i) // 9 + 1)
        res += str((strAlphabet.index(i) % 9) + 1)
        res += ' '
    print(res)
    # filePolybius = open('D:/aucheba/python/crypto2/decode.txt',
    #                     'w', encoding='UTF-8')
    # filePolybius.write(res)
    return res

def decodePolybius(text):
    # 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»— -'
    if len(text)%2!=0:
        return ("\nДля данного шифра используются двузначные числа. Поэтому длина шифртекста должна быть чётной!")
    polybiusAlpha = [['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З'],
                     ['И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р'],
                     ['С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ'],
                     ['Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в'],
                     ['г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к'],
                     ['л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у'],
                     ['ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
                     ['э', 'ю', 'я', ';', ',', '.', '!', '«', '»'],
                     ['—', ' ', '-', '-', '-', '-', '-', '-', '-']]
    res = ''
    bigrams = text.split(' ')
    for i in bigrams:
        if (i == '' or i == ' '):
            continue
        res += polybiusAlpha[int(i[0])-1][int(i[1])-1]
    print(res)
    return res

if __name__ == '__main__':
    print('Выберите шифр \n')
    print('1. АТБАШ\n2. Шифр Цезаря\n3. Квадрат Полибия\n')
    switchCase(input())
