preco = float(input())
quantidade = int(input())

valor_total = preco * quantidade
valor_desconto = valor_total * (0.9 - (quantidade/100))

print('%0.2f' % valor_total)
print('%0.2f' % valor_desconto)
