'''

BEECROWD LIXOOO!!!1!!

randomlist = []
for i in range(1,100):
    n = int(input())
    randomlist.append(n)
print(max(randomlist))
print(randomlist.index(max(randomlist)) + 1)
'''

n = int(input())
x=0

for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a

print(maior)
print(posicao)