import random
import math
import sys


def elgamal(p, g, x, isEncode, message_):
    #action = str(input('Действие (encode/decode): '))
    action = isEncode

    #message = input("Сообщение: ").upper()
    message = message_

    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя#,.!?:;{ }[]\'\"-—'

    # Вводим ключ P
    P = int(p)

    # Вводим ключ G
    G = int(g)
    if not G < P:  # Проверка параметра
        print("g >= p")
        return

    # Вводим ключ X
    X = int(x)
    if not (X > 1 and X < (P-1)):  # Проверка параметра
        print("x <= 1 or x >= p-1")
        return

    Y = G**X % P  # P,G,Y - открытые ключи, X - секретный ключ
    print("Открытый ключ Y: ", Y)

    F = P - 1  # Функция Эйлера от числа P
    array = []  # Массив чисел, взаимно простых с F
    for i in range(2, F):  # Заполнение массива
        Z = math.gcd(i, F)
        if Z == 1:
            array.append(i)
    print("Числа, взаимно простые с функцией Эйлера от числа P: ", array)


    array_k = []
    for i in range(3):
        Z = random.choice(array)
        if random.choice(array) not in array_k:
            array_k.append(Z)
        else:
            i = i - 1

    array_k = [3, 5, 7] #Мой массив рандомных k для пословицы
    #print("Массив рандомных k для пословицы: ", array_k)

    if action == "encode":  # Действия для зашифрования
        print("Случайные секретные числа k: ", array_k)
        result = ""
        for i in message:  # Зашифровка
            # Берём случайный k из массива случайных k
            Z = random.choice(array_k)
            a = (G ** Z) % P  # Вычисляем a
            b = ((Y ** Z) * (alphabet.index(i)+1)) % P  # Вычисляем b
            if len(str(a)) != 2:  # Если а - цифра, добавляем 0 вперёд
                a = '0'+str(a)
            if len(str(b)) != 2:  # Если b - цифра, добавляем 0 вперёд
                b = '0'+str(b)
            result += str(a)+str(b)  # Конкатенируем a и b в результат
        new_result = ""  # Далее идут действия для представления результата в виде пятёрок
        L = math.ceil(len(result) // 5)
        H = len(result)
        for i in range(L+1):
            five_symb = result[0:H // L]
            new_result += five_symb + " "
            result = result[5:]
        print("Результат зашифровки: ", new_result)
        return new_result
    if action == "decode":  # Действия для расшифрования
        result = ""
        # В вводимой строке из пятёрок и пробелов убираю пробелы
        message = message.replace(" ", "")
        array = []
        L = len(message) // 2
        for i in range(L):  # Делю строку на массив двоичных чисел
            array.append(message[0:2])
            message = message[2::]
        for i in range(0, len(array), 2):  # Расшифровываю
            # Решаю модульное сравнение относительно M
            M = solve_linear_congruence(int(array[i])**X, int(array[i+1]), P)
            result += alphabet[M-1]  # Добавляю в результат
        print("Результат расшифровки: ", result)
        return result


def solve_linear_congruence(a, b, m): #Функция для решения модульных сравненений
    g = math.gcd(a, m) #НОД a и m
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return pow(a, -1, m) * b % m #вычисление


# p = sys.argv[1]
# g = sys.argv[2]
# x = sys.argv[3]
# isEncode = sys.argv[4]
# message = sys.argv[5]

# elgamal(p, g, x, isEncode, message.lower())