import math

InicialX = input().split(' ')
X1, Y1 = InicialX
InicialY = input().split(' ')
X2, Y2 = InicialY

Distancia = math.sqrt(((float(X2) - float(X1))**2) + ((float(Y2) - float(Y1))**2))

print(f'{Distancia:0.4f}')
