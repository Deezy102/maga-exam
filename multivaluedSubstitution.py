# strAlphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»— -'

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
def switch_case(unit):
    encode_file = open('D:/aucheba/python/crypto2/proverb.txt', 'r', encoding='UTF-8')
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
    if unit == '4':
        block_file = open('D:/aucheba/python/crypto2/block.txt', 'r', encoding='UTF-8')
        s_block_magma(block_file.read())

def encode_Tritemius(text):
    text = text.lower()
    res = ''
    counter = 1
    for i in text:
        if (i == ' '):
            res += ' '
            continue
        res += alphabet[(alphabet.find(i) + counter - 1) % 32]
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
        res += alphabet[(alphabet.find(i) - counter + 1) % 32]
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
        res += alphabet[(alphabet.find(i) + (alphabet.find(key[counter % len(key)]))) % 32] 
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
        res += alphabet[(alphabet.find(i) - (alphabet.find(key[counter % len(key)]))) % 32] 
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
            res += alphabet[(alphabet.find(text[i]) + alphabet.find(key)) % 32]
        else:
            if text[i - 1] == ' ':
                res += alphabet[(alphabet.find(text[i]) + alphabet.find(text[i-2])) % 32]
            else:
                res += alphabet[(alphabet.find(text[i]) + alphabet.find(text[i-1])) % 32]
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
            res += alphabet[(alphabet.find(text[i]) - alphabet.find(key)) % 32]
        else:
            if text[i - 1] == ' ':
                res += alphabet[(alphabet.find(text[i]) - alphabet.find(res[i-2])) % 32]
            else:
                res += alphabet[(alphabet.find(text[i]) - alphabet.find(res[i-1])) % 32]
    print(res)
    return res

s_blocks = [
    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
    [12,8,2,1,13,4,15,6,7,0,10,5,3,14,9,11],
    [7,15,5,10,8,1,6,13,0,9,3,14,11,4,2,12],
    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]
]

def s_block_magma(block):
    block = block.replace(',', ' ')
    print(block)
    block = block.split()
    for i in range(len(block)):
        block[i] = block[i].strip()
    for i in range(len(block)):
        block[i] = str(s_blocks[i // 4][int(block[i])])
    for i in range(11):
        block.append(block[0])
        block.pop(0)
    for i in range(len(block)):
        if (block[i] == '10'):
            block[i] = 'a'
        if block[i] == '11':
            block[i] = 'b'
        if block[i] == '12':
            block[i] = 'c'
        if block[i] == '13':
            block[i] = 'd'
        if block[i] == '14':
            block[i] = 'e'
        if block[i] == '15':
            block[i] = 'f'

    block = ''.join(block)
    print(block)
    return block




if __name__ == '__main__':
    print('Выберите шифр\n')
    switch_case(input('1. Шифр Тритемия\n2. Шифр Белазо\n3. Шифр Виженера\n4. S-block Magma\n'))
