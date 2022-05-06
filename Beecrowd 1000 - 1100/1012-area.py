Inicial = input().split(' ')
A, B, C = Inicial


n = 3.14159
Triangulo = float(A) * float(C) / 2
Circulo = n * float(C)**2
Trapezio = (float(A) + float(B)) * float(C) /2
Quadrado = float(B) ** 2
Retangulo = float(A) * float(B)

print("TRIANGULO: %0.3f" % Triangulo)
print("CIRCULO: %0.3f" % Circulo)
print("TRAPEZIO: %0.3f" % Trapezio)
print("QUADRADO: %0.3f" % Quadrado)
print("RETANGULO: %0.3f" % Retangulo)
