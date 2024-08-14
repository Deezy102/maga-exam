def obmen(n, a, ka, kb):
    print("Открытые данные:\n")

    if a >= n or a <= 1:
        return "\nОшибка. 1 < a < n."
        exit()

    if ka <= 2 or ka >= n-1:
        return "\nОшибка. 2 < Ka < n-1."
        exit()
    ya = (a ** ka) % n
    if ya == 1:
        return "Ошибка. Открытый ключ не может быть равен 1."
        exit()
    print("\nYa:", ya)

    if kb <= 2 or kb >= n-1:
        return ("\nОшибка. 2 < Ka < n-1.")
        exit()
    yb = (a ** kb) % n

    if yb >= n or yb == 1:
        return ("Ошибка. Открытый ключ не может быть больше модуля n и равным 1.")
        exit()
    print("\nYb:", yb)
    Key1 = (yb ** ka) % n
    Key2 = (ya ** kb) % n
    print("\nОбщий секретный ключ К: ", Key1, Key2)
    return f"Открытые данные: n={n}, a={a}, ya={ya}, yb={yb}. Общий секретный ключ: {Key1} = {Key2}"

