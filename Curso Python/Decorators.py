"""
def seja_educado(funcao):
    print('Foi um prazer conhecer você!')
    funcao()
    return 'Tenha um ótimo dia!'
    

def soma():
    print('olá')

print(seja_educado(soma))

"""


def seja_educado(funcao):
    def educacao():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return educacao

@seja_educado
def apresentando():
    print('Meu nome é Tiago Mateus')


apresentando()