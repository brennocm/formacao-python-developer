class Conta:
    def __init__(self, saldo = 0, investimento = 100):
        self._saldo = saldo #Recurso privado
        self.investimento = investimento #Recurso público

    def depositar(self, valor):
        self._saldo += valor

    def sacar (self, valor):
        pass

#Instanciando fora da classe, visto que estamos 
#utilizando um recurso público
conta = Conta(100)
conta.investimento += 100
print(conta.investimento)

#Instanciando um recurso privado através de um método
conta1 = Conta(1000)
conta1.depositar(100)
print(conta1._saldo)
