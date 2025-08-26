class Conta():
    def __init__(self, num_conta, num_agencia, saldo):
        
        if num_conta <0 or num_agencia <0:
            raise f"A conta e/ou agencia não pode ser menor que 0 (zero)"
        
        self._num_conta = num_conta
        self._num_agencia = num_agencia
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor
        return True
    
    def sacar(self, valor):
        if self.get_saldo() < valor:
            raise Exception("Saldo insuficiente")
        self.__saldo -= valor
        print(f"Saque de R$ {valor:.2f} aprovado")
        
        return True

    def transferir(self, valor, conta_destino,):
        if self.get_saldo() < valor:
            raise Exception("saldo insuficiente")
        
        conta_destino.depositar(valor)
        self.sacar(valor)
        
        print(f"O valor de R$ {valor:.2f} foi depositado na conta {conta_destino}")
        return True

        
