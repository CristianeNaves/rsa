from rsa import gerar_n, gerar_e, gerar_d, encriptar, decriptar

def main():
    #n = gerar_n()
    #e = gerar_e()  ->precisa arrumar
    #d = gerar_d()  ->precisa arrumar para funcionar direito

    n = 187
    e = 7
    d = 23

    texto = "Hello World!"

    lista_cifras = encriptar(texto, e, n)
    print(lista_cifras)

    texto_decifrado = decriptar(lista_cifras, d, n)
    print(texto_decifrado)

main()