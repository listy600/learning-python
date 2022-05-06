dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
diadasemana = input()
quantidadededias = int(input())

if quantidadededias == 0:
    print('chega hoje!')
else:
    indexdiadasemana = dias.index(diadasemana)
    nova_lista = dias[indexdiadasemana + 1:len(dias)] + dias[0:indexdiadasemana]
    diadasemana = nova_lista[quantidadededias - 1]
    print('sera entregue', diadasemana)
