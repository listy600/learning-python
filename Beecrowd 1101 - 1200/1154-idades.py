idade = int(input())
contador = 0
media = 0.00

while idade >= 0:
    media = (idade + media)
    contador += 1
    idade = int(input())
    if idade < 0:
        media = media / contador
        print(f'{media:.2f}')
