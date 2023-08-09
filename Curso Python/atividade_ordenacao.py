# Análise e Projeto de Algoritmos
# AC2: Ciência da Computação
#
# Email Impacta: tiago.natal@aluno.faculdadeimpacta.com.br

def esta_ordenada(lista):
    if len(lista) <= 1:
        return True
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True


def ordenacao_bolha(lista):
    n = len(lista)
    flag = True
    while flag:
        flag = False
        for i in range(0, n-1):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                flag = True
        n -= 1