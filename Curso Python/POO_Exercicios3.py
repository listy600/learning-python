
class Pessoa:
    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade
        print('Construtor Padrão')

    def __str__(self):
        return self.__nome
    
    def Exibe(self):
        return f'{self.__codigo} {self.__nome} {self.__idade}'
    
    def Sobrecarga(self, carga):
        if carga == 1:
            return f'{self.__codigo} {self.__nome} {self.__idade}'
        else:  
            return f'{self.__codigo} {self.__nome}'
        

carlos = Pessoa(2200143, 'Carlos', 39)

print(carlos)
print(carlos.Exibe())
print(carlos.Sobrecarga(1))
print(carlos.Sobrecarga(2))