"""

Teste com geradores

"""

# Generator

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1) # Gerador

print(next(ge1))
print(next(ge1))
print(next(ge1))

# Generation Expression

ge2 = (num for num in range(1,10))

print(ge2) # Generation Expression

print(next(ge2))
print(next(ge2))
print(next(ge2))

print('------')

print(sum(num for num in range(1, 10)))

