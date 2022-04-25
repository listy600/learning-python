VENDEDOR = str(input())
SALARIO = float(input())
TOTAL = float(input())

RECEBER = (TOTAL / 100) * 15 + SALARIO

print("TOTAL = R$ %0.2f" % RECEBER)
