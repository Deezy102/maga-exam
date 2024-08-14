import numpy as np


def cvalue(d, value):
    if value in d:
        return d[value]
    else:
        return f"{value} нет в словаре."
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


# def c1(x):
#     t = x+0x01010101
#     if t < 2**32:
#         return t
#     else:
#         return t-2**32


# def c2(x):
#     t = x+0x01010104
#     if t < 2**32:
#         return t
#     else:
#         return (t-2**32)+1


s = [
    ["C", "4", "6", "2", "A", "5", "B", "9",
        "E", "8", "D", "7", "0", "3", "F", "1"],
    ["6", "8", "2", "3", "9", "A", "5", "C",
        "1", "E", "4", "7", "B", "D", "0", "F"],
    ["B", "3", "5", "8", "2", "F", "A", "D",
        "E", "1", "7", "4", "C", "9", "6", "0"],
    ["C", "8", "2", "1", "D", "4", "F", "6",
        "7", "0", "A", "5", "3", "E", "9", "B"],
    ["7", "F", "5", "A", "8", "1", "6", "D",
        "0", "9", "3", "E", "B", "4", "2", "C"],
    ["5", "D", "F", "6", "9", "2", "C", "A",
        "B", "7", "8", "1", "4", "3", "E", "0"],
    ["8", "E", "2", "5", "6", "9", "1", "C",
        "F", "4", "B", "0", "D", "A", "3", "7"],
    ["1", "7", "E", "D", "0", "5", "8", "3",
        "4", "F", "A", "6", "9", "C", "B", "2"]
]


def fx(a, x):
    k = (a+x) % (2 ** 32)
    xx = '{0:08x}'.format(k)
    tomb = []
    for i, c0 in enumerate(xx[::-1]):
        c1 = s[i][int(c0, 16)]
        tomb.append(c1)
    b32 = '{0:032b}'.format(int("".join(tomb[::-1]), 16))
    b32_rot = b32[11:32]+b32[0:11]
    i32 = int(b32_rot, 2)
    return i32


def step(a0, b0, x):
    a1 = b0
    b1 = a0 ^ fx(b0, x)
    return (a1, b1)


def g_mix(text, secret):
    if type(text) != str:
        return ("Текст должен быть строкой.")
        exit()
    if type(secret) != str:
        return ("Ключ должен быть строкой.")
        exit()
    if len(text) != 16:
        return ("Длина блока текста должна быть 64 бита.")
        exit()
    if len(secret) != 64:
        return ("Длина ключа должна быть 256 бит.")
        exit()
    (ax, bx) = [text[i:i+8] for i in range(0, len(text), 8)]
    a = int(ax, 16)
    b = int(bx, 16)

    kx = [secret[i:i+8] for i in range(0, len(secret), 8)]
    k = [int(p, 16) for p in kx]
    x = []
    for i in range(3):
        for j in range(len(k)):
            x.append(k[j])
    for j in range(len(k)):
        x.append(k[len(k)-j-1])
    ai = a
    bi = b
    for i in range(32):
        (ai, bi) = step(ai, bi, x[i])
    return '{0:08x}'.format(bi)+'{0:08x}'.format(ai)


def g_unmix(text, secret):
    if type(text) != str:
        return ("Текст должен быть строкой.")
        exit()
    if type(secret) != str:
        return ("Ключ должен быть строкой.")
        exit()
    if len(text) != 16:
        return ("Длина блока текста должна быть 64 бита.")
        exit()
    if len(secret) != 64:
        return ("Длина ключа должна быть 256 бит.")
        exit()
    (ax, bx) = [text[i:i+8] for i in range(0, len(text), 8)]
    a = int(ax, 16)
    b = int(bx, 16)
    kx = [secret[i:i+8] for i in range(0, len(secret), 8)]
    k = [int(p, 16) for p in kx]
    x = []
    for i in range(1):
        for j in range(len(k)):
            x.append(k[j])
    for i in range(3):
        for j in range(len(k)):
            x.append(k[len(k)-j-1])
    ai = a
    bi = b
    for i in range(32):
        (ai, bi) = step(ai, bi, x[i])
    return '{0:08x}'.format(bi)+'{0:08x}'.format(ai)


def g_gamma(iv, secret, steps):
    if type(iv) != str:
        return ("IV должен быть строкой.")
        exit()
    if type(secret) != str:
        return ("Ключ должен быть строкой.")
        exit()
    if len(iv) != 16:
        return ("Длина IV должна быть 64 бита.")
        exit()
    if len(secret) != 64:
        return ("Длина ключа должна быть 256 бит.")
        exit()

    (n4x, n3x) = [iv[i:i+8] for i in range(0, len(iv), 8)]
    n3 = 0
    n4 = int(n4x, 16)
    gamma = []
    ivn = '{0:08x}'.format(n4)+'{0:08x}'.format(n3)
    gamma.append(g_mix(ivn, secret))
    for i in range(steps-1):
        n3 = (n3+1) % (2**32)
        ivn = '{0:08x}'.format(n4)+'{0:08x}'.format(n3)
        gamma.append(g_mix(ivn, secret))
    return gamma


def g_ctr(gamma, blocks):
    ctr = []
    if len(gamma) != len(blocks):
        return ("Ошибка! Разные количества блоков текста и гаммы.")
        exit()
    for i, g in enumerate(gamma):
        b = blocks[i]
        ctr.append('{0:016x}'.format(int(g, 16) ^ int(b, 16)))
    return ctr


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


dic = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33, 'А': 34, 'Б': 35, 'В': 36, 'Г': 37, 'Д': 38, 'Е': 39, 'Ё': 40, 'Ж': 41, 'З': 42, 'И': 43, 'Й': 44, 'К': 45, 'Л': 46, 'М': 47, 'Н': 48, 'О': 49, 'П': 50,
       'Р': 51, 'С': 52, 'Т': 53, 'У': 54, 'Ф': 55, 'Х': 56, 'Ц': 57, 'Ч': 58, 'Ш': 59, 'Щ': 60, 'Ъ': 61, 'Ы': 62, 'Ь': 63, 'Э': 64, 'Ю': 65, 'Я': 66, '.': 67, ',': 68, '–': 69, '-': 70, '"': 71, '«': 72, '»': 73, '+': 74, '=': 75, ';': 76, '#': 77, '№': 78, '%': 79, ':': 80, '(': 81, ')': 82, '*': 83, '\\': 84, '/': 85, '|': 86, '0': 87, '1': 88, '2': 89, '3': 90, '4': 91, '5': 92, '6': 93, '7': 94, '8': 95, '9': 96, '!': 97, '?': 98, ' ': 99}
idic = upsidedown(dic)


def encryptmessage(orig, keykey):
    orighex = ''
    if orig == '92def06b3c130a59':
        orighex = orig
    else:
        orighex = hexv(orig)
    # keyhex = hexv(keykey)
    print('\nОткрытый текст: ', orig)
    (arrayhex, l) = padding(orighex)
    simp = ""
    for i in range(len(arrayhex)):
        g = g_mix(arrayhex[i], keykey)
        simp += g
    print("\nЗашифрованный текст: ", "".join(simp))

    return "".join(simp)


def decryptmessage(orig, keykey):
    # keyhex = hexv(keykey)
    print('\nОткрытый текст:', orig)
    (arrayhex, l) = padding(orig)
    simp = ""
    for i in range(len(arrayhex)):
        g = g_unmix(arrayhex[i], keykey)
        simp += g
    simp = hexup(simp)
    print("\nРасшифрованный текст: ", "".join(simp))

    return "".join(simp)


if __name__ == "__main__":
	decryptmessage(encryptmessage('Вот пример статьи на 1000 символов. Это достаточно маленький текст, оптимально подходящий для карточек товаров в интернет-магазинах или для небольших информационных публикаций. В таком тексте редко бывает более 2-3 абзацев и обычно один подзаголовок. Но можно и без него. На 1000 символов рекомендовано использовать 1-2 ключа и одну картину.Текст на 1000 символов – это сколько примерно слов? Статистика показывает, что тысяча включает в себя 150-200 слов средней величины. Но, если злоупотреблять предлогами, союзами и другими частями речи на 1-2 символа, то количество слов неизменно возрастает.В копирайтерской деятельности принято считать тысячи с пробелами или без. Учет пробелов увеличивает объем текста примерно на 100-200 символов – именно столько раз мы разделяем слова свободным пространством. Считать пробелы заказчики не любят, так как это пустое место. Однако некоторые фирмы и биржи видят справедливым ставить стоимость за 1000 символов с пробелами, считая последние важным элементом качественного восприятия. Согласитесь, читать слитный текст без единого пропуска, никто не будет. Но большинству нужна цена за 1000 знаков без пробелов.', "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"), "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")