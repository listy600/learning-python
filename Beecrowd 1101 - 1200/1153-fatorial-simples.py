N = int(input())
contador = N

while contador > 0:
    if contador == N:
        contador -= 1
        continue
    else:
        N = N * contador
        contador -= 1
print(N)
