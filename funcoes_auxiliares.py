"""
Recebe um numero grande e simplifica ele em fatores menores de 8,4,2 e 1.

num: 23
retorno: [8,8,4,2,1]
"""
def fatorar_numero(num):
    resultado = []
    quantidade_15 = int(num/15)
    mod_15 = num % 15

    num = num - (15 * quantidade_15)

    resultado.append(8) if int(num/8) else None
    num = num % 8
    resultado.append(4) if int(num/4) else None
    num = num % 4
    resultado.append(2) if int(num/2) else None
    num = num % 2
    resultado.append(1) if int(num/1) else None

    for i in range(0, quantidade_15):
        resultado.append(1)
        resultado.append(2)
        resultado.append(4)
        resultado.append(8)

    return resultado

"""
Recebe uma string e retorna uma lista dos codigos ascii do texto
"""
def string_to_ascii(texto):
    return list(map(lambda s: ord(s), list(texto)))

"""
Recebe uma lista de códigos ascii e retorna uma string
"""
def ascii_to_string(simbolos_ascii):
    resultado = list(map(lambda s: chr(s), simbolos_ascii))
    return "".join(resultado)