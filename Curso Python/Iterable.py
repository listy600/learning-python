def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 5, 6]

    meu_for(lista1)

    for _ in lista1:
        print(_)