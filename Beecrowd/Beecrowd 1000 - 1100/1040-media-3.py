numeros = input().split(' ')
numero_um, numero_dois, numero_tres, numero_quatro = numeros
numero_um = float(numero_um)
numero_dois = float(numero_dois)
numero_tres = float(numero_tres)
numero_quatro = float(numero_quatro)

media = ((numero_um * 2) + (numero_dois * 3) + (numero_tres * 4) + (numero_quatro * 1)) / 10

print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif media >= 5 and media < 7:
    print('Aluno em exame.')
    nota_exame = float(input(''))
    print('Nota do exame: %.1f' % nota_exame)
    nota_final = (media + nota_exame) / 2
    if nota_final >= 5:
        print('Aluno aprovado.')
    elif nota_final < 5:
        print('Aluno reprovado.')
    print(f'Media final: {nota_final:.1f}')
