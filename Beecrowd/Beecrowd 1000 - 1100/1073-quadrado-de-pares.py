N = int(input())
contador = 1

while N >= contador:
    if contador % 2 == 0:
        print(f'{contador}^2 = {contador**2}')
    contador += 1
