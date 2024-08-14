import numpy as np
'старого воробья на мякине не проведешь тчк'
def encode_vert_permutation(text, key):
    cols = len(key)
    text = text.replace(' ', '/')
    rows = len(text) // cols if len(text) % cols == 0 else len(text) // cols + 1
    matrA = []
    res = []
    while len(text) < cols*rows:
        text += '%'
    for i in range(rows):
        str_slice = text[i*cols:i*cols + cols]
        if i % 2 == 1:
            str_slice = str_slice[::-1]
        matrA.append(list(str_slice))
        res.append([])
        for j in range(cols):
            res[i].append('')
    key_list = sorted(list(key))

    for i in key:
        col_start = key.find(i)
        col_end = 0
        for j, item in enumerate(key_list):
            if item == i:
                col_end = j
        for j in range(rows):
            res[j][col_end] = matrA[j][col_start]

    for i in matrA:
        print(i)

    for i in res:
        print(i)

    res_str = ''
    for i in range(cols):
        for j in range(rows):
            res_str += res[j][i] + ' '

   
    # for i in res:
    #     res_str += ' '.join(i) + ' '

    file = open('D:/aucheba/python/crypto2/decode.txt',
                     'w', encoding='UTF-8')
    file.write(res_str)

    return res_str

def decode_vert_permutation(text, key):
    cols = len(key)
    text = text.replace(' ', '')
    rows = len(text) // cols if len(text) % cols == 0 else len(text) // cols + 1
    matrA = []
    res = []

    for i in range(rows):
        matrA.append([])
        res.append([])
        for j in range(cols):
            matrA[i].append('')
            res[i].append('')
    
    for i in range(cols):
        for j in range(rows):
            matrA[j][i] = text[i * rows + j]

    for i in matrA:
        print(i)

    key_list = sorted(list(key))
    for i, item in enumerate(key_list):
         col_start = i
         col_end = key.find(item)
         for j in range(rows):
             res[j][col_end] = matrA[j][col_start]

    res_str = ''
    for i in range(rows):
        if i % 2 == 1:
            res_str += ''.join(res[i])[::-1]
        else: 
            res_str += ''.join(res[i])
    # for i in range(rows):
    #     str_slice = text[i*cols:i*cols + cols]
    #     matrA.append(list(str_slice))
    #     res.append([])
    #     for j in range(cols):
    #         res[i].append('')
        
    res_str = res_str.replace('/', ' ')
    return res_str.replace('%', '')



def encode_Cardano(text):
    print('Введите ключ-решетку\n')
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    # создание отражений ключ-решетки
    for i in range(6):
        f1.append(input())
        f2.append('')
        f3.append('')
        f4.append('')

    for i in range(6):
        f2[i] = f1[i][::-1]
        f4[i] = f1[5 - i]
    
    for i in range(6):
        f3[i] = f2[5 - i]

    for i in range(6):
        f1[i] = list(f1[i])
        f2[i] = list(f2[i])
        f3[i] = list(f3[i])
        f4[i] = list(f4[i])

    # заполнение таблицы в соответствии с решетками
    text = text.replace(' ', '')
    while len(text) < 60:
        text += 'a'
    # print(text, len(text))
    res = []
    for i in range(6):
        res.append([])
        for j in range(10):
            res[i].append(' ')
    counter = 0
    for i in range(6):
        for j in range(10):
            if f1[i][j] == '*':
                res[i][j] = text[counter]
                counter += 1 
    
    for i in range(6):
        for j in range(10):
            if f2[i][j] == '*':
                res[i][j] = text[counter]
                counter += 1
   
    for i in range(6):
        for j in range(10):
            if f3[i][j] == '*':
                res[i][j] = text[counter]
                counter += 1 
   
    for i in range(6):
        for j in range(10):
            if f4[i][j] == '*':
                res[i][j] = text[counter]
                counter += 1 
    res_str = ''
    for i in res:
        print(i)
        res_str += ''.join(i)

    file = open('D:/aucheba/python/crypto2/decode.txt',
                     'w', encoding='UTF-8')
    file.write(res_str)
    return res_str

def decode_Cardano(text):
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    print('Введите ключ-решетку\n')
    for i in range(6):
        f1.append(input())
        f2.append('')
        f3.append('')
        f4.append('')

    for i in range(6):
        f2[i] = f1[i][::-1]
        f4[i] = f1[5 - i]
    
    for i in range(6):
        f3[i] = f2[5 - i]

    for i in range(6):
        f1[i] = list(f1[i])
        f2[i] = list(f2[i])
        f3[i] = list(f3[i])
        f4[i] = list(f4[i])
    res = []
    for i in range(6):
        res.append([])
        for j in range(10):
            res[i].append(text[i*10 + j])
    counter = 0
    res_str = ''
    for i in range(6):
        for j in range(10):
            if f1[i][j] == '*':
                res_str += res[i][j]
    for i in range(6):
        for j in range(10):
            if f2[i][j] == '*':
                res_str += res[i][j]
    for i in range(6):
        for j in range(10):
            if f3[i][j] == '*':
                res_str += res[i][j] 
    for i in range(6):
        for j in range(10):
            if f4[i][j] == '*':
                res_str += res[i][j]

    return res_str[:res_str.find('тчк') + 3]


if __name__ == '__main__':
    f = open('D:/aucheba/python/crypto2/proverb.txt', 'r', encoding='UTF-8')
    df = open('D:/aucheba/python/crypto2/decode.txt', 'r', encoding='UTF-8')
    print('Шифрование вертикальной перестановкой\n', encode_vert_permutation(f.read(), input('key\n')))
    print('Расшифрование вертикальной перестановкой\n',decode_vert_permutation(df.read(), input('key\n')))
    'шифр решетка является частным случаем шифра маршрутной перестановки'
    # print('Шифрование решеткой Кардано\n', encode_Cardano(f.read()))
    # print('Расшифрование решеткой Кардано\n', decode_Cardano(df.read()))
    f.close()