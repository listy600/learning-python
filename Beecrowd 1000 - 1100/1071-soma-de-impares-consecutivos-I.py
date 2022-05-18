X = int(input())
Y = int(input())
soma = 0

if X == Y:
    print('0')

if X <= Y:
    contador = X + 1
    while contador != Y:
        if contador % 2 == 1 or contador % 2 == -1 and X < contador < Y:
            soma = contador + soma
        contador += 1
    print(soma)

if Y < X:
    contador = Y + 1
    while contador != X:
        if contador % 2 == 1 or contador % 2 == -1 and Y < contador < X:
            soma = contador + soma
        contador += 1
    print(soma)
