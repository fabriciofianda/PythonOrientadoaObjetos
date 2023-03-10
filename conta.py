class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos... {}".format(self))
        print("Construindo objetos... {}".format(Conta))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo equivalente a {} do Titular {} ".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_retirar(self, valor_de_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_de_saque <= valor_disponivel

    def retirar(self, valor):
        if (self.__pode_retirar(valor)):
            self.__saldo -= valor
        else:
            print("limite indisponivel...")

    def transferir(self, valor, origem, destino):
        self.retirar(valor)
        destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero
    @property
    def titular(self):
        return self.__titular.title()
    @property
    def saldo(self):
        return self.__saldo
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigo_banco():
        return "001"
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}