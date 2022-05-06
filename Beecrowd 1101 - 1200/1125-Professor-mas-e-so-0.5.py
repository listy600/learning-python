nota_trabalho = float(input())
nota_prova = float(input())

media = (nota_prova + nota_trabalho) / 2

if media >= 6:
    print('aprovado')
elif media <= 6 and nota_trabalho <= 2:
    print('reprovado')
else:
    print('talvez com a sub')

