
class Pessoa():
    def __init__(self, nome, idade, conta):
        self.nome = nome
        self._idade = idade
        self.__saldo = 0
        self.conta = conta

    def mostar_nome(self):
        return self.nome
    
    def mostrar_idade(self):
        return self._idade

    def mostrar_saldo(self):
        return self.__saldo
        
pessoa = Pessoa("mario",27)




    