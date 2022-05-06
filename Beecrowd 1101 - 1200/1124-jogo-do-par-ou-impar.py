numero = int(input())

antecessor = numero - 1
sucessor = numero + 1

if (antecessor - 1) % 2 == 1:
    antecessor = antecessor - 1

elif (sucessor + 1) % 2 == 0:
    sucessor = sucessor + 1

print(antecessor, sucessor)
