from Crypto.Util import number
import os
from funcoes_auxiliares import string_to_ascii, fatorar_numero, ascii_to_string

"""
Funcao utilizada para cifrar e para decifrar
C = texto_claro^e (mod n)
M = texto_cifrado^d (mod n)

Para cifrar é necessário utilizar a chave publica PU = {e, n}
Para decifrar é necessário utilizar a chave privada PR = {d, n}

texto: pode ser o texto_claro(utiliza 'e') ou o texto_cifrado('utiliza d')
chave_fatorada: pode ser e ou d, com a chave fatorada em tamanho menor em um array
"""
def aritmetica_modular(texto, chave_fatorada, n):  #ascii code ao invez de texto
    resultado = 1
    for chave in chave_fatorada:
        resultado *= pow(texto, chave) % n
    return resultado % n

"""
Recebo uma string e retorno uma lista de cifras
"""
def encriptar(texto, e, n):
    lista_ascii = string_to_ascii(texto)
    e_fatorado = fatorar_numero(e)

    return [aritmetica_modular(i, e_fatorado, n) for i in lista_ascii]

def decriptar(lista_cifras, d, n):
    d_fatorado = fatorar_numero(d)
    resultado = [aritmetica_modular(i, d_fatorado, n) for i in lista_cifras]
    return ascii_to_string(resultado)

"""
n = p * q
"""
def gerar_n():
    n_tamanho = 8  # tamanho do numero primo

    p = number.getPrime(n_tamanho, os.urandom)
    print(p)
 
    q = number.getPrime(n_tamanho, os.urandom)
    print(q)

    return p * q

def phi_n(p, q):
    return (p - 1) * (q - 1) 

# mdc(e, phi(n)) = 1   1 < e < phi(n)
def gerar_e():
    pass

# e * d = 1 mod(phi(n))
def gerar_d():
    pass
