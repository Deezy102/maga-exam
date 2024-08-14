# -*- coding: utf-8 -*-
def encrypt_shenon(text, t0, a, c):
    t = []
    t.append(t0)
    res = ''
    i = 1
    for symbol in text:
     
        symbol = ord(symbol)
       
        res += chr((symbol + t[i - 1]) % 2 ** 16)
        t.append((a*t[i-1] + c) % 2**16)
        i += 1
    print(res, t)
    return (res, t)

def decrypt_shenon(tpl):
    text = tpl[0]
    t = []
    t+=tpl[1]
    res = ''
    i = 1
    for symbol in text:
        symbol = ord(symbol)
        res += chr((symbol - t[i - 1]) % 2**16)
        i += 1
    return res

if __name__ == '__main__':
    print(res)
    print(decrypt_shenon(res))