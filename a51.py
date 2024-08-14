import numpy as np
import sys


def cvalue(d, value):
    if value in d:
        return d[value]
    else:
        return f"{value}, нет в словаре."
        exit()


def upsidedown(d):
    h = {}
    for k, v in d.items():
        h[v] = k
    return h


def hexv(text):
    return "".join(['{0:02x}'.format(cvalue(dic, k)) for k in text])


def hexup(hext):
    temx = [hext[i:i+2] for i in range(0, len(hext), 2)]
    return "".join([cvalue(idic, int(i, 16)) for i in temx])


def load(iv, secret):
    r1 = np.zeros(19, np.int32)
    r2 = np.zeros(22, np.int32)
    r3 = np.zeros(23, np.int32)
    for x in [*secret, *iv]:
        r1[0] = r1[0] ^ x
        r2[0] = r2[0] ^ x
        r3[0] = r3[0] ^ x
        r1 = np.roll(r1, 1)
        r2 = np.roll(r2, 1)
        r3 = np.roll(r3, 1)

    for x in range(100):
        majority = get_majority(r1[8], r2[10], r3[10])
        if r1[8] == majority:
            x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
            temp1 = np.roll(r1, 1)
            temp1[0] = x_bit
            r1 = temp1
        if r2[10] == majority:
            x_bit = r2[20] ^ r2[21]
            temp2 = np.roll(r2, 1)
            temp2[0] = x_bit
            r2 = temp2
        if r3[10] == majority:
            x_bit = r3[20] ^ r3[21] ^ r3[22] ^ r3[7]
            temp3 = np.roll(r3, 1)
            temp3[0] = x_bit
            r3 = temp3
    return(r1, r2, r3)


def apoload(iv, secret):
    r1 = np.zeros(19, np.int32)
    r2 = np.zeros(22, np.int32)
    r3 = np.zeros(23, np.int32)
    for x in [*secret, *iv]:
        r1[0] = r1[0] ^ x
        r2[0] = r2[0] ^ x
        r3[0] = r3[0] ^ x
        majority = get_majority(r1[8], r2[10], r3[10])
        if r1[8] == majority:
            x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
            temp1 = np.roll(r1, 1)
            temp1[0] = x_bit
            r1 = temp1
        if r2[10] == majority:
            x_bit = r2[20] ^ r2[21]
            temp2 = np.roll(r2, 1)
            temp2[0] = x_bit
            r2 = temp2
        if r3[10] == majority:
            x_bit = r3[20] ^ r3[21] ^ r3[22] ^ r3[7]
            temp3 = np.roll(r3, 1)
            temp3[0] = x_bit
            r3 = temp3
    for x in range(100):
        majority = get_majority(r1[8], r2[10], r3[10])
        if r1[8] == majority:
            x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
            temp1 = np.roll(r1, 1)
            temp1[0] = x_bit
            r1 = temp1
        if r2[10] == majority:
            x_bit = r2[20] ^ r2[21]
            temp2 = np.roll(r2, 1)
            temp2[0] = x_bit
            r2 = temp2
        if r3[10] == majority:
            x_bit = r3[20] ^ r3[21] ^ r3[22] ^ r3[7]
            temp3 = np.roll(r3, 1)
            temp3[0] = x_bit
            r3 = temp3
    return(r1, r2, r3)


def a_gamma(iv, secret, steps):
    if len(iv) != 22:
        return "Ошибка. Длина iv должна быть 22 бита."
        exit()
    if len(secret) != 64:
        return "Ошибка. Длина ключа должна быть 64 бит."
        exit()
    (r1, r2, r3) = load(iv, secret)
    gamma = []
    for x in range(steps):
        majority = get_majority(r1[8], r2[10], r3[10])
        if r1[8] == majority:
            x_bit = r1[18] ^ r1[17] ^ r1[16] ^ r1[13]
            temp1 = np.roll(r1, 1)
            temp1[0] = x_bit
            r1 = temp1
        if r2[10] == majority:
            x_bit = r2[20] ^ r2[21]
            temp2 = np.roll(r2, 1)
            temp2[0] = x_bit
            r2 = temp2
        if r3[10] == majority:
            x_bit = r3[20] ^ r3[21] ^ r3[22] ^ r3[7]
            temp3 = np.roll(r3, 1)
            temp3[0] = x_bit
            r3 = temp3
        output = r1[18] ^ r2[21] ^ r3[22]
        gamma.append(output)
    kg = "".join(['{0:d}'.format(i) for i in gamma])
    kx = [kg[i:i+64] for i in range(0, len(kg), 64)]
    pio = ['{0:016x}'.format(int(i, 2)) for i in kx]
    return pio


def get_majority(a, b, c):
    if a + b + c > 1:
        return 1
    else:
        return 0


def binv(hext):
    return [int(i, 2) for i in '{0:064b}'.format(int(hext, 16))]


def ivv(frame):
    x = (frame % (0x400000))
    return [int(i, 2) for i in '{0:022b}'.format(x)]


def xrand(n):
    x = ""
    if n % 2 != 0:
        n -= 1
        x += "0"
    for i in range(int(n/2)):
        x += '{0:02x}'.format(np.random.randint(1, 33))
    return x


def padding(hext):
    l = len(hext)
    freak = l % 16
    if freak > 0:
        hext += xrand(16-freak)
    return ([hext[i:i+16] for i in range(0, len(hext), 16)], l)


def g_ctr(gamma, blocks):
    ctr = []
    if len(gamma) != len(blocks):
        return "Ошибка! Разные количества блоков текста и гаммы."
        exit()
    for i, g in enumerate(gamma):
        b = blocks[i]
        ctr.append('{0:016x}'.format(int(g, 16) ^ int(b, 16)))
    return ctr


dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33, 'А': 34, 'Б': 35, 'В': 36, 'Г': 37, 'Д': 38, 'Е': 39, 'Ё': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44, 'К': 45, 'Л': 46, 'М': 47, 'Н': 48, 'О': 49, 'П': 50,
       'Р': 51, 'С': 52, 'Т': 53, 'У': 54, 'Ф': 55, 'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59, 'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63, 'Э': 64, 'Ю': 65, 'Я': 66, '.': 67, ',': 68, '–': 69, '-': 70, '"': 71, '«': 72, '»': 73, '+': 74, '=': 75, ';': 76, '#': 77, '№': 78, '%': 79, ':': 80, '(': 81, ')': 82, '*': 83, '\\': 84, '/': 85, '|': 86, '0': 87, '1': 88, '2': 89, '3': 90, '4': 91, '5': 92, '6': 93, '7': 94, '8': 95, '9': 96, '!': 97, '?': 98, ' ': 99, '—': 100}

idic = upsidedown(dic)


def encryptmessage(orig, keykey, iv):

    orighex = hexv(orig)
    keyhex = hexv(keykey)
    keybin = binv(keyhex)
    ivv2 = ivv(iv)
    (arrayhex, l) = padding(orighex)
    g = a_gamma(ivv2, keybin, len(arrayhex)*64)
    gctr = g_ctr(g, arrayhex)
    #print("\nЗашифрованный текст: ", "".join(gctr))

    return "".join(gctr)


def decryptmessage(orig, keykey, iv):
    keyhex = hexv(keykey)
    keybin = binv(keyhex)
    ivv2 = ivv(iv)
    (arrayhex, l) = padding(orig)
    g = a_gamma(ivv2, keybin, len(arrayhex)*64)
    gctr = g_ctr(g, arrayhex)
    up = hexup("".join(gctr))
    #print("\nРасшифрованный текст: ", up)

    return "".join(up)
