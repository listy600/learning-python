Inicial = input().split(' ')
A, B = Inicial


if (int(A) % int(B) == 0) or (int(B) % int(A) == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
