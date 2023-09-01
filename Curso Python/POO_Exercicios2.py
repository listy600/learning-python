
class Elevador:
    def __init__(self, andares, capacidade):
        self.__andar_atual = 0
        self.__andares = andares
        self.__capacidade = capacidade
        self.__num_atual = 0
    
    def inicializa(self):
        self.__andar_atual = 0
        self.__num_atual = 0
    
    def entra(self):
        if self.__num_atual < self.__capacidade:
            self.__num_atual += 1

    def sai(self):
        if self.__num_atual > 0:
            self.__num_atual -= 1
    
    def sobe(self):
        if self.__andar_atual < self.__andares:
            self.__andar_atual += 1
    
    def desce(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1

predio1 = Elevador(5, 8)
print(predio1.__dict__)
predio1.entra()
predio1.entra()
predio1.sobe()
print(predio1.__dict__)
predio1.desce()
predio1.sai()
predio1.sai()
print(predio1.__dict__)