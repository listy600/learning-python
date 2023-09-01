
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    
    def get_altura(self):
        return self.__altura
    
    def dados_pessoa(self):
        print(f'O nome é {self.__nome} com {self.__idade} anos e {self.__altura} de altura.')

pessoa1 = Pessoa('Carlos', 39, 1.80)

pessoa1.dados_pessoa()

print(pessoa1.get_nome())