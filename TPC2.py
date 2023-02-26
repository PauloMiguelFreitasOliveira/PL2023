import sys

def somaSeq():
    ligado = 0
    soma = 0
    for linha in sys.stdin:
        linha = linha.strip()
        if linha == "off":
            ligado = 1   
        elif linha == "on":
            ligado = 0
        elif linha == "=":
            print(soma)
        elif ligado == 0 and linha.isdigit():
             soma = soma + int(linha)
    return soma

soma = somaSeq()
