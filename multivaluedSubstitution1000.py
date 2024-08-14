# strAlphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»— -'
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»-'
# alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
def switch_case(unit):
    encode_file = open('D:/aucheba/python/crypto2/text.txt', 'r', encoding='UTF-8')
    decode_file = open('D:/aucheba/python/crypto2/decode.txt', 'r', encoding='UTF-8')
    if unit == '1':
        choice = input('Выберите действие\n1. Шифровать\n2. Расшифровать\n')
        if choice == '1':
            encode_Tritemius(encode_file.read())
        else:
            decode_Tritemius(decode_file.read())
    if unit == '2':
        choice = input('Выберите действие\n1. Шифровать\n2. Расшифровать\n')
        if choice == '1':
            encode_Belaso(encode_file.read(), input('Введите ключ\n'))
        else:
            decode_Belaso(decode_file.read(), input('Введите ключ\n'))
    if unit == '3':
        choice = input('Выберите действие\n1. Шифровать\n2. Расшифровать\n')
        if choice == '1':
            encode_Vigenere(encode_file.read(), input('Введите ключ\n'))
        else:
            decode_Vigenere(decode_file.read(), input('Введите ключ\n'))
   
def encode_Tritemius(text):
    text = text.lower()
    res = ''
    counter = 1
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += alphabet[(alphabet.find(i) + counter - 1) % len(alphabet)]
        counter += 1
    print(res)
    # file = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # file.write(res)
    return res
    
def decode_Tritemius(text):
    text = text.lower()
    res = ''
    counter = 1
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += alphabet[(alphabet.find(i) - counter + 1) % len(alphabet)]
        counter += 1
    print(res)
    return res

def encode_Belaso(text, key):
    text = text.lower()
    key = key.lower()
    res = ''
    counter = 0
    for i in text:
        if i == ' ':
            res += ' '
            continue
        res += alphabet[(alphabet.find(i) + (alphabet.find(key[counter % len(key)]))) % len(alphabet)] 
        counter += 1
    print(res)
    # file = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # file.write(res)
    return res

def decode_Belaso(text, key):
    text = text.lower()
    key = key.lower()
    res = ''
    counter = 0
    for i in text:
        if i == ' ':
            res += ' '
            continue
        res += alphabet[(alphabet.find(i) - (alphabet.find(key[counter % len(key)]))) % len(alphabet)] 
        counter += 1
    print(res)
    return res
    

def encode_Vigenere(text, key):
    text = text.lower()
    key = key.lower()
    res = ''
    for i in range(len(text)):
        if text[i] == ' ':
            res += ' '
            continue
        if i == 0:
            res += alphabet[(alphabet.find(text[i]) + alphabet.find(key)) % len(alphabet)]
        else:
            if text[i - 1] == ' ':
                res += alphabet[(alphabet.find(text[i]) + alphabet.find(text[i-2])) % len(alphabet)]
            else:
                res += alphabet[(alphabet.find(text[i]) + alphabet.find(text[i-1])) % len(alphabet)]
    print(res)
    # file = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # file.write(res)
    return res

def decode_Vigenere(text, key):
    text = text.lower()
    key = key.lower()
    res = ''
    for i in range(len(text)):
        if text[i] == ' ':
            res += ' '
            continue
        if i == 0:
            res += alphabet[(alphabet.find(text[i]) - alphabet.find(key)) % len(alphabet)]
        else:
            if text[i - 1] == ' ':
                res += alphabet[(alphabet.find(text[i]) - alphabet.find(res[i-2])) % len(alphabet)]
            else:
                res += alphabet[(alphabet.find(text[i]) - alphabet.find(res[i-1])) % len(alphabet)]
    print(res)
    return res

if __name__ == '__main__':
    print('Выберите шифр\n')
    switch_case(input('1. Шифр Тритемия\n2. Шифр Белазо\n3. Шифр Виженера\n'))
