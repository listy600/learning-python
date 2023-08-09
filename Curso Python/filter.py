
paises = ['', 'Brasil', '', 'Equador', ' ', 'Argentina']

print(list(filter(lambda pais: len(pais) > 1, paises)))

# A diferença entre map e filter é:
# map -> recebe dois parâmetros, uma função e um interável e retorna um objeto mapeando a função para cada elemento do interável
# filter -> Recebe dois parâmetros, uma função e um interável e retorna um objeto filtrando apenas os elementos de acordo com a função