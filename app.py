from flask import Flask, render_template, session, request, redirect, url_for, flash
from simpleReplacement import encodeATBASH, encodeCesar, decodeCesar, encodePolybius, decodePolybius
from simpleReplacement1000 import encodeATBASH as enATBASH1000
from simpleReplacement1000 import encodeCesar as enCesar1000
from simpleReplacement1000 import decodeCesar as deCesar1000
from simpleReplacement1000 import encodePolybius as enPolybius1000
from simpleReplacement1000 import decodePolybius as dePolybius1000
from multivaluedSubstitution import encode_Tritemius, decode_Tritemius, encode_Belaso, decode_Belaso, encode_Vigenere, decode_Vigenere
from multivaluedSubstitution1000 import encode_Tritemius as enTritemius1000
from multivaluedSubstitution1000 import decode_Tritemius as deTritemius1000
from multivaluedSubstitution1000 import encode_Belaso as enBelaso1000
from multivaluedSubstitution1000 import decode_Belaso as deBelaso1000
from multivaluedSubstitution1000 import encode_Vigenere as enVigenere1000
from multivaluedSubstitution1000 import decode_Vigenere as deVigenere1000
from blockSubstitution import encode_matrix_cipher, decode_matrix_cipher, encode_Playfair_cipher
from blockSubstitution1000 import encode_matrix_cipher as enMatrix1000
from blockSubstitution1000 import decode_matrix_cipher as deMatrix1000
from blockSubstitution1000 import encode_Playfair_cipher as enPlayfair1000
from shennon import encrypt_shenon, decrypt_shenon
from magmagamma import encryptmessage as enMagmaGamma
from magmagamma import decryptmessage as deMagmaGamma
from magmasimple import encryptmessage as enMagmaSimple
from magmasimple import decryptmessage as deMagmaSimple
from a51 import encryptmessage as enA51
from a51 import decryptmessage as deA51
from aes import encryptmessage as enAES
from aes import decryptmessage as deAES
from rsa import encryptmessage as enRSA
from rsa import decryptmessage as deRSA
from rsa_ecp import genecp as genRSAECP
from rsa_ecp import checkecp as checkRSAECP
from elgamal_ecp import gencp as genElgamalECP
from elgamal_ecp import checkcp as checkElgamalECP
from gost94 import gencp as genGOST94
from gost94 import checkcp as checkGOST94
from dh import obmen
from permutation import encode_vert_permutation, decode_vert_permutation
from ecc import ecc as enECC
from elgamal import elgamal as enElgamal 
from a52 import encryptmessage as enA52
from a52 import decryptmessage as deA52
app = Flask(__name__)
application = app
app.config.from_pyfile('config.py')
ECP_OPERATIONS = ['Генерация', 'Проверка']
OPERATIONS = ['Зашифровать','Расшифровать']
TYPE = ['Тест', 'Текст']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alg/atbash', methods=['GET', 'POST'])
def atbash():
    result = None
    if request.method == 'POST':
        if request.form.get('type') == 'Тест':
            result = encodeATBASH(request.form.get('original_text'))
        else:
            result = enATBASH1000(request.form.get('original_text'))
    return render_template('alg/atbash.html', operations=OPERATIONS, type=TYPE, result=result)

@app.route('/alg/cesar', methods=['GET', 'POST'])
def cesar():
    result = None
    key = None
    if request.method == 'POST':
        key = int(request.form.get('key'))
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encodeCesar(request.form.get('original_text'), shift=key)
            else:
                result = decodeCesar(request.form.get('original_text'), shift=((-1) * int(key)))
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enCesar1000(request.form.get('original_text'), shift=key)
            else:
                result = deCesar1000(request.form.get('original_text'), shift=((-1) * int(key)))
    return render_template('alg/cesar.html', operations=OPERATIONS, type=TYPE, key=key, result=result)

@app.route('/alg/polybius', methods=['GET', 'POST'])
def polybius():
    result = None
    key = None
    if request.method == 'POST':
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encodePolybius(request.form.get('original_text'))
            else:
                result = decodePolybius(request.form.get('original_text'))
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enPolybius1000(request.form.get('original_text'))
            else:
                result = dePolybius1000(request.form.get('original_text'))
    return render_template('alg/polybius.html', operations=OPERATIONS, type=TYPE, result=result)
    
@app.route('/alg/tritemius', methods=['GET', 'POST'])
def tritemius():
    result = None
    if request.method == 'POST':
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encode_Tritemius(request.form.get('original_text'))
            else:
                result = decode_Tritemius(request.form.get('original_text'))
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enTritemius1000(request.form.get('original_text'))
            else:
                result = deTritemius1000(request.form.get('original_text'))
    return render_template('alg/tritemius.html', operations=OPERATIONS, type=TYPE, result=result)

@app.route('/alg/belaso', methods=['GET', 'POST'])
def belaso():
    result = None
    key = None
    if request.method == 'POST':
        key = str(request.form.get('key'))
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encode_Belaso(request.form.get('original_text'), key)
            else:
                result = decode_Belaso(request.form.get('original_text'), key)
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enBelaso1000(request.form.get('original_text'), key)
            else:
                result = deBelaso1000(request.form.get('original_text'), key)
    return render_template('alg/belaso.html', operations=OPERATIONS, type=TYPE, key=key, result=result)

@app.route('/alg/vigenere', methods=['GET', 'POST'])
def vigenere():
    result = None
    key = None
    if request.method == 'POST':
        key = str(request.form.get('key'))
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encode_Vigenere(request.form.get('original_text'), key)
            else:
                result = decode_Vigenere(request.form.get('original_text'), key)
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enVigenere1000(request.form.get('original_text'), key)
            else:
                result = deVigenere1000(request.form.get('original_text'), key)
    return render_template('alg/vigenere.html', operations=OPERATIONS, type=TYPE, key=key, result=result)

@app.route('/alg/matrix', methods=['GET', 'POST'])
def matrix():
    result = None
    key = None
    if request.method == 'POST':
        key = str(request.form.get('key'))
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encode_matrix_cipher(request.form.get('original_text'), key)
            else:
                result = decode_matrix_cipher(request.form.get('original_text'), key)
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enMatrix1000(key, request.form.get('original_text'))
            else:
                result = deMatrix1000(key, request.form.get('original_text'))
    return render_template('alg/matrix.html', operations=OPERATIONS, type=TYPE, key=key, result=result)

@app.route('/alg/playfair', methods=['GET', 'POST'])
def playfair():
    result = None
    key = None
    if request.method == 'POST':
        key = str(request.form.get('key'))
        if request.form.get('type') == 'Тест':
            if request.form.get('operation') == 'Зашифровать':
                result = encode_Playfair_cipher(key, request.form.get('original_text'), action='encode')
            else:
                result = encode_Playfair_cipher(key, request.form.get('original_text'), action='decode')
        else:
            if request.form.get('operation') == 'Зашифровать':
                result = enPlayfair1000(key, request.form.get('original_text'), action='encode')
            else:
                result = enPlayfair1000(key, request.form.get('original_text'), action='decode')
    return render_template('alg/playfair.html', operations=OPERATIONS, type=TYPE, key=key, result=result)


@app.route('/alg/shennon', methods=['GET', 'POST'])
def shennon():
    result = ('', '')
    t0 = None
    a = None
    c = None
    gamma = None
    if request.method == 'POST':
        if request.form.get('operation') == 'Зашифровать':
            t0 = int(request.form.get('t0'))
            a = int(request.form.get('a'))
            c = int(request.form.get('c'))
            text = request.form.get('original_text')
            n = 33
            chunks = [text[i:i+n] for i in range(0, len(text), n)]
            res1 = ''
            res2 = []
            for chunk in chunks:
                sub_res = encrypt_shenon(chunk, t0, a, c)
                res1 += sub_res[0]
                res2 += sub_res[1]
            result = (res1, res2)
        else:
            text = request.form.get('original_text')
            gamma = request.form.get('gamma').split(', ')
            for i in range(len(gamma)):
                gamma[i] = int(gamma[i])
            n = 33
            chunks = [text[i:i+n] for i in range(0, len(text), n)]
            r1 = ''
            def chunkify(items, chunk_size):
                for i in range(0, len(items), chunk_size):
                    yield items[i:i+chunk_size]
            gamma_chunks = chunkify(gamma, 33)
            gamma_chunks = list(gamma_chunks)
            print(len(chunks), len(gamma_chunks))
            for i in range(len(chunks)):
                chunk = chunks[i]
                gamma = gamma_chunks[i]
                sub_res = decrypt_shenon((chunk, gamma))
                r1 += sub_res
            result = (r1,'')
    return render_template(
                            'alg/shennon.html', 
                            operations=OPERATIONS, 
                            t0=t0, 
                            a=a,
                            c=c,
                            result_text=result[0],
                            result_gamma=result[1]
                        )

@app.route('/alg/magmagamma', methods=['GET', 'POST'])
def magmagamma():
    key = None
    result = None
    iv = None
    if request.method == 'POST':
        key = request.form.get('key')
        iv = request.form.get('iv')
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enMagmaGamma(text, key, iv)
        else:
            result = deMagmaGamma(text, key, iv)
    return render_template('alg/magmagamma.html', operations=OPERATIONS, key=key, result=result)

@app.route('/alg/magmasimple', methods=['GET', 'POST'])
def magmasimple():
    key = None
    result = None
    iv = None
    if request.method == 'POST':
        key = request.form.get('key')
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enMagmaSimple(text, key)
        else:
            result = deMagmaSimple(text,key)
    return render_template('alg/magmasimple.html', operations=OPERATIONS, key=key, result=result)

@app.route('/alg/a5_1', methods=['GET', 'POST'])
def a5_1():
    key = None
    result = None
    if request.method == 'POST':
        key = request.form.get('key')
        iv = int(request.form.get('iv'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enA51(text, key, iv)
        else:
            result = deA51(text, key, iv)
    return render_template('alg/a5_1.html', operations=OPERATIONS, key=key, result=result)

@app.route('/alg/a52', methods=['GET', 'POST'])
def a52():
    key = None
    result = None
    if request.method == 'POST':
        key = request.form.get('key')
        iv = int(request.form.get('iv'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enA52(text,key,iv)
        else:
            result = deA52(text, key, iv)
    return render_template('alg/a52.html', operations=OPERATIONS, key=key, result=result)

@app.route('/alg/aes', methods=['GET', 'POST'])
def aes():
    key = None
    result = None
    if request.method == 'POST':
        key = request.form.get('key')
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enAES(text, key)
        else:
            result = deAES(text, key)
    return render_template('alg/aes.html', operations=OPERATIONS, key=key, result=result)

@app.route('/alg/rsa', methods=['GET', 'POST'])
def rsa():
    p = None
    q = None
    e = None
    result = None
    if request.method == 'POST':
        p = int(request.form.get('p'))
        q = int(request.form.get('q'))
        e = int(request.form.get('e'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Зашифровать':
            result = enRSA(text, p, q, e)
        else:
            result = deRSA(text, p, q, e)
    return render_template('alg/rsa.html', operations=OPERATIONS, result=result)

@app.route('/alg/rsa_ecp', methods=['GET', 'POST'])
def rsa_ecp():
    p = None
    q = None
    e = None
    result = None
    if request.method == 'POST':
        p = int(request.form.get('p'))
        q = int(request.form.get('q'))
        e = int(request.form.get('e'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Генерация':
            result = genRSAECP(text, p, q, e, request.form.get('type'))
        else:
            result = checkRSAECP(text, p, q, e,
                                int(request.form.get('sign')),
                                request.form.get('type'))
    return render_template('alg/rsa_ecp.html', operations=ECP_OPERATIONS, type=TYPE, result=result)

@app.route('/alg/elgamal_ecp', methods=['GET', 'POST'])
def elgamal_ecp():
    p = None
    g = None
    x = None
    k = None
    a = None
    b = None
    result = None
    if request.method == 'POST':
        p = int(request.form.get('p'))
        g = int(request.form.get('g'))
        x = int(request.form.get('x'))
        k = int(request.form.get('k'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Генерация':
            result = genElgamalECP(text,p,g,x,k)
        else:
            result = checkElgamalECP(text,p,g,x,k,
                                    int(request.form.get('a')),
                                    int(request.form.get('b')))
    return render_template('alg/elgamal_ecp.html', operations=ECP_OPERATIONS, result=result)

@app.route('/alg/gost94', methods=['GET', 'POST'])
def gost94():
    p = None
    q = None
    a = None
    x = None
    k = None
    r = None
    s = None
    result = None
    if request.method == 'POST':
        p = int(request.form.get('p'))
        q = int(request.form.get('q'))
        a = int(request.form.get('a'))
        x = int(request.form.get('x'))
        k = int(request.form.get('k'))
        text = request.form.get('original_text')
        if request.form.get('operation') == 'Генерация':
            result = genGOST94(text,p,q,a,x,k)
        else:
            result = checkGOST94(text,p,q,a,x,k,
                                int(request.form.get('r')),
                                int(request.form.get('s')))
    return render_template('alg/gost94.html', operations=ECP_OPERATIONS, result=result)

@app.route('/alg/dh', methods=['GET', 'POST'])
def dh():
    result = None
    if request.method == 'POST':
        a = int(request.form.get('a'))
        n = int(request.form.get('n'))
        ka = int(request.form.get('ka'))
        kb = int(request.form.get('kb'))
        result = obmen(n,a,ka,kb)
    return render_template('alg/dh.html', result=result)

@app.route('/alg/vert', methods=['GET', 'POST'])
def vert():
    result = None
    key = None
    if request.method == 'POST':
        text = request.form.get('original_text')
        key = request.form.get('key')
        if request.form.get('operation') == 'Зашифровать':
            result = encode_vert_permutation(text, key)
            result = result.replace('/', '')
            result = result.replace('%', '')
            result = result.replace('  ', ' ')
        else:
            df = open('D:/aucheba/python/crypto2/decode.txt', 'r', encoding='UTF-8')
            result = decode_vert_permutation(df.read(), key)
            df.close()
    return render_template('alg/vert.html',  operations=OPERATIONS, result=result)
    'p_, a_, b_, Cb_, action, x_, y_, k_, m_, e_'

@app.route('/alg/ecc', methods=['GET', 'POST'])
def ecc():
    result = 0
    p = 0
    a = 0
    b = 0
    cb = 0
    action = None
    x = 0
    y = 0
    k = 0
    m = 0
    e = 0
    if request.method == 'POST':
        p = int(request.form.get('p') or '0')
        a = int(request.form.get('a') or '0')
        b = int(request.form.get('b') or '0')
        cb = int(request.form.get('cb') or '0')
        x = int(request.form.get('x') or '0')
        y = int(request.form.get('y') or '0')
        k = int(request.form.get('k') or '0')
        m = int(request.form.get('m') or '0')
        e = int(request.form.get('e') or '0')
        if request.form.get('operation') == 'Зашифровать':
            result = enECC(p,a,b,cb,'Зашифровать',x,y,k,m,e)
        else:
            result = enECC(p,a,b,cb,'Расшифровать',x,y,k,m,e) 
    return render_template('alg/ecc.html', operations=OPERATIONS, result=result)

@app.route('/alg/elgamal', methods=['GET', 'POST'])
def elgamal():
    result = ''
    if request.method == 'POST':
        p = int(request.form.get('p') or '0')
        g = int(request.form.get('g') or '0')
        x = int(request.form.get('x') or '0')
        m = (request.form.get('m') or '')
        if request.form.get('operation') == 'Зашифровать':
            result = enElgamal(p,g,x,'encode',m)
        else:
            result = enElgamal(p,g,x,'decode',m)
    return render_template('alg/elgamal.html', operations=OPERATIONS, result=result)