import numpy as np

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«»— -'
alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя;,.!«» -?'
def switch_case(unit):
    file =  open('D:/aucheba/python/crypto2/text.txt', 'r', encoding='UTF-8')
    decode_file = open('D:/aucheba/python/crypto2/decode.txt', 'r', encoding='UTF-8')

    if unit == '1':
        print('1. Encode\n2. Decode\n')
        if input() == '1':
            encode_matrix_cipher(input('Ключ-матрица\n'), file.read())
        else:
            decode_matrix_cipher(input('Ключ-матрица\n'), decode_file.read())
    if unit == '2':
        print('1. Encode\n2. Decode\n')
        if input() == '1':
            encode_Playfair_cipher(input('Введите ключ\n'), file.read(), 'encode')
        else:
            encode_Playfair_cipher(input('Введите ключ\n'), decode_file.read(), 'decode')


def encode_matrix_cipher(key, text):
    matrix = []
    row = []
    for i in key.split():
        row.append(int(i))
        if len(row) == 3:
            matrix.append(row)
            row = []
    key_matrix = np.array(matrix, dtype=int)
    text = text.lower()
    text = text.replace(' ', '')
    while(len(text) % 3 != 0):
        text += 'а'
    res = []
    vect = []
    
    # s = ''
    # for i in text:
    #     s += str(alphabet.find(i) + 1) + ' '
    # print(s)

    for i in text:
        vect.append(int(alphabet.find(i)) + 1)
        if len(vect) == 3:
            vect = np.array([[vect[0]], [vect[1]], [vect[2]]])
            sub_res = key_matrix.dot(vect)
            vect = []
            for i in sub_res:
                res.append(str(i[0]))
            vect = []
    res = ' '.join(res)
    print(res)
    # f = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # f.write(res)
    return res

def decode_matrix_cipher(key, text):
    matrix = []
    row = []
    for i in key.split():
        row.append(int(i))
        if len(row) == 3:
            matrix.append(row)
            row = []
    key_matrix = np.array(matrix)
    
    inv_matrix = np.linalg.inv(key_matrix)
    print(inv_matrix)
    text = text.split()
    for i in range(len(text)):
        text[i] = int(text[i])
        
    while(len(text) % 3 != 0):
        text.append(int('0'))
    
    res = []
    vect = []


    for i in text:
        vect.append(i)
        if len(vect) == 3:
            vect = np.array([[vect[0]], [vect[1]], [vect[2]]])
            sub_res = inv_matrix.dot(vect)
            # print(vect, sub_res)
            vect = []
            
            for i in sub_res:
                # print(int(round(i[0])-1))
                res.append(alphabet[int(round(i[0])-1)])
    res = ' '.join(res)
    print(res)
    return res








cipher_table = [
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', ''],
        [ '', '', '', '', '', '']
    ]

def encode_Playfair_cipher(key, text, action):
    key_list = []
    for i in key:
        key_list.append(i)
    key_set = set(key_list)
    # проверка ключа на повтор букв
    if len(key_list) != len(key_set):
        return 'Неверный ключ'
    
    
    temp = []
    for i in alph:
        temp.append(i)

    for i in key_set:
        temp.remove(i)
    print('temp ===',temp)
    key_list.extend(temp)
    print('key_list', key_list)
    for i in range(7):
        for j in range(6):
            cipher_table[i][j] = key_list.pop(0)
    print(cipher_table[0], '\n',
        cipher_table[1], '\n',
        cipher_table[2], '\n',
        cipher_table[3], '\n',
        cipher_table[4], '\n',
        cipher_table[5], '\n',
        cipher_table[6], '\n',
        )
    
    text = text.lower()
    # text = text.replace(' ', '')
    
    # # проверка на одинаковую биграмму и вставка ф между ними
    # for i in range(len(text)):
    #     if i == 0: continue
    #     if text[i] == text[i-1]:
    #         text = text.replace(f'{text[i]}{text[i-1]}', f'{text[i]}ф{text[i-1]}')
    if action != 'encode':
        text = text.replace(' ', '')
    if len(text) % 2 != 0:
        text +='ф'
    
    text_list = []
    for i in text:
        text_list.append(i)
    
    x0, y0, x1, y1 = 0,0,0,0
    res = ''

    for i in range(0, len(text_list), 2):
        coords = find_coords(text_list[i], text_list[i+1])
        x0, y0, x1, y1 = coords[0], coords[1], coords[2], coords[3]
        if x0 == x1:
            if action == 'encode':
                y0 = (y0 + 1) % 6
                y1 = (y1 + 1) % 6
            else:
                y0 = (y0 - 1) % 6
                y1 = (y1 - 1) % 6
        elif y0 == y1:
            if action == 'encode':
                x0 = (x0 + 1) % 7
                x1 = (x1 + 1) % 7
            else:
                x0 = (x0 - 1) % 7
                x1 = (x1 - 1) % 7
        else:
            y0, y1 = y1, y0

        res += cipher_table[x0][y0] + cipher_table[x1][y1] + ' '

    print(res)
    # f = open('D:/aucheba/python/crypto2/decode.txt',
    #                  'w', encoding='UTF-8')
    # f.write(res)
    return res

        
def find_coords(first, second):
    res = [0, 0, 0, 0]
    for i in range(7):
        for j in range(6):
            if first == cipher_table[i][j]: 
                res[0] = i 
                res[1] = j
            if second == cipher_table[i][j]: 
                res[2] = i 
                res[3] = j
    # print('check', first, res[0], res[1])
    return res

if __name__ == '__main__':
    print('Выберите шифр:\n1. Матричный шифр\n2. Шифр Плейфера\n')
    switch_case(input())


