alphabet = [ 'а', 'б', 'в', 'г', 'д', 'е',
             'ж', 'з', 'и', 'й', 'к', 'л',
             'м', 'н', 'о', 'п', 'р', 'с',
             'т', 'у', 'ф', 'х', 'ц', 'ч',
             'ш', 'щ', 'ъ', 'ы', 'ь', 'э', ]

strAlphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def switchCase(unit):
   
    if unit == '1':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):
            print('Введите текст')
            encodeATBASH(input())
        else:
            print('Введите шифртекст')
            encodeATBASH(input())
    if unit == '2':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):
            print('Введите текст')
            text = input()
            print('Введите сдвиг')
            shift = int(input())
            encodeCesar(text, shift)
        else:
            print('Введите шифртекст')
            text = input()
            print('Введите сдвиг')
            shift = int(input())
            decodeCesar(text, shift)
    if unit == '3':
        print('Выберите действие:\n')
        print('1.Шифровать\n2.Расшифровать')
        choice = input()
        if (choice == '1'):
            print('Введите текст')
            encodePolybius(input())
        else:
            print('Введите шифртекст')
            decodePolybius(input())


def encodeATBASH(text):
    res = ''
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += strAlphabet[len(strAlphabet) - strAlphabet.index(i) - 1]
    print(res)
    return res

def encodeCesar(text, shift):
    res = ''
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += strAlphabet[(strAlphabet.index(i) + (shift % 32)) % 32]
    print(res)
    return res

def decodeCesar(text, shift):
    res = ''
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += strAlphabet[(strAlphabet.index(i) - (shift % 32)) % 32]
    print(res)
    return res

def encodePolybius(text):
    res = ''
    for i in text:
        # res += polybiusAlpha[strAlphabet.index(i) // 6 ][strAlphabet.index(i) % 6]
        if (i == ' '):
            continue
        res += str(strAlphabet.index(i) // 6 + 1)
        res += str(strAlphabet.index(i) % 6 + 1)
        res += ' '
    print(res)
    return res
    

def decodePolybius(text):
    if len(text)%2!=0:
        return ("\nДля данного шифра используются двузначные числа. Поэтому длина шифртекста должна быть чётной!")

    polybiusAlpha = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                 ['Ж', 'З', 'И', 'Й', 'К', 'Л'],
                 ['М', 'Н', 'О', 'П', 'Р', 'С'],
                 ['Т', 'У', 'Ф', 'Х', 'Ц', 'Ч'],
                 ['Ш', 'щ', 'Ъ', 'Ы', 'Ь', 'Э'],
                 ['Ю', 'Я', '-', '-', '-', '-']]
    res = ''
    bigrams = text.split(' ')
    for i in bigrams:
        if (i == ' '):
            res += ' '
            continue
        res += polybiusAlpha[int(i[0]) - 1][int(i[1]) - 1]
        res += ' '
    print(res)
    return res

if __name__ == '__main__':
    print('Выберите шифр \n')
    print('1. АТБАШ\n2. Шифр Цезаря\n3. Квадрат Полибия\n')
    switchCase(input())



