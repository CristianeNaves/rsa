from Crypto.Util import number
from sympy import mod_inverse
from math import gcd
from random import randint
import os
from funcoes_auxiliares import string_to_ascii, fatorar_numero, ascii_to_string

class RSA:
    def __init__(self):
        self.n = self.gerar_n()
        self.gerar_e()
        print("e: ")
        print(self.e)
        self.gerar_d()
        print("d: ")
        print(self.d)

        #self.n = 187
        #self.e = 7
        #self.d = 23

    """
    n = p * q
    """
    def gerar_n(self):
        n_tamanho = 8  # tamanho do numero primo

        self.p = number.getPrime(n_tamanho, os.urandom)
        print(self.p)
 
        self.q = number.getPrime(n_tamanho, os.urandom)
        print(self.q)

        self.phi_n = (self.p - 1) * (self.q - 1)

        return self.p * self.q

    """
    Recebo uma string e retorno uma lista de cifras
    """
    def encriptar(self, texto):
        lista_ascii = string_to_ascii(texto)
        e_fatorado = fatorar_numero(self.e)

        return [self.aritmetica_modular(i, e_fatorado) for i in lista_ascii]

    def decriptar(self, lista_cifras):
        d_fatorado = fatorar_numero(self.d)
        resultado = [self.aritmetica_modular(i, d_fatorado) for i in lista_cifras]
        return ascii_to_string(resultado)

    """
    Funcao utilizada para cifrar e para decifrar
    C = texto_claro^e (mod n)
    M = texto_cifrado^d (mod n)

    Para cifrar é necessário utilizar a chave publica PU = {e, n}
    Para decifrar é necessário utilizar a chave privada PR = {d, n}

    texto: pode ser o texto_claro(utiliza 'e') ou o texto_cifrado('utiliza d')
    chave_fatorada: pode ser e ou d, com a chave fatorada em tamanho menor em um array
    """
    def aritmetica_modular(self, texto, chave_fatorada):  #ascii code ao invez de texto
        resultado = 1
        for chave in chave_fatorada:
            resultado *= pow(texto, chave) % self.n
        return resultado % self.n
    

    # mdc(e, phi(n)) = 1   1 < e < phi(n)
    def gerar_e(self):
        self.e = randint(2, self.phi_n)
    
        if gcd(self.e, self.phi_n) != 1:
            self.gerar_e()

    # e * d = 1 mod(phi(n))
    def gerar_d(self):
        self.d = mod_inverse(self.e, self.phi_n)


rsa = RSA()
lista_encriptada = rsa.encriptar("Agora, passaremos à questão da complexidade computacional exigida para usar o RSA. Existem, na realidade, dois pontos a considerar: encriptação/decriptação e geração de chave. Vamos examinar primeiro o processo de encriptação e decriptação, para depois considerarmos a geração de chave.")
print(lista_encriptada)
print(rsa.decriptar(lista_encriptada))