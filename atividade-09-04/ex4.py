class contaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            slef.__saldo -= valor
    def mostrar_saldo(self):
        print("Saldo de:", self.__saldo)
    def mostrarTitular(self):
        print("Correntista", self.__titular)

conta = contaBancaria("Ana")
conta.depositar(5000)