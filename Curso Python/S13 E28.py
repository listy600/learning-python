import os

num1 = 89
contador = 0
arquivo = open('entrada.txt', 'r')
saida = open('saida.txt', 'a+')

while contador != 90:
    temp = arquivo.read(1)
    arquivo.seek(num1)
    saida.write(temp)
    contador += 1
    num1 -= 1



arquivo.close()
saida.close()